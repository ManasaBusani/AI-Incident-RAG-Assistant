# 🚀 AI Incident Resolution Assistant (RAG + LangChain)

This project is a simple proof-of-concept that shows how Retrieval-Augmented Generation (RAG) can be used to help with incident analysis in backend systems.

In real production environments, engineers debug issues by checking logs, monitoring metrics, and looking at past incidents. This project simulates that workflow by retrieving similar incidents and providing structured guidance on how to investigate and resolve issues.

---

## 💡 How it Works

1. Incident data is converted into embeddings using Sentence Transformers  
2. Embeddings are stored in a FAISS vector database  
3. User enters a new issue (e.g., API latency or failure)  
4. System retrieves similar past incidents using similarity search  
5. Generates structured output:
   - Root cause suggestion  
   - What to Check (logs, metrics, dependencies)  
   - Next Steps (resolution actions)  

---

## 🛠 Tech Stack

- Python  
- LangChain  
- FAISS (Vector Database)  
- Sentence Transformers (Embeddings)  
- Streamlit (UI)  

---

## 🌍 Real-World Relevance

This project is inspired by production support workflows using tools like:
- Splunk (logs)  
- AppDynamics / Grafana (monitoring)  

It demonstrates how past incident data can be reused to speed up debugging and improve incident resolution.

---

## ▶ Run Locally

```bash
pip install -r requirements.txt
py -3 -m streamlit run ui/streamlit_app.py
