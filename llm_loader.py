from langchain_community.llms import HuggingFaceHub
import os

def load_llm():
    # Load Hugging Face token from environment variable
    token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    if not token:
        raise ValueError("Missing Hugging Face API token in environment.")

    return HuggingFaceHub(
        repo_id="google/flan-t5-large",
        model_kwargs={"temperature": 0.5, "max_length": 512}
    )
