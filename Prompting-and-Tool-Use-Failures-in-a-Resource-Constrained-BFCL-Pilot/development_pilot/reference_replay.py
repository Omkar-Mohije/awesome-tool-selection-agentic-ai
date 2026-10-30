"""CPU-only synthetic control of pinned BFCL execution checkers; no model inference."""
import argparse
import copy
import hashlib
import json
import platform
import sys
import time
import uuid
from pathlib import Path

PIN = '6ea57973c7a6097fd7c5915698c54c17c5b1b6c8'
CATEGORIES = ('base', 'miss_func', 'miss_param')
SOURCE_FILES = [
    'bfcl_eval/constants/executable_backend_config.py',
    'bfcl_eval/eval_checker/multi_turn_eval/multi_turn_checker.py',
    'bfcl_eval/eval_checker/multi_turn_eval/multi_turn_utils.py',
    *['bfcl_eval/eval_checker/multi_turn_eval/func_source_code/' + f
      for f in ('gorilla_file_system.py', 'ticket_api.py', 'long_context.py')],
    *[f'bfcl_eval/data/{prefix}BFCL_v4_multi_turn_{c}.json'
      for c in CATEGORIES for prefix in ('', 'possible_answer/')],
]

def load_jsonl(path):
    return {x['id']: x for line in path.read_text().splitlines()
            if line.strip() for x in [json.loads(line)]}

def run(source_root, output):
    source_root = Path(source_root).resolve()
    lock = json.loads((Path(__file__).parent / 'reference_control/source_lock.json').read_text())
    assert lock['upstream_commit'] == PIN
    assert set(lock['source_sha256']) == set(SOURCE_FILES)
    for relative, expected in lock['source_sha256'].items():
        assert hashlib.sha256((source_root/relative).read_bytes()).hexdigest() == expected, relative
    sys.path.insert(0, str(source_root))
    from bfcl_eval.eval_checker.multi_turn_eval.multi_turn_checker import (
        multi_turn_checker, multi_turn_irrelevance_checker)
    from bfcl_eval.eval_checker.multi_turn_eval.multi_turn_utils import execute_multi_turn_func_call
    # Reject accidentally imported modules from another installation.
    for name, module in list(sys.modules.items()):
        if name.startswith('bfcl_eval') and getattr(module, '__file__', None):
            assert Path(module.__file__).resolve().is_relative_to(source_root), name
    started = time.monotonic()
    # BFCL interpolates model_name into a Python identifier before eval().
    nonce = 'p06_reference_' + uuid.uuid4().hex
    rows = []
    for category in CATEGORIES:
        data = source_root / 'bfcl_eval/data'
        entries = load_jsonl(data / f'BFCL_v4_multi_turn_{category}.json')
        answers = load_jsonl(data / f'possible_answer/BFCL_v4_multi_turn_{category}.json')
        for family in (2, 3):
            case_id = f'multi_turn_{category}_{family}'
            entry = entries[case_id]
            gold = answers[case_id]['ground_truth']
            assert len(gold) == len(entry['question'])
            assert any(gold)
            evidence = []
            for calls in gold:
                responses, _ = execute_multi_turn_func_call(
                    calls, copy.deepcopy(entry['initial_config']), entry['involved_classes'],
                    nonce + '_audit', case_id, is_evaL_run=True)
                evidence.append(responses)
            execution_errors = [r for turn in evidence for r in turn
                                if r.startswith('Error during execution:')]
            checks = {}
            for layout in ('one_step_per_turn', 'one_step_per_call'):
                decoded = [[list(calls)] if layout == 'one_step_per_turn'
                           else [[call] for call in calls] for calls in gold]
                checks[layout] = {
                    'execution': multi_turn_checker(decoded, gold, copy.deepcopy(entry),
                        case_id.rsplit('_', 1)[0], nonce + '_' + layout),
                    'irrelevance': multi_turn_irrelevance_checker(decoded, gold),
                }
            empty = [[] for _ in gold]
            negative = multi_turn_checker(empty, gold, copy.deepcopy(entry),
                case_id.rsplit('_', 1)[0], nonce + '_empty')
            irrelevant_negative = None
            if any(not turn for turn in gold):
                corrupted = [[list(calls)] for calls in gold]
                slot = next(i for i, calls in enumerate(gold) if not calls)
                corrupted[slot] = [[next(call for calls in gold for call in calls)]]
                irrelevant_negative = multi_turn_irrelevance_checker(corrupted, gold)
            passed = (not execution_errors and
                all(v['execution']['valid'] and v['irrelevance']['valid'] for v in checks.values())
                and not negative['valid'] and
                (irrelevant_negative is None or not irrelevant_negative['valid']))
            row = dict(case_id=case_id, passed=passed, turns=len(gold),
                reference_call_count=sum(map(len, gold)), reference_responses=evidence,
                reference_execution_errors=execution_errors, positive_controls=checks,
                empty_action_negative=negative, no_call_violation_negative=irrelevant_negative)
            rows.append(row)
            print(case_id, 'PASS' if passed else 'FAIL', flush=True)
    report = dict(control='synthetic_reference_replay_not_model_performance',
        upstream_commit=PIN, python=platform.python_version(),
        elapsed_seconds=time.monotonic()-started,
        source_sha256={p: hashlib.sha256((source_root/p).read_bytes()).hexdigest()
                       for p in SOURCE_FILES},
        cases=rows, passed=sum(r['passed'] for r in rows), total=len(rows),
        limits=['Direct official decoded execution/state/response and irrelevance checkers only; '
                'does not test model decoding, server, CLI dispatch, tool exposure, or clarification wording.',
                'Synthetic author reference actions are supplied deliberately; these are not model predictions.'])
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + '\n')
    assert report['passed'] == report['total'] == 6, 'Reference-control failure; inspect saved report'
    return report

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    run(args.source_root, args.output)
