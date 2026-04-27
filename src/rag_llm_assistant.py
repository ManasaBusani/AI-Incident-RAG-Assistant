from pathlib import Path

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

DATA_PATH = Path("data/past_incidents.txt")


def load_documents():
    lines = DATA_PATH.read_text().splitlines()
    return [Document(page_content=line) for line in lines if line.strip()]


def build_retriever(documents):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vector_store = FAISS.from_documents(documents, embeddings)
    return vector_store.as_retriever(search_kwargs={"k": 2})


def generate_llm_response(query, docs):
    context = "\n".join([doc.page_content for doc in docs])

    return f"""
Root Cause:
The issue may be related to one of the similar past incidents retrieved from the incident knowledge base.

Current Issue:
{query}

Retrieved Incident Context:
{context}

What to Check:
- Search Splunk logs using service name, timestamp, and correlation ID
- Review AppDynamics or Grafana metrics for latency, error rate, and downstream failures
- Validate downstream service health and recent deployment changes

Next Steps:
- Compare the current issue with the retrieved incidents
- Confirm the root cause using logs and telemetry
- Escalate to the owning service team if the issue is dependency-related
"""


def analyze(query):
    documents = load_documents()
    retriever = build_retriever(documents)
    similar_docs = retriever.invoke(query)
    return generate_llm_response(query, similar_docs)


if __name__ == "__main__":
    print(analyze("Payment API is slow and timing out"))
