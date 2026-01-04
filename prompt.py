from google import genai
from hybrid_function import hybrid_search

import os
from dotenv import load_dotenv
import requests
load_dotenv()  # loads .env file

api_key = os.getenv("API_KEY")
client = genai.Client(api_key=api_key)  

def generate_answer(query):
    # 1️⃣ Get top context chunks
    top_contexts = hybrid_search(query)
    context_text = "\n---\n".join(top_contexts)

    # 2️⃣ Build prompt
    prompt = f"""You are a legal assistant. Based on the following legal documents, answer the query:

Context:
{context_text}

Query:
{query}

Answer:"""

    # 3️⃣ Call Gemini model
    response = client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=prompt
    )

    # 4️⃣ Access the actual text
    return response.candidates[0].content

print("Generate answer function defined.")

