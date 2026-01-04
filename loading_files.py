import glob
import os
from sklearn.feature_extraction.text import TfidfVectorizer

def load_documents(path=r"C:\Users\amuiruri_basi-go\Desktop\RAG\documents"):
    docs = []
    found_files = glob.glob(path + r"\*.txt")

    if not found_files:
        print(f"Error: No .txt files found in the directory: {path}")

    for file in found_files:
        with open(file, "r", encoding="utf-8") as f:
            docs.append(f.read())

    return docs
def chunk_text(text, chunk_size=500):
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

all_docs = load_documents()
all_chunks = []
for doc in all_docs:
    chunks = chunk_text(doc)
    all_chunks.extend(chunks)

print(f"Loaded {len(load_documents())} documents.")
print(f"Generated {len(all_chunks)} chunks from the documents.")


if not all_chunks:
    print("Error: No valid chunks found in the documents.")
else:
    vectorizer = TfidfVectorizer().fit(all_chunks)
    tfidf_matrix = vectorizer.transform(all_chunks)
    print("TF-IDF vectorizer created and matrix transformed.")
    print(f"TF-IDF matrix shape: {tfidf_matrix.shape}")