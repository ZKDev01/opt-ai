import os 
import streamlit as st 

from src.chat_history import (
  BaseHistory 
)
from src.vectorstore import FAISS_VECTORSTORE
from src.core import FAISS_PATH

# Buscar las bases de datos creadas de faiss
vs_dirs = [ FAISS_PATH + element for element in os.listdir(FAISS_PATH) ]

# Mostrarlas y recopilar datos
opt = st.multiselect(
  label='Seleccion de base de datos vectorial',
  options=vs_dirs
)

query = st.text_input(
  label='Query'
)
k = st.number_input(
  label='Numero de peticiones',
  min_value=1,
  max_value=5
)

btn = st.button ("Process")

# aplicar una busqueda de similitud 
# TODO: Aplicar LLM + Result 

if btn:
  for vs_dir in opt:
    vs = FAISS_VECTORSTORE(folder_path=vs_dir, load=True)
    results = vs.similarity_search(query=query, k=k)
    st.write (f"Resultados de la vectorstore {vs_dir}")
    for i,result in enumerate(results):
      st.write (f"Answer {i+1}")
      st.markdown (result.page_content)
  

