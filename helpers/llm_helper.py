"""
Author: Hello (World)
llm_helper.py (c) 2024
Desc: description
Created:  2024-04-02T05:40:48.648Z
Modified: !date!
"""


import ollama
from config import Config

system_prompt = Config.SYSTEM_PROMPT

def chat(user_prompt, model):
    stream = ollama.chat(
        model=model,
        messages=[{'role': 'assistant', 'content': system_prompt},
                  {'role': 'user', 'content': f"Model being used is {model}.{user_prompt}"}],
        stream=True,
    )

    return stream

# handles stream response back from LLM
def stream_parser(stream):
    for chunk in stream:
        yield chunk['message']['content']