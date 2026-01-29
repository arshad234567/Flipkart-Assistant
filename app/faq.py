import pandas as pd
from pathlib import Path
import chromadb
from chromadb.utils import embedding_functions
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

faqs_path = Path(__file__).parent / "resources/faq_data.csv"

chroma_client = chromadb.Client()
collection_name_faq = "faqs"
groq_client = Groq()

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
        n_results=2

        )
    return result

def generate_answer(query, context):
    prompt = f''' Given the question and context below, generate the answer based on the context only.
        If you don't find the answer inside the context than say "I don't know".
        Do not make things up.

        QUESTION: {query}
        CONTEXT: {context}
        '''
        #calling llm
    chat_completion = groq_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
        model=os.environ['GROQ_MODEL'],
    )

    return chat_completion.choices[0].message.content

def faq_chain(query):
        result = get_relevant_qa(query)
        context = " ".join(
            r["answer"] for r in result["metadatas"][0]
        )
        answer = generate_answer(query,context)
        return answer

if __name__ == "__main__":
    ingest_faq_data(faqs_path)
    query = "Do you take cash as a payment option?"
    # result = get_relevant_qa(query)
    # print(result)
    answer = faq_chain(query)
    print(answer)
