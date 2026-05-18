import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("----"))

def generate_answer(query, contexts):

    if not contexts:
        return "No relevant information found in the document."

    contexts = contexts[:2]

    context_text = "\n\n".join([
        c["metadata"]["text"][:500] for c in contexts
    ])

    prompt = f"""
Answer ONLY using the context below.

If answer is not in context, say:
"The answer is not available in the provided document."

Context:
{context_text}

Question:
{query}
"""

    try:
        response = client.chat.completions.create(
            
            model="----",
            messages=[
                {"role": "system", "content": "You are a strict RAG assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"
