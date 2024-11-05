import os
import streamlit as st
from llm import llm
from langchain_core.prompts import ChatPromptTemplate
from vector_db import (
    store_response,
    setup_weaviate_schema,
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Você é um assistente útil que responde perguntas com clareza.",
        ),
        ("human", "{input}"),
    ]
)


def get_response(user_input):
    formatted_input = prompt.format(input=user_input)
    response = llm.invoke(formatted_input)
    return response.content


def main():
    st.title("Chatbot Interativo")
    user_input = st.text_input("Você: ", "")
    if user_input:
        response = get_response(user_input)
        store_response(user_input, response)
        st.write("Bot:", response)


if __name__ == "__main__":
    setup_weaviate_schema()
    main()
