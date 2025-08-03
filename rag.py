from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.schema.runnable import RunnableMap, RunnablePassthrough
from llm_loader import load_llm
import os

def load_documents(doc_folder="docs"):
    docs = []
    for filename in os.listdir(doc_folder):
        if filename.endswith(".txt"):
            path = os.path.join(doc_folder, filename)
            loader = TextLoader(path)
            docs.extend(loader.load())
    return docs

def build_vector_store(docs):
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.from_documents(docs, embedding)

def get_prompt_template():
    template = """
You are a helpful medical assistant providing information based only on medical research documents.

🔍 Task: {query_type}
🦠 Condition: {disease}

📄 Document Context:
{context}

✅ Please give a short, user-friendly, medically accurate answer.
"""
    return PromptTemplate(
        input_variables=["query_type", "disease", "context"],
        template=template
    )

def get_rag_chain():
    docs = load_documents()
    vector_store = build_vector_store(docs)
    retriever = vector_store.as_retriever(search_kwargs={"k": 1})

    llm = load_llm()
    prompt = get_prompt_template()

    chain = (
        RunnableMap({
            "context": lambda x: "\n\n".join(
                doc.page_content for doc in retriever.get_relevant_documents(x["query"])
            ),
            "query_type": lambda x: x["query_type"],
            "disease": lambda x: x["disease"]
        }) 
        | prompt 
        | llm
    )

    return chain
