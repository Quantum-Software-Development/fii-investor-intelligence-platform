# ⚡ FAISS — Semantic Similarity Search Engine

## 1. 📌 Overview

**FAISS (Facebook AI Similarity Search)** is a high-performance library designed for efficient similarity search over dense vector representations.

Within this project, FAISS acts as the **semantic retrieval engine**, enabling the system to move beyond keyword matching and operate over **meaning-based relationships**.

---

## 2. 🎯 Purpose in the Architecture

FAISS is responsible for:

* Indexing vector embeddings generated from financial text
* Performing fast nearest-neighbor search
* Retrieving semantically similar documents

> It enables the system to find **relevant information even when exact terms are not present**.

---

## 3. 🧠 Conceptual Role

FAISS operates in a **high-dimensional vector space**, where:

* Each document → becomes a vector
* Distance between vectors → represents semantic similarity

> The closer two vectors are, the more similar their meanings.

---

## 4. ⚙️ How It Works

### Step 1 — Text → Embeddings

Financial text is transformed into vectors using models such as:

* SentenceTransformer
* BERT-based encoders

---

### Step 2 — Indexing

FAISS stores vectors in optimized data structures:

* Flat indexes (exact search)
* IVF (Inverted File Index)
* HNSW (Hierarchical graphs)

---

### Step 3 — Similarity Search

Given a query vector, FAISS:

1. Computes distance (e.g., cosine similarity or L2)
2. Retrieves nearest neighbors
3. Returns the most relevant documents

---

## 5. 🔍 Types of Similarity

FAISS supports multiple similarity metrics:

| Metric            | Description            |
| ----------------- | ---------------------- |
| L2 Distance       | Euclidean distance     |
| Inner Product     | Dot product similarity |
| Cosine Similarity | Angular similarity     |

---

## 6. 🚀 Why FAISS is Critical in This Project

Traditional methods (TF-IDF, BM25):

* Depend on exact word matching
* Fail with paraphrases or implicit meaning

FAISS enables:

* Semantic understanding
* Context-aware retrieval
* Discovery of implicit signals

> This is essential for analyzing **investor sentiment and market narratives**.

---

## 7. 🔗 Integration with Other Components

FAISS does not work in isolation — it complements other techniques:

| Component  | Role               | Relation to FAISS         |
| ---------- | ------------------ | ------------------------- |
| MapReduce  | Data preparation   | Feeds clean text          |
| TF-IDF     | Term relevance     | Supports lexical baseline |
| BM25       | Keyword precision  | Handles explicit mentions |
| Embeddings | Vector generation  | Input for FAISS           |
| RAG        | Insight generation | Uses FAISS results        |

---

## 8. 🧠 Application to FIIs

In the context of Brazilian FIIs, FAISS enables:

* Detection of **indirect discussions** about funds
* Identification of **market sentiment trends**
* Retrieval of **contextually similar financial narratives**

Example:

Query:

```text
"Logistics funds under pressure"
```

FAISS can retrieve:

* Discussions about HGLG11 without mentioning it explicitly
* News about warehouse vacancy rates
* Sentiment shifts in logistics FIIs

---

## 9. 🔁 FAISS within RAG

FAISS is a core component of the **Retrieval-Augmented Generation (RAG)** pipeline:

```text
User Query → Embedding → FAISS Search → Retrieved Context → LLM → Answer
```

---

## 10. 🧩 Strengths

* High scalability (millions of vectors)
* Extremely fast search
* Works with high-dimensional data
* Enables semantic retrieval

---

## 11. ⚠️ Limitations

* Requires high-quality embeddings
* Approximate search may reduce precision
* No inherent interpretability (black-box vectors)

---

## 12. 🔮 Conceptual Insight

FAISS transforms information retrieval from:

* Keyword matching → **Meaning navigation**
* Static search → **Semantic exploration**

> It allows the system to operate in a **space of meanings rather than words**.

---

## 13. 🔗 Relation to Conceptual Foundations

For deeper theoretical context:

📄 `docs/Conceptual Foundations.md`

---

## 🧠 Final Insight

FAISS is not just a search tool — it is the **core enabler of semantic intelligence** in the system.

When combined with:

* Embeddings → representation
* BM25 → precision
* RAG → reasoning

> FAISS becomes the **bridge between language and meaning** in financial intelligence systems.

