import ollama
from config import Config

system_prompt = Config.SYSTEM_PROMPT

def chat(user_prompt, model):
    ...

# handles stream response back from LLM
def stream_parser(stream):
    ...