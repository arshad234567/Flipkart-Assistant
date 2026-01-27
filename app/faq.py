import pandas as pd
from pathlib import Path
import chromadb
from chromadb.utils import embedding_functions
from groq import Groq

faqs_path = Path(__file__).parent / "resources/faq_data.csv"

chroma_client = chromadb.Client()
collection_name_faq = "faqs"

ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def ingest_faq_data(path):
    collection = chroma_client.get_or_create_collection(
        name=collection_name_faq,
        embedding_function=ef
    )

    df = pd.read_csv(path)
    docs = df["question"].to_list()
    metadatas = [{"answer": ans} for ans in df["answer"].to_list()]
    ids = [f"id_{i}" for i in range(len(docs))]

    collection.add(
        documents=docs,
        metadatas=metadatas,
        ids=ids
    )

    print(f"FAQ data ingested into collection: {collection_name_faq}")

def get_relevant_qa(query):
    collection = chroma_client.get_collection(
        name=collection_name_faq,
        embedding_function=ef
    )

    result = collection.query(
        query_texts=[query],
        n_results=2,
        # include = ["embeddings", "documents", "metadatas", "distances"]
    )
    return result

if __name__ == "__main__":
    ingest_faq_data(faqs_path)

    query = "what's your policy on defective products?"
    result = get_relevant_qa(query)
    print(result)
