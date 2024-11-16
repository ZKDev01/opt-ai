import streamlit as st 

from src.core import load_documents 

st.title ("Document Analyzer")

documents = load_documents()
for i,document in enumerate(documents):
  st.write (f"{i+1}. {document}")




