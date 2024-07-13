import streamlit as st


st.write("This is a ChatBot using Gemini")

question = st.text_input("Insert your question")

main_button = st.button("Insert")

if main_button:
  question = f"Your question is: {question}"
  st.write(question)
