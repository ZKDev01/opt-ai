from re import S
from typing import (
  Any,
  List,
  Dict
)

from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.documents import Document
from langchain_core.output_parsers import JsonOutputParser

from src.vectorstore import Vectorstore

PROMPT = """
Eres un asistente virtual, capaz de responder detalladamente las preguntas que se te hagan
Tambien puedes dar explicaciones sobre temas especificos 
Puedes analizar la conversacion que tengas con el usuario para poder mejorar las respuestas futuras
"""


class ChatHistory:
  def __init__(self,vectorstore:Vectorstore) -> None:
    self.model = ...
    self.chat:List = [ ]
    self.prompt = ChatPromptTemplate.from_messages([
      ('system', PROMPT),
      MessagesPlaceholder(variable_name='chat'),
      ('human', '{input}')
    ])
    self.llm = self.prompt | self.model 
    self.vectorstore:Vectorstore = vectorstore 

  def clean_history (self) -> None:
    self.chat:List = [ ]

  def process_query (self, query:str, few_shots:List[str] = []) -> str:
    response = self.llm.invoke({
      'input': self.create_prompt(PROMPT, few_shots=few_shots),
      'chat' : self.chat
    })
    self.chat.append ( HumanMessage(content=query) )
    self.chat.append ( AIMessage(content=response) )
    return response
  
  def create_prompt (self, prompt:str, few_shots:List[str] = []) -> str:
    response = self.model.invoke({
      'input': prompt,
      'chat' : self.chat
    })



