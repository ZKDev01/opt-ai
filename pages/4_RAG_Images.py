import os
import dotenv
import pathlib
import textwrap
import PIL.Image as pillow
import google.generativeai as genai 

from src.core import load_env 

from typing import (
  Dict,
  List
)
from IPython.display import (
  display,
  display_jpeg,
  Markdown
)

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


api_key = load_env()
genai.configure(api_key=api_key)



model = genai.GenerativeModel(
  model_name='models/gemini-1.5-pro'
)


messages = [
  """
  Que es un LLM?
  """,
  """
  Un LLM es un modelo de aprendizaje profundo?
  """
]

response = model.generate_content(messages)
response.resolve()

response_md = to_markdown(response.text)

import streamlit as st 

st.markdown (response_md)

# TODO 1. Mostrar las imagenes como una galeria (ver si se puede claro)

# TODO 2. Seleccionar un conjunto de imagenes

# TODO 3. Preguntar al LLM sobre informacion de las imagenes


