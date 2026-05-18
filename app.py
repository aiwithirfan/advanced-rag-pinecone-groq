import streamlit as st

from loader import load_pdf
from chunker import chunk_text
from embeddings import get_embeddings
from pinecone_db import upload_to_pinecone
from retriever import retrieve
from generator import generate_answer

st.title("Advanced RAG System (Pinecone + Groq)")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

chunk_size = st.slider("Chunk Size", 200, 1000, 500)
top_k = st.slider("Top-K Retrieval", 1, 10, 3)

namespace = st.text_input("Namespace", "pdf1")

if uploaded_file:

    pages = load_pdf(uploaded_file)
    chunks = chunk_text(pages, chunk_size=chunk_size)

    vectors = get_embeddings(chunks)
    upload_to_pinecone(vectors, chunks, namespace)

    st.success("PDF processed successfully!")

    query = st.text_input("Ask a question")

    if query:

        results = retrieve(query, top_k=top_k, namespace=namespace)
        answer = generate_answer(query, results)

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Sources")

        for r in results:
            st.write("Page:", r["metadata"]["page"])
            st.write(r["metadata"]["text"])
            st.write("Score:", r["score"])
            st.write("---")
