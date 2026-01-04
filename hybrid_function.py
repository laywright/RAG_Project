import numpy as np
from sentence_transformers import SentenceTransformer, util
from loading_files import load_documents, chunk_text, all_chunks
from loading_files import vectorizer, tfidf_matrix
model = SentenceTransformer('all-MiniLM-L6-v2')
chunk_embeddings = model.encode(all_chunks, convert_to_tensor=True)


def hybrid_search(query, top_k=5):
    query_embedding = model.encode(query, convert_to_tensor=True)
    semantic_scores = util.pytorch_cos_sim(query_embedding, chunk_embeddings)[0]

    keyword_vec = vectorizer.transform([query])
    keyword_scores = (tfidf_matrix * keyword_vec.T).toarray().sum(axis=1)

    final_scores = 0.7 * semantic_scores.cpu().numpy() + 0.3 * keyword_scores
    top_indices = np.argsort(final_scores)[::-1][:top_k]

    return [all_chunks[i] for i in top_indices]

print("Hybrid search function defined.")