# AI Incident Resolution Assistant (RAG + LangChain)

This project demonstrates an AI-powered assistant built to support incident analysis and troubleshooting using Retrieval-Augmented Generation (RAG). The system processes operational logs and retrieves relevant historical data to generate meaningful insights and suggested resolution steps.

---

## What this project does

* Analyzes incident logs and system data
* Retrieves similar past incidents using vector search
* Generates context-aware responses for troubleshooting
* Assists in faster issue identification and resolution

---

## Tech Stack

* Python
* LangChain
* FAISS (Vector Database)
* Embeddings
* Streamlit

---

## Project Structure

AI-Incident-RAG-Assistant/
├── data/ → Sample logs / incident data
├── embeddings/ → Vector store setup
├── app/ → Main application logic
├── utils/ → Helper functions
├── streamlit_app.py → UI interface
├── README.md

---

## How to run locally

1. Install dependencies:
   pip install -r requirements.txt

2. Run the application:
   streamlit run streamlit_app.py

3. Open in browser:
   http://localhost:8501

---

## How it works

1. Input query or incident description
2. Convert query into embeddings
3. Retrieve relevant historical logs from vector store
4. Pass context to LLM using LangChain
5. Generate response with suggested actions

---

## Sample Use Case

* Input: “API latency spike during peak hours”
* Output:

  * Similar past incidents
  * Possible root causes
  * Suggested debugging steps

---

## Why I built this

I built this project to explore how AI can be applied to real-world production support scenarios. It simulates how engineers can quickly identify and resolve issues using historical data and intelligent retrieval mechanisms.

---

## Future Improvements

* Integrate with real-time monitoring tools (Splunk, Grafana)
* Enhance retrieval accuracy with better embeddings
* Add alert-based triggering
* Deploy as a scalable backend service

---

## Resume Summary

Built an AI-powered incident resolution assistant using LangChain and vector search (FAISS) to retrieve relevant historical data and generate actionable troubleshooting insights.
