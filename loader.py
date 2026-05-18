from pypdf import PdfReader

def load_pdf(file):
    reader = PdfReader(file)

    pages_text = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            pages_text.append({
                "page": i + 1,
                "text": text
            })

    return pages_text
