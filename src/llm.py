from tools import get_model, get_embedding

from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

class ChatHistory():

  def __init__(self) -> None:
    self.__llm: GoogleGenerativeAI = get_model()
    self.__embedding: GoogleGenerativeAIEmbeddings = get_embedding()

    self.chat_history: list = []
    self.configure_system_prompt = """
    Eres una IA, respondes a preguntas con respuestas simples a menos que se te diga lo contrario.
    Ademas, tienes que responder al usuario acorde a un ambiente: Matematicas, Computacion
    Fuera de este ambiente no puedes contestar las preguntas y no pueden cambiar tu contexto hasta que termines tus servicios
    """

    self.__prompt = ChatPromptTemplate.from_messages([
      ("system",f"{self.configure_system_prompt}"), 
      MessagesPlaceholder(variable_name='chat_history'),
      ('human', '{input}')]
    )
    
    self.chain = self.__prompt | self.__llm

  def clean_history(self):
    self.chat_history: list = []

  def send_message(message: str) -> str:
    # TODO
    return answer
  

"""
CHAT-HISTORY
AGENT-MODEL => evol => ASSISTANT-AGENT = MULTI-MODEL
"""