from typing import (
  Any,
  List,
  Dict
)

from src.core import (
  get_model,
  get_embedding
)

from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.documents import Document
from langchain_core.output_parsers import JsonOutputParser

PROMPT = """
Eres un asistente virtual, capaz de responder detalladamente las preguntas que se te hagan
Tambien puedes dar explicaciones sobre temas especificos 
Puedes analizar la conversacion que tengas con el usuario para poder mejorar las respuestas futuras
"""


class BaseHistory : 

  def __init__(self, vectorstore:Any, prompt:str = PROMPT) -> None:
    self.model = get_model()
    self.embed = get_embedding()

    self.chat:List = [ ]
    self.prompt = ChatPromptTemplate.from_messages([
      ('system', prompt),
      MessagesPlaceholder(variable_name='chat'),
      ('human', '{input}')
    ])
    self.chain = self.prompt | self.model 
    self.vectorstore = vectorstore


  def clean_history (self) -> None:
    self.chat:List = [ ]

  def process_query (self, query:str, chunks:List[Document] = []) -> str:
    response = self.chain.invoke({
      'input': query,
      'chat' : self.chat
    })
    self.chat.append ( HumanMessage(content=query) )
    self.chat.append ( AIMessage(content=response) )
    return response



