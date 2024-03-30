from openai import OpenAI
from config import Config

system_prompt = Config.SYSTEM_PROMPT

def chat(user_prompt, model, max_tokens=200, temp=0.7):
    client = OpenAI()

    # create chat using OpenAI LLM
    # https://platform.openai.com/docs/api-reference/chat/create
    completion = client.chat.completions.create(
    model=model,
    messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content":  user_prompt}
        ],
        temperature=temp,
        max_tokens=max_tokens,
        stream=True
    )

    return completion

# handles stream response back from LLM
def stream_parser(stream):
    for chunk in stream:
        if chunk.choices[0].delta.content != None:
            yield chunk.choices[0].delta.content