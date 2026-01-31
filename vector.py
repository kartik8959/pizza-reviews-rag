import pandas as pd
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os

DB_DIR = "./chroma_db"
COLLECTION_NAME = "pizza_reviews"


def load_reviews(csv_path="realstic_reviews.csv"):
    """Load reviews from CSV and return LangChain Documents."""
    df = pd.read_csv(csv_path)

    documents = []
    for i, row in df.iterrows():
        text = f"{row.get('Title', '')}\n\n{row.get('Review', '')}"
        doc = Document(
            page_content=text.strip(),
            metadata={
                "rating": row.get("Rating", ""),
                "date": row.get("Date", "")
            }
        )
        documents.append(doc)

    return documents


def get_vector_store():
    """Create or load the Chroma vector store."""
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")

    if os.path.exists(DB_DIR):
        return Chroma(
            collection_name=COLLECTION_NAME,
            embedding_function=embeddings,
            persist_directory=DB_DIR
        )

    documents = load_reviews()
    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=DB_DIR
    )
    vector_store.persist()
    return vector_store


# Initialize once
vector_store = get_vector_store()


def search_reviews(query, k=5):
    """Return top-k relevant review documents."""
    return vector_store.similarity_search(query, k=k)
