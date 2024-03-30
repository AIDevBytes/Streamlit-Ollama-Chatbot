class Config:
    OLLAMA_MODELS = ('llama2:7b', 'llama2:13b', 'mistral', 'llama2-uncensored:latest')

    SYSTEM_PROMPT = rf"""You are a helpful chatbot that has access to the following 
                    open-source models {OLLAMA_MODELS}.
                    You can can answer questions for users on any topic."""
    