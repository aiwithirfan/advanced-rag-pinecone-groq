from embeddings import model
from pinecone_db import index

def retrieve(query, top_k=3, namespace="pdf1"):
    query_vector = model.encode([query]).tolist()

    results = index.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True,
        namespace=namespace
    )

    return results["matches"]
