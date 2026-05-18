from sentence_transformers import SentenceTransformer

model = SentenceTransformer("---")

def get_embeddings(chunks):
    texts = [c["text"] for c in chunks]
    vectors = model.encode(texts).tolist()
    return vectors
