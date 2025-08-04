from langchain_community.llms import HuggingFaceHub
import os
from dotenv import load_dotenv

load_dotenv()

def load_llm():
    return HuggingFaceHub(
        repo_id="google/flan-t5-large",  # or any other valid model
        model_kwargs={"temperature": 0.5, "max_length": 512},
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
        task="text2text-generation"
    )
