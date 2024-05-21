import src.load_env as lenv

from src.utils import to_markdown

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain.prompts import PromptTemplate

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma

import os
import google.generativeai as genai

llm = ChatGoogleGenerativeAI(model=lenv.model,google_api_key=lenv.geminiapi_key)
embeddings = GoogleGenerativeAIEmbeddings(model=lenv.model_embedding,google_api_key=lenv.geminiapi_key)

# LOAD THE PDF and SPLIT
loader = PyPDFLoader("./database/pdf/MD_guide.pdf")
pages = loader.load_and_split()

# INITIALIZE VECTORDB and RETRIEVER
vector_db = Chroma.from_documents(pages[1:5],embeddings)
retriever = vector_db.as_retriever(search_kwargs={"k": 2})

# DEFINE THE RETRIEVAL CHAIN
template = """
Eres un asistente.
Responde basadose en el contenido provisto
context: {context}
input: {input}
answer:
"""

prompt = PromptTemplate.from_template(template)
combine_docs_chain = create_stuff_documents_chain(llm, prompt)
retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)

response = retrieval_chain.invoke({"input": "Quien es Harry Potter"})
print(response["answer"])

