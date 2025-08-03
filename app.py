import streamlit as st
from rag import get_rag_chain

st.set_page_config(page_title="🧠 Medical Chatbot", layout="centered")
st.title("🧠 Medical Chatbot")
st.markdown("Ask a medical question based on research documents.")

query_type = st.selectbox(
    "📌 What would you like to know?",
    ["Symptoms", "Treatment", "Medicine", "Precautions"]
)

user_query = st.text_input("💬 Enter disease or condition:")
st.markdown("Note: Ask about asthma, anemia, cancer, Diabetes, Diarrehea, Fever, Flu, Headache, Heart Attack, Vomiting.")

if st.button("🔍 Get Answer"):
    if not user_query:
        st.warning("Please enter a disease or condition.")
    else:
        try:
            rag_chain = get_rag_chain()
            query = f"{query_type} of {user_query}"

            # Properly invoke chain
            result = rag_chain.invoke({
                "query": query,
                "query_type": query_type,
                "disease": user_query
            })

            st.markdown("### 💬 Answer:")
            st.write(result.strip())

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
