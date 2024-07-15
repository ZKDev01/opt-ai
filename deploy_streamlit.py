import streamlit as st
from src.chat_history import BaseHistory
from src.primary_process_engine import selector_system

st.write("This is a ChatBot using Gemini")

question = st.text_area(
  "Insert your question here!!!"
)

llm = BaseHistory()

main_button = st.button("Insert")

def run(query: str, llm: BaseHistory) -> str:

  output = selector_system(
    llm_historial=llm,
    query=query,
    kvalues_for_rag=5,
    numbers_througth=5 )
  
  return output



if main_button:
  display = f"""Your question is:  
  
  {question}
  """

  st.write(display)

  answer = run(query=question, llm=llm)  

  
  st.write(answer)
