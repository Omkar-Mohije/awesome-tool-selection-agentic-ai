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

def main():
    from bfcl_eval.model_handler.local_inference.qwen_fc import QwenFCHandler
    policy = os.environ['P06_POLICY']
    QwenFCHandler._format_prompt = make_formatter(QwenFCHandler._format_prompt, policy)
    runpy.run_module('bfcl_eval', run_name='__main__')

if __name__ == '__main__':
    main()
