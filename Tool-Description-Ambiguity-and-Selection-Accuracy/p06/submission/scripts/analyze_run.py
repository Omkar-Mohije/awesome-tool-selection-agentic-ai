"""Validate a genuine BFCL output archive and export task counts and research figures."""
import argparse
import collections
import csv
import hashlib
import json
import zipfile
from pathlib import Path

def write_csv(path, rows):
    with path.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]))
        writer.writeheader();writer.writerows(rows)

def analyze(archive, output, plots=True):
    archive,output=Path(archive),Path(output)
    output.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(archive) as z:
        manifest=json.loads(z.read('manifest.json'))
        assert manifest['status'].get('generation')=='passed' and manifest['status'].get('evaluation')=='passed', 'Archive is incomplete; do not report completed model accuracy'
        study_label='prospective evaluation' if manifest.get('protocol',{}).get('protocol_id') else 'development pilot'
        for name,digest in manifest['files'].items():
            assert hashlib.sha256(z.read(name)).hexdigest()==digest,name
        expected={i for ids in manifest['selected_ids'].values() for i in ids}
        conditions=manifest['conditions']
        assert len(expected)>0 and len(conditions)==3
        summaries=[];cases=[];failures=[]
        for condition in conditions:
            raw={}
            for name in z.namelist():
                if name.startswith('conditions/'+condition+'/result/') and name.endswith('_result.json'):
                    for line in z.read(name).decode().splitlines():
                        if not line.strip():continue
                        item=json.loads(line);assert item['id'] not in raw
                        raw[item['id']]=item
            assert set(raw)==expected,(condition,'incomplete/duplicate/unexpected IDs')
            assert not any(r.get('traceback') or str(r.get('result','')).startswith('Error during inference:') for r in raw.values()),'Serving exception: save as incomplete, do not calculate model accuracy'
            observed_scores=set();total=correct=0
            for name in z.namelist():
                if not (name.startswith('conditions/'+condition+'/score/') and name.endswith('_score.json')):continue
                records=[json.loads(l) for l in z.read(name).decode().splitlines() if l.strip()]
                header=records[0];total+=header['total_count'];correct+=header['correct_count']
                category=name.rsplit('/',1)[1].removeprefix('BFCL_v4_').removesuffix('_score.json')
                selected={i for i in expected if i.rsplit('_',1)[0]==category}
                assert len(selected)==header['total_count']
                assert not observed_scores.intersection(selected)
                observed_scores.update(selected)
                bad={r['id']:r for r in records[1:]}
                assert set(bad)<=selected and len(bad)==len(selected)-header['correct_count']
                for case_id in sorted(selected):
                    failure=bad.get(case_id)
                    cases.append(dict(condition=condition,case_id=case_id,
                        family=int(case_id.rsplit('_',1)[1]),category=category,
                        task_success=int(failure is None),error_type=failure['error']['error_type'] if failure else ''))
                    if failure:failures.append(dict(condition=condition,case_id=case_id,
                        error_type=failure['error']['error_type'],
                        error_message=json.dumps(failure['error'].get('error_message'))))
            assert observed_scores==expected and total==len(expected)
            summaries.append(dict(condition=condition,successes=correct,total=total,
                                  accuracy=correct/total,failures=total-correct))
        write_csv(output/'results.csv',summaries)
        write_csv(output/'per_case.csv',cases)
        if failures:write_csv(output/'failures.csv',failures)
        counts=collections.Counter(r['error_type'] for r in failures)
        audit=dict(archive_sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),
                   verified_file_hashes=len(manifest['files']),run_id=manifest['run_id'],
                   selected_ids=manifest['selected_ids'],conditions=conditions,
                   families=sorted({r['family'] for r in cases}),first_failure_counts=dict(counts))
        (output/'analysis_verification.json').write_text(json.dumps(audit,indent=2)+'\n')
    if plots:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
        fig,ax=plt.subplots(figsize=(6.4,3.3),layout='constrained')
        labels=[r['condition'].replace('_','\n') for r in summaries]
        good=[r['successes'] for r in summaries];bad=[r['failures'] for r in summaries]
        ax.bar(labels,good,label='Task success',color='#237766')
        ax.bar(labels,bad,bottom=good,label='Task failure',color='#b34e4e')
        for x,row in enumerate(summaries):ax.text(x,row['total']/2,f"{row['successes']}/{row['total']} success",ha='center',color='white',weight='bold')
        ax.set(ylabel='Task records',title=f'Official complete-task outcomes ({study_label})')
        ax.legend(loc='upper center',bbox_to_anchor=(.5,-.22),ncol=2,frameon=False)
        for ext in ['png','pdf']:fig.savefig(output/f'task_outcomes.{ext}',dpi=180)
        plt.close(fig)
        fig,ax=plt.subplots(figsize=(6.4,3.3),layout='constrained')
        keys=list(counts)
        ax.barh([k.replace('multi_turn:','').replace('_',' ') for k in keys],[counts[k] for k in keys],color='#3d658c')
        ax.set(xlabel='Condition/task records',title='First reported task failure')
        for i,k in enumerate(keys):ax.text(counts[k]+.1,i,str(counts[k]),va='center')
        ax.set_xlim(0,max(counts.values(),default=0)+2)
        for ext in ['png','pdf']:fig.savefig(output/f'failure_types.{ext}',dpi=180)
        plt.close(fig)
    return summaries

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--archive',required=True);p.add_argument('--output',required=True)
    p.add_argument('--no-plots',action='store_true')
    a=p.parse_args()
    print(json.dumps(analyze(a.archive,a.output,not a.no_plots),indent=2))
