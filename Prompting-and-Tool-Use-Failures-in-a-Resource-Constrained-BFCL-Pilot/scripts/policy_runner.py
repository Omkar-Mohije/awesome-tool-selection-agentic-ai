"""Development-only prompting policies; official scoring and tools are unchanged."""
import copy
import os
import runpy

COMMON = ('Use the available tools and the conversation history to satisfy the user request. '
          'A tool introduced by a later message is available from that message onward. ')
POLICIES = {
    'vanilla': '',
    'generic_control': COMMON + (
        'Work carefully through the task, review relevant details and check your progress. '
        'Use concise explanations where helpful. Keep the requested outcome in mind '
        'throughout the conversation and review whether the task is complete before reporting success.'),
    'schema_evidence': COMMON + (
        'Before acting, check the requested operation, the documented tool capabilities, '
        'argument requirements and known conversation state. Do not substitute an operation '
        'with different effects. Ask for clarification when information essential to the '
        'requested outcome is unresolved; optional defaults alone do not establish intent. '
        'If no available tool supports the operation, explain the limitation. '
        'Claim completion only when supported by executed tool results.')
}

def make_formatter(original, policy):
    instruction = POLICIES[policy]
    def format_prompt(self, messages, functions):
        if not instruction:
            return original(self, messages, functions)
        updated = copy.deepcopy(messages)
        if updated and updated[0].get('role') == 'system':
            updated[0]['content'] = instruction + '\n\n' + updated[0]['content']
        else:
            updated.insert(0, {'role': 'system', 'content': instruction})
        return original(self, updated, functions)
    return format_prompt

def make_context_guard(original):
    def query(self, inference_data):
        limit=int(os.environ['P06_CONTEXT_CAP'])
        self.max_context_length=min(self.max_context_length,limit)
        prompt=self._format_prompt(inference_data['message'],inference_data['function'])
        count=len(self.tokenizer.tokenize(prompt))
        # Preserve the official 4096-token output allowance. No history truncation.
        if count+4096+2>limit:
            raise RuntimeError(f'CONTEXT_BUDGET_EXHAUSTED: input={count}, answer_budget=4096, cap={limit}; no truncation or reduced budget applied')
        return original(self,inference_data)
    return query

def main():
    # Pin handler-side config/tokenizer to the same revision as the model server.
    from transformers import AutoConfig, AutoTokenizer
    import functools
    def pinned(original):
        @functools.wraps(original)
        def load(name, *args, **kwargs):
            if name == 'Qwen/Qwen3-4B-Instruct-2507':
                kwargs['revision'] = os.environ['ATR_MODEL_REVISION']
            return original(name, *args, **kwargs)
        return load
    AutoConfig.from_pretrained = pinned(AutoConfig.from_pretrained)
    AutoTokenizer.from_pretrained = pinned(AutoTokenizer.from_pretrained)
    from bfcl_eval.model_handler.local_inference.qwen_fc import QwenFCHandler
    from bfcl_eval.model_handler.local_inference.base_oss_handler import OSSHandler
    OSSHandler._query_prompting=make_context_guard(OSSHandler._query_prompting)
    policy = os.environ['P06_POLICY']
    QwenFCHandler._format_prompt = make_formatter(QwenFCHandler._format_prompt, policy)
    runpy.run_module('bfcl_eval', run_name='__main__')

if __name__ == '__main__':
    main()
