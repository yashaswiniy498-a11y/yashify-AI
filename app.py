import streamlit as st
from transformers import pipeline

st.title("🤖 Yashify AI")

summarizer = pipeline(
    "summarization",
    model="t5-small"
)

text = st.text_area("Paste your text here:")

if st.button("Summarise"):
    if text:
        summary = summarizer(
            text,
            max_length=50,
            min_length=10,
            do_sample=False
        )

        st.subheader("✨ Yashify's Summary")
        st.write(summary[0]["summary_text"])
        st.write("Created by: Yashaswini")
    else:
        st.warning("Please enter some text first.")