import shutil
import src.load_env as lenv
import requests
from pypdf import PdfReader
import os
import re
import google.generativeai as genai
from chromadb import Documents, EmbeddingFunction, Embeddings
import chromadb
from typing import List

# Load the PDF file and extract text from each page
def load_pdf(file_path):
  reader = PdfReader(file_path)
  text = ""
  for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
      text += page_text
  return text

pdf_text = load_pdf("./database/pdf/MD_guide.pdf")

# Split the text into chunks based on double newlines
def split_text(text):
  return [i for i in re.split('\n', text) if i.strip()]

chunked_text = split_text(pdf_text)

# Define a custom embedding function using Gemini API
class GeminiEmbeddingFunction(EmbeddingFunction):
  def __call__(self, input: Documents) -> Embeddings:
    gemini_api_key = lenv.geminiapi_key
    genai.configure(api_key=gemini_api_key)
    model = lenv.model_embedding
    title = "Custom query"
    return genai.embed_content(
      model=model, 
      content=input, 
      task_type="retrieval_document", 
      title=title
    )["embedding"]

# Create directory for database if it doesn't exist
db_folder = "./database/chromadb"
if not os.path.exists(db_folder):
  os.makedirs(db_folder)

# Create a Chroma database with the given documents
def create_chroma_db(documents: List[str], path: str, name: str):
  chroma_client = chromadb.PersistentClient(path=path)
  db = chroma_client.create_collection(name=name, embedding_function=GeminiEmbeddingFunction())
  for i, d in enumerate(documents):
    db.add(documents=[d], ids=[str(i)])
  return db, name

# Specify the path and collection name for Chroma database
db_name = "rag_experiment"
db_path = os.path.join(os.getcwd(), db_folder)

if os.path.exists(db_path):
  shutil.rmtree(db_path)  # Borra la carpeta de la base de datos si existe

db, _ = create_chroma_db(chunked_text, db_path, db_name)

# Load an existing Chroma collection
def load_chroma_collection(path: str, name: str):
  chroma_client = chromadb.PersistentClient(path=path)
  return chroma_client.get_collection(name=name, embedding_function=GeminiEmbeddingFunction())

db = load_chroma_collection(db_path, db_name)

# Retrieve the most relevant passages based on the query
def get_relevant_passage(query: str, db, n_results: int):
  results = db.query(query_texts=[query], n_results=n_results)
  return [doc[0] for doc in results['documents']]

query = "Que son los numeros primos"
relevant_text = get_relevant_passage(query, db, n_results=1)

# Construct a prompt for the generation model based on the query and retrieved data
def make_rag_prompt(query: str, relevant_passage: str):
  escaped_passage = relevant_passage.replace("'", "").replace('"', "").replace("\n", " ")
  prompt = f"""You are a helpful and informative bot that answers questions using text from the reference passage included below.
            Be sure to respond in a complete sentence, being comprehensive, including all relevant background information.
            However, you are talking to a non-technical audience, so be sure to break down complicated concepts and
            strike a friendly and conversational tone.
            QUESTION: '{query}'
            PASSAGE: '{escaped_passage}'
            ANSWER:
            """
  return prompt

# Generate an answer using the Gemini Pro API
def generate_answer(prompt: str):
  genai.configure(api_key=lenv.geminiapi_key)
  model = genai.GenerativeModel(lenv.model)
  result = model.generate_content(prompt)
  return result.text

# Construct the prompt and generate the answer
final_prompt = make_rag_prompt(query, "".join(relevant_text))
answer = generate_answer(final_prompt)
print(answer)


"""

# Interactive function to process user input and generate an answer
def process_query_and_generate_answer():
    query = input("Please enter your query: ")
    if not query:
        print("No query provided.")
        return
    db = load_chroma_collection(db_path, db_name)
    relevant_text = get_relevant_passage(query, db, n_results=1)
    if not relevant_text:
        print("No relevant information found for the given query.")
        return
    final_prompt = make_rag_prompt(query, "".join(relevant_text))
    answer = generate_answer(final_prompt)
    print("Generated Answer:", answer)

# Invoke the function to interact with user
process_query_and_generate_answer()
"""