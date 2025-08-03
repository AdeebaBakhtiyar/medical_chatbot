from langchain_community.llms import Ollama

def load_llm(model_name="tinyllama"):
    return Ollama(model=model_name)
