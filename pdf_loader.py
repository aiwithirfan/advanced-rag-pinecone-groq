from pypdf import PdfReader

def load_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page_num, page in enumerate(reader.pages):
        content = page.extract_text()
        if content:
            text += f"\nPage {page_num+1}:\n{content}"

    return text
