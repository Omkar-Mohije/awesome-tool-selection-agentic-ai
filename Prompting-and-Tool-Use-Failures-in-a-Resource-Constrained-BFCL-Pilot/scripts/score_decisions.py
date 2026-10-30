"""Apply the attributed published BFCL attempt-decision scorer to an actual output ZIP."""
import argparse,csv,hashlib,importlib.util,json,tempfile,urllib.request,zipfile
from pathlib import Path

def score(archive,output,cache):
    archive,output,cache=map(Path,(archive,output,cache))
    lock=json.loads((Path(__file__).resolve().parents[1]/'configs/published_scorer_lock.json').read_text())
    for name,digest in lock['published_files_sha256'].items():
        dest=cache/name
        if not dest.exists() or hashlib.sha256(dest.read_bytes()).hexdigest()!=digest:
            url='https://raw.githubusercontent.com/'+lock['published_repository']+'/'+lock['published_commit']+'/'+('pairs_package/' if name.endswith(('.py','.json')) else '')+name
            with urllib.request.urlopen(url,timeout=60) as r:content=r.read()
            assert hashlib.sha256(content).hexdigest()==digest,name
            dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(content)
    spec=importlib.util.spec_from_file_location('attributed_scorer',cache/'score_pairs.py')
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    mut=m.Mutators(str(cache/'mutator_map.json'));man=m.load_manifest(str(cache/'pairs.json'),mut)
    eligible=m.scored_pairs(man['pairs'],mut)
    output.mkdir(parents=True,exist_ok=True);summaries=[];availability=[]
    with zipfile.ZipFile(archive) as z:
        manifest=json.loads(z.read('manifest.json'))
        for name,digest in manifest['files'].items():assert hashlib.sha256(z.read(name)).hexdigest()==digest,name
        for condition in manifest['conditions']:
            res={c:{} for c in m.CATS}
            for name in z.namelist():
                if name.startswith('conditions/'+condition+'/result/') and name.endswith('_result.json'):
                    cat=Path(name).name.removeprefix('BFCL_v4_multi_turn_').removesuffix('_result.json')
                    assert cat in res
                    for line in z.read(name).decode().splitlines():
                        if not line.strip():continue
                        r=json.loads(line);assert isinstance(r['result'],list) and not r.get('traceback')
                        assert r['id'] not in res[cat];res[cat][r['id']]=r['result']
            included=[]
            for pair in eligible:
                c=pair['category'];key=pair['miss_id'];base=pair['base_id'];k=pair['anchor_turn']
                if key not in res[c] or base not in res['base']:continue
                exists=k<len(res[c][key]) and k<len(res['base'][base])
                availability.append(dict(condition=condition,miss_id=key,anchor_turn=k,raw_anchor_available=exists))
                if exists:included.append(pair)
            rows=[];result=m.score_model(included,res,mut,rows)
            if rows:
                with (output/(condition+'_pairs.csv')).open('w',newline='') as f:
                    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
            summaries.append(dict(condition=condition,**(result or {'n':0})))
    report=dict(attribution='Liu and Han (2026), unchanged released definition-C scorer and inherited labels',
        source=lock,archive_sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),
        run_id=manifest['run_id'],summaries=summaries,availability=availability,
        limits=['Missing raw anchors are unavailable, never counted as successful abstention.',
                'These are attempted actions, not successful execution or useful clarification.',
                'New model outputs require reference/parser compatibility review; this script does not establish semantic gold labels.'])
    (output/'decision_scores.json').write_text(json.dumps(report,indent=2)+'\n')
    return report

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--archive',required=True);p.add_argument('--output',required=True)
    p.add_argument('--cache',default='/tmp/p06_published_scorer')
    a=p.parse_args();print(json.dumps(score(a.archive,a.output,a.cache)['summaries'],indent=2))
