import streamlit as st 

from src.chat_history import (
  BaseHistory 
)


chat_history = BaseHistory ()



query = st.text_input (
  label='Introduzca una consulta'
)

btn_process = st.button (
  label='Procesar consulta'
)



if btn_process and len(query) > 0:  
  st.write ( chat_history.process_query (query=query) )


