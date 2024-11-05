import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Você é um assistente útil que responde perguntas com clareza."),
        ("human", "{input}"),
    ]
)

chain = prompt | llm


def get_response(user_input):
    response = chain.invoke({"input": user_input})
    return response.content


def main():
    st.title("Chatbot Interativo")
    user_input = st.text_input("Você: ", "")
    if user_input:
        response = get_response(user_input)
        st.write("Bot:", response)


if __name__ == "__main__":
    main()
