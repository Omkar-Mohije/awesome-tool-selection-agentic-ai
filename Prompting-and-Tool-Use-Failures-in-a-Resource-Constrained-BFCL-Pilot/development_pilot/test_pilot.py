"""Offline checks only: python test_pilot.py. No GPU/model results are generated."""
import ast, contextlib, io, json, os, pathlib, signal, subprocess, sys, tempfile, zipfile
from pathlib import Path
from unittest.mock import Mock, patch
n=json.loads(Path(__file__).with_name('P06_BFCL_Development_Pilot_Colab.ipynb').read_text())
passed=[]
for i,c in enumerate(n['cells']):
 if c['cell_type']=='code':
  tree=ast.parse(''.join(c['source']))
  compile(tree,f'cell_{i}','exec')
  for node in ast.walk(tree):
   if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id in ('selection_check','tokenizer_check') for t in node.targets):
    compile(ast.literal_eval(node.value),'child_preflight','exec')
passed.append('all notebook and child-preflight Python syntax')
s=''.join(n['cells'][2]['source'])
tree=ast.parse(s)
for node in ast.walk(tree):
 if isinstance(node,ast.Call) and isinstance(node.func,ast.Attribute) and isinstance(node.func.value,ast.Name) and node.func.value.id=='constraints' and node.func.attr=='write_text':
  constraint=ast.literal_eval(node.args[0])
  assert constraint=='transformers==4.51.3\n'
  with tempfile.TemporaryDirectory() as td:
   p=Path(td)/'constraints.txt';p.write_text(constraint)
   from pip._internal.req.req_file import parse_requirements
   from pip._internal.network.session import PipSession
   assert [r.requirement for r in parse_requirements(str(p),session=PipSession(),constraint=True)]==['transformers==4.51.3']
  break
else: raise AssertionError('Constraint not found')
passed.append('actual pip constraint-file parser accepts exact version pin')
funcs=[node for node in tree.body if isinstance(node,ast.FunctionDef)]
with tempfile.TemporaryDirectory() as td, contextlib.redirect_stdout(io.StringIO()):
 r=Path(td); (r/'logs').mkdir(); (r/'result').mkdir()
 (r/'result'/'current.json').write_text('{"id":"current"}\n')
 scope=dict(Path=Path,subprocess=subprocess,os=os,signal=signal,json=json,run_root=r,
            log_dir=r/'logs',run_id='test',commit='fixture',model='fixture',config={},policies=('vanilla','generic_control','schema_evidence'),
            run_status={},shutil=__import__('shutil'),hashlib=__import__('hashlib'),datetime=__import__('datetime'))
 exec(compile(ast.Module(body=funcs,type_ignores=[]),'helpers','exec'),scope)
 scope['run_logged']([sys.executable,'-c','print("ok")'],'success')
 assert (r/'logs'/'success.log').read_text().strip()=='ok'
 try: scope['run_logged']([sys.executable,'-c','import sys; print("failed");sys.exit(7)'],'failure')
 except subprocess.CalledProcessError as exc: assert exc.returncode==7
 else: raise AssertionError('failure was swallowed')
 assert scope['run_status']['failure'].startswith('failed:')
 try: scope['run_logged']([sys.executable,'-c','import time;time.sleep(3)'],'timeout',timeout=0.05)
 except TimeoutError: pass
 else: raise AssertionError('timeout was swallowed')
 archive=scope['export_outputs']()
 with zipfile.ZipFile(archive) as z:
  manifest=json.loads(z.read('manifest.json'))
  assert manifest['status']['timeout'].startswith('failed:')
  assert 'result/current.json' in z.namelist()
  for name,digest in manifest['files'].items():
   assert scope['hashlib'].sha256(z.read(name)).hexdigest()==digest
passed.extend(['real subprocess success and nonzero-exit logging','real subprocess timeout cleanup','failure ZIP, manifest status and byte hashes'])

code=''.join(n['cells'][4]['source'])
class Response:
 def __enter__(self):return self
 def __exit__(self,*args):pass
 def read(self):return b'{"data":[{"id":"Qwen/Qwen3-4B-Instruct-2507"}]}'
for mode in ('ready','server_failure','generation_failure','recorded_error','missing_result'):
 with tempfile.TemporaryDirectory() as td, contextlib.redirect_stdout(io.StringIO()), patch.dict(os.environ,{},clear=False):
  r=Path(td); (r/'logs').mkdir()
  server=Mock(pid=987654321)
  server.poll.return_value=1 if mode=='server_failure' else None
  server.returncode=1 if mode=='server_failure' else 0
  cfg={c:[c+'_2',c+'_3'] for c in ('multi_turn_base','multi_turn_miss_func','multi_turn_miss_param')}
  calls=[]
  def fake_run(cmd,*args,**kwargs):
   if cmd[0]=='nvidia-smi': return
   calls.append(cmd)
   if mode=='generation_failure':raise subprocess.CalledProcessError(1,cmd)
   result_root=Path(kwargs['env']['BFCL_PROJECT_ROOT'])/'result'/'Qwen_Qwen3-4B-Instruct-2507-FC'; result_root.mkdir(parents=True)
   records=[dict(id=i,result=[[]]) for ids in cfg.values() for i in ids]
   if mode=='recorded_error':records[0].update(result='Error during inference: context overflow',traceback='fixture')
   if mode=='missing_result':records=records[:-1]
   (result_root/'BFCL_v4_fixture_result.json').write_text('\n'.join(map(json.dumps,records))+'\n')
  exports=[]
  scope=dict(Path=Path,json=json,subprocess=subprocess,os=os,work=r,venv=r,bfcl_python=r/'python',bfcl_cli=r/'bfcl',
             policies=('vanilla','generic_control','schema_evidence'),runner_path=r/'runner.py',run_root=r,log_dir=r/'logs',run_logged=fake_run,config=cfg,server_max_len=12288,
             host_resources=lambda:{'fixture':True},run_status={'selection':'passed'},save_status=lambda:None,export_outputs=lambda:exports.append(1))
  with patch('subprocess.check_output',return_value='[7,5]'),patch('subprocess.Popen',return_value=server) as popen,patch('urllib.request.urlopen',return_value=Response()),patch('os.killpg') as killpg:
   try:
    exec(compile(code,'generation_cell','exec'),scope)
    assert mode=='ready'
   except (RuntimeError,subprocess.CalledProcessError):assert mode!='ready'
   assert killpg.call_count==2
   cmd=popen.call_args.args[0]
   assert cmd[cmd.index('--dtype')+1]=='half'
   assert cmd[cmd.index('--max-model-len')+1]=='12288'
   assert cmd[cmd.index('--swap-space')+1]=='0'
   assert cmd[cmd.index('--cpu-offload-gb')+1]=='0'
   assert '--enable-chunked-prefill' in cmd
   assert cmd[cmd.index('--max-num-batched-tokens')+1]=='2048'
   if mode=='ready':
    assert scope['run_status']['generation']=='passed'
    assert len(calls)==3
    assert '--skip-server-setup' in calls[0] and '--allow-overwrite' in calls[0]
    assert scope['run_env']['BFCL_PROJECT_ROOT']==str(r)
   else:
    assert scope['run_status']['generation'].startswith('failed')
    assert exports
 passed.append('generation lifecycle: '+mode)
print('PASS ('+str(len(passed))+' groups):')
for item in passed:print('-',item)
