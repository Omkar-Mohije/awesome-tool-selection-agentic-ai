import ast,contextlib,hashlib,importlib.util,io,json,os,tempfile
from pathlib import Path
from unittest.mock import patch
root=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('runner',root/'p06_policy_runner.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class Tokenizer:
 def tokenize(self,p):return list(range(int(p)))
class Handler:
 max_context_length=262144
 tokenizer=Tokenizer()
 def _format_prompt(self,msgs,functions):return msgs
calls=[]
def original(self,data):calls.append(self.max_context_length);return 'called'
with patch.dict(os.environ,{'P06_CONTEXT_CAP':'24576'}):
 assert m.make_context_guard(original)(Handler(),{'message':'8302','function':[]})=='called'
 assert calls==[24576]
 try:m.make_context_guard(original)(Handler(),{'message':'23000','function':[]})
 except RuntimeError as e:assert 'CONTEXT_BUDGET_EXHAUSTED' in str(e)
 else:raise AssertionError('Oversized prompt accepted')
 assert len(calls)==1
print('PASS: full-budget calls fit 24K; oversized calls blocked without truncation.')
n=json.loads((root/'P06_BFCL_Development_Pilot_Recovery_Colab.ipynb').read_text())
s=''.join(n['cells'][3]['source']);seed=s[s.index('# Reuse only original'):]
assert "'--allow-overwrite'" not in ''.join(n['cells'][4]['source'])
assert "'pip','install'" not in ''.join(n['cells'][2]['source'])
expected_sha=ast.literal_eval(next(x.value for x in ast.parse(seed).body if isinstance(x,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='expected_runner_sha' for t in x.targets)))
# Exact archived original runner was embedded in the pre-repair notebook fetched earlier.
old_runner=(root/'fixtures/p06_policy_runner_before_context_fix.py').read_text()
assert hashlib.sha256(old_runner.encode()).hexdigest()==expected_sha
with tempfile.TemporaryDirectory() as td,contextlib.redirect_stdout(io.StringIO()):
 base=Path(td);source=base/'source';source.mkdir();new=base/'new';new.mkdir()
 (source/'p06_policy_runner.py').write_text(old_runner)
 (source/'P06_BFCL_Development_Pilot_Outputs.zip').write_bytes(b'fixture archive unchanged')
 model='Qwen/Qwen3-4B-Instruct-2507-FC'
 policies=('vanilla','generic_control','schema_evidence')
 cfg={c:[c+'_2',c+'_3'] for c in ('multi_turn_base','multi_turn_miss_func','multi_turn_miss_param')}
 ids=[x for v in cfg.values() for x in v]
 for policy in policies[:2]:
  out=source/'conditions'/policy/'result'/model.replace('/','_')/'multi_turn';out.mkdir(parents=True)
  rows=[{'id':i,'result':[[]]} for i in ids]
  if policy=='generic_control':rows[0].update(result='Error during inference: overflow',traceback='fixture')
  (out/'BFCL_v4_fixture_result.json').write_text(''.join(json.dumps(r)+'\n' for r in rows))
 scope=dict(source_run=source,run_root=new,hashlib=hashlib,json=json,config=cfg,model=model,policies=policies,server_max_len=24576,shutil=__import__('shutil'))
 exec(compile(seed,'recovery_seed','exec'),scope)
 prov=json.loads((new/'recovery_provenance.json').read_text());assert len(prov['reused'])==11
 assert len(prov['rejected_inference_errors'])==1
 assert (new/'source_attempt_outputs.zip').read_bytes()==b'fixture archive unchanged'
 saved=[json.loads(l) for p in (new/'conditions').rglob('*_result.json') for l in p.read_text().splitlines()]
 assert len(saved)==11 and all(isinstance(r['result'],list) for r in saved)
 assert len(list(source.rglob('*_result.json')))==2
print('PASS: 11 valid fixture records retained, 1 exception excluded, original files/ZIP preserved; no overwrite or reinstall.')
for nb in root.glob('*.ipynb'):
 data=json.loads(nb.read_text())
 for i,c in enumerate(data['cells']):
  if c['cell_type']=='code':compile(''.join(c['source']),f'{nb.name}:{i}','exec')
print('PASS: main and recovery notebook code cells compile.')
