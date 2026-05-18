def chunk_text(pages, chunk_size=500, overlap=50):
    chunks = []

    for page_data in pages:
        text = page_data["text"]
        page = page_data["page"]

        start = 0
        i = 0

        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]

            chunks.append({
                "text": chunk,
                "page": page,
                "chunk_id": f"p{page}_c{i}"
            })

            start += chunk_size - overlap
            i += 1

    return chunks
