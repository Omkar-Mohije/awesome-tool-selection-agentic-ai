"""CPU-only synthetic check of pinned evaluation dispatch, using an identity decoder."""
import ast
import copy
import hashlib
import json
import sys
import uuid
from pathlib import Path

def run(source_root, runner_source, output):
    here = Path(__file__).resolve().parent
    lock = json.loads((here/'diagnostic_review/source_lock.json').read_text())
    runner_source = Path(runner_source)
    assert hashlib.sha256(runner_source.read_bytes()).hexdigest() == lock['eval_runner_sha256']
    source_root = Path(source_root).resolve()
    bfcl_lock = json.loads((here/'reference_control/source_lock.json').read_text())
    for relative, expected in bfcl_lock['source_sha256'].items():
        assert hashlib.sha256((source_root/relative).read_bytes()).hexdigest() == expected
    sys.path.insert(0, str(source_root))
    from bfcl_eval.eval_checker.multi_turn_eval.multi_turn_checker import multi_turn_checker, multi_turn_irrelevance_checker
    from bfcl_eval.eval_checker.multi_turn_eval.multi_turn_utils import is_empty_execute_response
    # Extract the original function without importing unrelated model dependencies.
    tree = ast.parse(runner_source.read_text())
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef)
                and n.name == '_evaluate_single_multi_turn_entry')
    namespace = dict(BaseHandler=object, multi_turn_checker=multi_turn_checker,
                     is_empty_execute_response=is_empty_execute_response)
    exec(compile(ast.Module(body=[node], type_ignores=[]), str(runner_source), 'exec'), namespace)
    evaluate = namespace[node.name]
    class IdentityDecoder:
        def decode_execute(self, step, **kwargs):
            assert isinstance(step, list) and all(isinstance(s, str) for s in step)
            return step
    def load(path):
        return {r['id']:r for line in path.read_text().splitlines() if line.strip()
                for r in [json.loads(line)]}
    rows = []
    prefix = 'p06_dispatch_' + uuid.uuid4().hex
    for category in ('base', 'miss_func', 'miss_param'):
        path = source_root/'bfcl_eval/data'/f'BFCL_v4_multi_turn_{category}.json'
        entries, answers = load(path), load(path.parent/'possible_answer'/path.name)
        for family in (2,3):
            key = f'multi_turn_{category}_{family}'
            entry, gold = entries[key], answers[key]['ground_truth']
            raw = [[list(calls)] for calls in gold]
            baseline = evaluate(IdentityDecoder(), key, raw, gold, copy.deepcopy(entry),
                                prefix+'_reference', 'multi_turn_'+category)
            assert baseline['valid']
            slots = [i for i, calls in enumerate(gold) if not calls]
            row = dict(case_id=key, reference_dispatch_valid=True, corruption=None)
            if slots:
                corrupted = copy.deepcopy(raw)
                corrupted[slots[0]] = [['pwd()']]
                wrapper = evaluate(IdentityDecoder(), key, corrupted, gold, copy.deepcopy(entry),
                                   prefix+'_extra_read', 'multi_turn_'+category)
                direct = multi_turn_irrelevance_checker(corrupted, gold)
                assert wrapper['valid'] and not direct['valid']
                row['corruption'] = dict(turn=slots[0], injected_call='pwd()',
                    official_dispatch_valid=wrapper['valid'], direct_irrelevance_valid=direct['valid'])
            rows.append(row)
    result = dict(control='synthetic_dispatch_identity_decoder_not_model_inference',
        upstream_commit=bfcl_lock['upstream_commit'], eval_runner_sha256=lock['eval_runner_sha256'],
        reference_dispatch_passes=6, extra_read_controls_accepted_by_dispatch=4,
        extra_read_controls_rejected_by_standalone_irrelevance_checker=4, cases=rows,
        limits=['Uses the unmodified original evaluation function extracted by AST, real execution checker, '
                'and deliberately supplied decoded calls through an identity decoder.',
                'Does not test production model decoding, full CLI invocation, or user clarification quality.'])
    Path(output).write_text(json.dumps(result,indent=2)+'\n')
    print('6 reference dispatch passes; 4 injected-read controls accepted by dispatch and rejected by standalone irrelevance checker')

if __name__ == '__main__':
    import argparse
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-root',required=True)
    p.add_argument('--runner-source',required=True)
    p.add_argument('--output',required=True)
    a=p.parse_args()
    run(a.source_root,a.runner_source,a.output)
