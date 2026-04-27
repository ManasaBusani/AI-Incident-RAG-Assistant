import streamlit as st
from src.rag_llm_assistant import analyze

st.set_page_config(page_title="AI Incident Assistant")

st.title("🚀 AI Incident Resolution Assistant")

issue = st.text_area("Enter issue", "Payment API is slow and timing out")

if st.button("Analyze"):
    result = analyze(issue)
    st.success("Analysis Complete")
    st.write(result)
