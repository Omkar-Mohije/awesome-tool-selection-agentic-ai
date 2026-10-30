"""Extract first reported failures; do not infer semantic causes from category names."""
import argparse
import csv
import hashlib
import json
import re
import zipfile
from pathlib import Path

ARCHIVE_SHA256 = '4b7178e4208094c16f04cdaf83235f2986a5923f1b910496d92d545c2b1eba40'

def audit(archive, source_root, output):
    archive, source_root, output = map(Path, (archive, source_root, output))
    assert hashlib.sha256(archive.read_bytes()).hexdigest() == ARCHIVE_SHA256
    gold = {}
    for path in (source_root/'bfcl_eval/data/possible_answer').glob('*.json'):
        for line in path.read_text().splitlines():
            if line.strip():
                record = json.loads(line)
                gold[record['id']] = record['ground_truth']
    rows = []
    with zipfile.ZipFile(archive) as z:
        for name in sorted(z.namelist()):
            if not (name.startswith('conditions/') and '/score/' in name and name.endswith('_score.json')):
                continue
            records = [json.loads(line) for line in z.read(name).decode().splitlines() if line.strip()]
            for record in records[1:]:
                error = record['error']
                details = error.get('details', {})
                execution = error.get('execution_result', details.get('execution_result', []))
                # State failures save all turns through the failing one; response failures name the turn.
                match = re.search(r'for turn (\d+)', str(error.get('error_message', '')))
                turn = len(execution)-1 if execution else int(match[1]) if match else None
                empty_turns = [i for i, calls in enumerate(gold[record['id']]) if not calls]
                decoded_turns = record.get('model_result_decoded')
                no_call_checks = ({str(i): (decoded_turns[i] == [] or decoded_turns[i] == [[]])
                                  for i in empty_turns}
                                 if isinstance(decoded_turns, list) and
                                 all(i < len(decoded_turns) for i in empty_turns) else None)
                responses = [r for t in execution for step in t['model'] for r in step]
                tool_errors = []
                for response in responses:
                    if response.startswith('Error during execution:'):
                        tool_errors.append(response)
                        continue
                    try:
                        decoded = json.loads(response)
                    except (ValueError, TypeError):
                        continue
                    if isinstance(decoded, dict) and 'error' in decoded:
                        tool_errors.append(decoded['error'])
                relation = ('not_applicable' if not empty_turns else 'unknown' if turn is None
                            else 'before' if turn < empty_turns[0] else 'at' if turn == empty_turns[0] else 'after')
                rows.append(dict(condition=name.split('/')[1], case_id=record['id'],
                    error_type=error['error_type'], first_reported_failure_turn_zero_based=turn,
                    reference_no_call_turns_zero_based=json.dumps(empty_turns),
                    failure_relative_to_first_no_call=relation,
                    decoded_no_call_turn_checks=json.dumps(no_call_checks),
                    tool_error_responses_in_saved_execution_prefix=len(tool_errors),
                    tool_error_messages=json.dumps(tool_errors)))
    assert len(rows) == 18 and len({(r['condition'],r['case_id']) for r in rows}) == 18
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    return rows

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', required=True)
    parser.add_argument('--source-root', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    rows = audit(args.archive, args.source_root, args.output)
    from collections import Counter
    print(json.dumps(dict(records=len(rows), timing=dict(Counter(r['failure_relative_to_first_no_call'] for r in rows)))))
