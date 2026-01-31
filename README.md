# 🍕 Pizza Reviews 
**A small retrieval-augmented generation (RAG) demo that answers questions about a pizza restaurant using real customer reviews.**

---

## 🚀 Features

- Convert CSV reviews into LangChain `Document`s and embed them with **Ollama embeddings**.
- Store embeddings and perform semantic search with **Chroma**.
- CLI assistant (`main.py`) that retrieves top-k reviews and asks an LLM for an answer.
- Modular code: `vector.py` (indexing + search) and `main.py` (interactive assistant).

---

## ✅ Prerequisites

- Python 3.10+
- Git (optional)
- A Python virtual environment (recommended)

Files you should see in the repo:
- `realstic_reviews.csv` — your reviews dataset
- `main.py` — interactive CLI assistant
- `vector.py` — CSV -> vector store, `search_reviews` helper
- `requirements.txt` — Python dependencies

---

## ⚙️ Quick setup

1. Create & activate a virtual environment (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If activation is blocked, run:
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
```

2. Install dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

> Tip: If you add a UI with Gradio/Streamlit, add `gradio` or `streamlit` to `requirements.txt` and run `pip install -r requirements.txt` again.

---

## 🛠️ Build the vector DB

The first time you run the application, the vector store will be created and persisted in `./chroma_db`.

Run (this happens automatically on import of `vector.py`):

```powershell
python -c "import vector; print(len(vector.search_reviews('pizza', k=1)))"
```

Or simply run the CLI which instantiates the vector store if needed:
```powershell
python main.py
```

---

## 💬 Usage — CLI Assistant

1. Run:
```powershell
python main.py
```
2. Ask questions like: `Which vegan pizza is best?` or `Do they have gluten-free crust?`
3. Type `q` to quit.

The assistant will:
- Retrieve the top-k relevant reviews (from `vector.search_reviews`),
- Build a prompt containing only those reviews, and
- Ask the Ollama LLM to answer using only that evidence.

