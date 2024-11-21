import streamlit as st 

from src.core import (
  load_documents,
  load_contents_from_documents,
  FAISS_PATH
)
from src.vectorstore import FAISS_VECTORSTORE

st.title ("Document Analyzer")

documents = load_documents()
chunks_by_document = { document : load_contents_from_documents(document,document.split('.')[-1]) for document in documents }


# TODO 1. Presentar todos los documentos para elegir cual desea chunkenizar

doc_select = st.multiselect(
  label='Seleccione un documento para analizar',
  options=documents
)
btn_chunks = st.button('Procesar Documentos')
btn_create = st.button('Crear Base de Datos Vectorial con Documentos')

# Presentar chunks de los documentos seleccionados

if btn_chunks:
  for document in doc_select:
    st.write (f'### {document.capitalize()}')
    chunks = chunks_by_document.get(document)
    for i,chunk in enumerate(chunks):
      with st.expander(f'Chunk {i+1}'):
        st.markdown(chunk.page_content)

# TODO 3. Hacer una base de datos vectoriales por cada documento que haya elegido

if btn_create:
  for document in doc_select:
    chunks = chunks_by_document.get(document)
    folder_path = FAISS_PATH + document + ' Vectorstore\\'
    vs = FAISS_VECTORSTORE(folder_path=folder_path, load=False, chunks=chunks)
    
