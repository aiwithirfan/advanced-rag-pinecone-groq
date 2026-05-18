import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

load_dotenv()

pc = Pinecone(api_key=os.getenv("---"))

index_name = "rag-project"

if index_name not in [i.name for i in pc.list_indexes()]:
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(index_name)


def upload_to_pinecone(vectors, chunks, namespace="pdf1"):
    data = []

    for i, (vec, chunk) in enumerate(zip(vectors, chunks)):
        data.append((
            chunk["chunk_id"],
            vec,
            {
                "text": chunk["text"],
                "page": chunk["page"]
            }
        ))

    index.upsert(vectors=data, namespace=namespace)
