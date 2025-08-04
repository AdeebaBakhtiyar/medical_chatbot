import streamlit as st
from rag import load_documents, build_faiss_index, get_most_similar
from transformers import pipeline

# Load documents and build index once
docs, filenames = load_documents()
index, embeddings = build_faiss_index(docs)

# Load transformer model
gen = pipeline("text2text-generation", model="google/flan-t5-large")

st.set_page_config(page_title="🧠 Medical Chatbot", layout="centered")
st.title("🧠 Medical Chatbot")
st.markdown("Ask a medical question based on research documents.")

query_type = st.selectbox("📌 What would you like to know?", ["Symptoms", "Treatment", "Medicine", "Precautions"])
user_query = st.text_input("💬 Enter disease or condition:")

if st.button("🔍 Get Answer"):
    if not user_query:
        st.warning("Please enter a condition.")
    else:
        try:
            query = f"{query_type} of {user_query}"
            context = get_most_similar(query, docs, index, embeddings)

            full_input = f"Question: {query} \n Context: {context} \n Answer:"
            result = gen(full_input, max_length=512, do_sample=False)[0]['generated_text']

            st.markdown("### 💬 Answer:")
            st.write(result.strip())
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
