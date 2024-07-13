import streamlit as st


st.write("This is a ChatBot using Gemini")

question = st.text_area(
  "Insert your question here!!!"
)

main_button = st.button("Insert")

if main_button:
  display = f"""Your question is:  
  
  {question}
  """
  st.write(display)
