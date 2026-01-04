import glob
from sentence_transformers import SentenceTransformer
from loading_files import load_documents, chunk_text, all_chunks
model = SentenceTransformer('all-MiniLM-L6-v2')
chunk_embeddings = model.encode(all_chunks, convert_to_tensor=True)

print(f"Generated embeddings for {len(all_chunks)} chunks.")
print(f"Embeddings shape: {chunk_embeddings.shape}")