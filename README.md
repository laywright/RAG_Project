---

# 🧠 RAG Legal Assistant

### Retrieval-Augmented Generation with Hybrid Search & Gemini

A **production-ready Retrieval-Augmented Generation (RAG) system** that answers legal questions by combining **semantic search**, **keyword-based retrieval**, and **large language models (LLMs)**.

This project demonstrates a **modern, industry-grade RAG pipeline** using **Sentence Transformers**, **TF-IDF**, and **Google Gemini** to generate accurate, context-aware answers grounded in private legal documents.

---

## 🏗️ System Architecture

```text
                ┌───────────────────┐
                │   Legal Documents │
                └─────────┬─────────┘
                          │
                ┌─────────▼─────────┐
                │  Chunking Engine  │
                └─────────┬─────────┘
                          │
        ┌─────────────────┴─────────────────┐
        │                                   │
┌───────▼────────┐                ┌─────────▼─────────┐
│ Semantic Search │                │ Keyword Search    │
│ (Embeddings)   │                │ (TF-IDF)          │
└───────┬────────┘                └─────────┬─────────┘
        │                                   │
        └───────────────┬───────────────────┘
                        ▼
               ┌─────────────────┐
               │ Hybrid Scoring  │
               └────────┬────────┘
                        ▼
               ┌─────────────────┐
               │  Gemini LLM     │
               └────────┬────────┘
                        ▼
               ┌─────────────────┐
               │ Final Answer    │
               └─────────────────┘
```

---

## 🧪 Technologies Used

| Component      | Technology                                |
| -------------- | ----------------------------------------- |
| Language       | Python 3.10+                              |
| Embeddings     | SentenceTransformers (`all-MiniLM-L6-v2`) |
| Keyword Search | TF-IDF (scikit-learn)                     |
| Similarity     | Cosine Similarity                         |
| LLM            | Google Gemini (`gemini-flash-lite`)       |
| RAG Pattern    | Hybrid Retrieval                          |
| Environment    | Windows / Linux / macOS                   |

---

## 📁 Project Structure

```text
RAG/
│
├── documents/                # Legal documents (.txt)
│
├── loading_files.py          # Document loading & chunking
├── hybrid_function.py        # Hybrid semantic + keyword search
├── prompt.py                 # Gemini prompt & answer generation
├── main.py                   # Entry point
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env                      #
```


## 👨‍💻 Author

**Muiruri Alex**
Mechatronics Engineer | Machine Learning Engineer

* GitHub: [https://github.com/laywright](https://github.com/laywright)
* LinkedIn: [https://www.linkedin.com/in/alex-muiruri-410457215](https://www.linkedin.com/in/alex-muiruri-410457215)

---

