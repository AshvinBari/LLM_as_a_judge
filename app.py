import streamlit as st
from openai import OpenAI
from tavily_search import search_web
from judge import evaluate_answer
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

st.title("LLM Judge + Tavily RAG")

question = st.text_input("Ask a question")

if st.button("Generate Answer"):

    context = search_web(question)

    prompt = f"""
Use this context to answer.

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    answer = response.choices[0].message.content

    evaluation = evaluate_answer(
        question,
        answer,
        context
    )

    st.subheader("Answer")
    st.write(answer)

    st.subheader("Evaluation")
    st.write(evaluation)