"""Audit observed tool exposure from a saved smoke ZIP, without GPU inference."""
import argparse
import csv
import io
import json
import re
import zipfile
from pathlib import Path

def parse_tools(prompt):
    # Ignore the illustrative empty <tools></tools> pair in the instruction text.
    blocks=re.findall(r'<tools>(.*?)</tools>',prompt,flags=re.S)
    block=max(blocks,key=len)
    decoder=json.JSONDecoder()
    tools=[]
    while block.strip():
        block=block.lstrip()
        if block.startswith('\\n'):
            block=block[2:]
            continue
        obj,end=decoder.raw_decode(block)
        tools.append(obj)
        block=block[end:]
    return tools

def audit(archive):
    rows=[]
    with zipfile.ZipFile(archive) as z:
        for name in sorted(z.namelist()):
            if not name.endswith('_result.json'): continue
            case=json.loads(z.read(name))
            turn=0
            for entry in case['inference_log']:
                if not isinstance(entry,dict) or 'begin_of_turn_query' not in entry: continue
                steps=entry.get('step_0',[])
                inp=next(s for s in steps if s.get('role')=='inference_input')
                tools=parse_tools(inp['content']['formatted_prompt'])
                names=[t['name'] for t in tools]
                tail=next((t for t in tools if t['name']=='tail'),{})
                query=entry['begin_of_turn_query']
                rows.append({'case_id':case['id'],'turn_index':turn,'tool_block_count':len(tools),
                    'cp_in_tool_block':'cp' in names,'mv_in_tool_block':'mv' in names,
                    'mv_introduced_this_turn':any("'name': 'mv'" in x.get('content','') for x in query),
                    'tail_lines_required':'lines' in tail.get('parameters',{}).get('required',[]),
                    'tail_lines_default':tail.get('parameters',{}).get('properties',{}).get('lines',{}).get('default'),
                    'current_query':json.dumps(query,ensure_ascii=False)})
                turn+=1
    return rows

def main():
    p=argparse.ArgumentParser();p.add_argument('archive');p.add_argument('output');a=p.parse_args()
    rows=audit(a.archive)
    with Path(a.output).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    print(f'Audited {len(rows)} observed turns; no new model execution.')

if __name__=='__main__':main()
