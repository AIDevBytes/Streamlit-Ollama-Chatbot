import os

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    SYSTEM_PROMPT = "You are a helpful chatbot assistant that can answer questions for users."
    OLLAMA_MODELS = ('llama2:7b', 'llama2:13b', 'mistral')