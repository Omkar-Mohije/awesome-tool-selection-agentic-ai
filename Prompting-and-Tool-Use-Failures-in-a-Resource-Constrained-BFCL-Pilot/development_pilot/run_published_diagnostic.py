"""Re-score the preserved pilot with the attributed, pinned published decision scorer."""
import argparse
import ast
import csv
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import urllib.request
import zipfile
from pathlib import Path

ARCHIVE_SHA256 = '4b7178e4208094c16f04cdaf83235f2986a5923f1b910496d92d545c2b1eba40'
MODEL = 'Qwen_Qwen3-4B-Instruct-2507-FC'
CONDITIONS = ('vanilla', 'generic_control', 'schema_evidence')

def run(archive, cache, output):
    archive, cache, output = map(Path, (archive, cache, output))
    assert hashlib.sha256(archive.read_bytes()).hexdigest() == ARCHIVE_SHA256
    lock = json.loads((Path(__file__).parent/'diagnostic_review/source_lock.json').read_text())
    for relative, expected in lock['published_files_sha256'].items():
        dest = cache/relative
        if not dest.exists() or hashlib.sha256(dest.read_bytes()).hexdigest() != expected:
            url = ('https://raw.githubusercontent.com/' + lock['published_repository'] + '/'
                   + lock['published_commit'] + '/'
                   + ('pairs_package/' if relative.endswith(('.py','.json')) else '') + relative)
            with urllib.request.urlopen(url,timeout=60) as response:
                content = response.read()
            assert hashlib.sha256(content).hexdigest() == expected, relative
            dest.parent.mkdir(parents=True,exist_ok=True)
            dest.write_bytes(content)
    spec = importlib.util.spec_from_file_location('published_decision_scorer',cache/'score_pairs.py')
    scorer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(scorer)
    mut = scorer.Mutators(str(cache/'mutator_map.json'))
    manifest = scorer.load_manifest(str(cache/'pairs.json'),mut)
    eligible = scorer.scored_pairs(manifest['pairs'],mut)
    output.mkdir(parents=True,exist_ok=True)
    summaries, compatibility = [], []
    with tempfile.TemporaryDirectory(prefix='p06_published_') as temp:
        temp = Path(temp)
        with zipfile.ZipFile(archive) as z:
            scores = {}
            for name in z.namelist():
                if not name.startswith('conditions/'):
                    continue
                if '/result/' in name and name.endswith('_result.json'):
                    dest = temp/name
                    dest.parent.mkdir(parents=True,exist_ok=True)
                    dest.write_bytes(z.read(name))
                elif '/score/' in name and name.endswith('_score.json'):
                    for line in z.read(name).decode().splitlines()[1:]:
                        if line.strip():
                            item=json.loads(line)
                            scores[name.split('/')[1],item['id']] = item
        for condition in CONDITIONS:
            result_root = temp/'conditions'/condition/'result'
            results = {c: scorer.load_results([str(result_root)],MODEL,c) for c in scorer.CATS}
            included = [r for r in eligible if r['miss_id'] in results[r['category']]
                        and r['base_id'] in results['base']]
            assert len(included) == 2
            for pair in included:
                k = pair['anchor_turn']
                assert k < len(results[pair['category']][pair['miss_id']])
                assert k < len(results['base'][pair['base_id']])
                base_score = scores[condition,pair['base_id']]
                miss_score = scores[condition,pair['miss_id']]
                assert base_score['possible_answer'][k] == pair['gold_anchor']
                # Removing the designated no-call turn must restore the reference trajectory.
                miss_gold = miss_score['possible_answer']
                assert miss_gold[k] == []
                assert miss_gold[:k]+miss_gold[k+1:] == base_score['possible_answer']
                checked=[]
                for case,cat,allowed in ((pair['base_id'],'base',pair['_base_tools']),
                                         (pair['miss_id'],pair['category'],pair['_miss_tools'])):
                    score = scores[condition,case]
                    official = score.get('model_result_decoded')
                    if official is None:
                        checked.append(dict(case_id=case, official_decoder_comparison='unavailable_force_terminated'))
                        continue
                    names = [ast.parse(call,mode='eval').body.func.id
                             for step in official[k] for call in step]
                    parsed = [n for n,_ in scorer.turn_calls(results[cat][case][k],allowed)]
                    assert names == parsed, (condition,case,names,parsed)
                    checked.append(dict(case_id=case, official_decoder_comparison='exact_function_name_sequence_match'))
                compatibility.append(dict(condition=condition,miss_id=pair['miss_id'],
                    anchor_turn=k, reference_trajectory_alignment=True,
                    anchor_turn_present_in_both_raw_results=True, decoder_checks=checked))
            rows=[]
            summary=scorer.score_model(included,results,mut,rows)
            summaries.append(dict(condition=condition,**summary))
            command=[sys.executable,str(cache/'score_pairs.py'),'--results',str(result_root),
                     '--per-item',str(output/f'published_{condition}_pairs.csv')]
            completed=subprocess.run(command,capture_output=True,text=True,check=True)
            (output/f'published_{condition}.log').write_text(completed.stdout+completed.stderr)
    report=dict(attribution='Liu and Han, Asking Earns Nothing (2026), published definition C scorer',
        upstream=lock, archive_sha256=ARCHIVE_SHA256, summaries=summaries,
        compatibility=compatibility, limits=[
            'Post-hoc application to two inspected development pairs, both missing-parameter; no held-out or statistical improvement claim.',
            'Mutator labels and certification are inherited from the published work, not newly independently annotated.',
            'Generic-control missing-parameter family 3 is force-terminated later/in its trajectory; its raw anchor exists, '
            'but official decoded outputs are unavailable for the anchor parser cross-check.',
            'Function-name sequence agreement does not verify all parsed argument values; the score is attempt-based, not successful execution.'])
    (output/'published_diagnostic.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(summaries,indent=2))

if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--archive',required=True)
    p.add_argument('--cache',default='/tmp/p06_published_scorer')
    p.add_argument('--output',default='published_diagnostic_results')
    a=p.parse_args()
    run(a.archive,a.cache,a.output)
