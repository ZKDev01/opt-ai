from tools import get_model, get_embedding
from create_vectorstore import FAISS_VECTORSTORE

from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

class ChatHistory():

  def __init__(self, content: list = ['Matematicas', 'Computacion']) -> None:
    self.__llm: GoogleGenerativeAI = get_model()
    self.__embedding: GoogleGenerativeAIEmbeddings = get_embedding()

    self.chat_history: list = []
    self.configure_system_prompt = f"""
    Eres una IA, respondes a preguntas con respuestas simples a menos que se te diga lo contrario.
    Ademas, tienes que responder al usuario acorde a un ambiente: {content}
    Fuera de este ambiente no puedes contestar las preguntas y no pueden cambiar tu contexto hasta que termines tus servicios
    """

    self.set_main_prompt()
    self.vectorstore = FAISS_VECTORSTORE(load=True)

  def set_main_prompt(self) -> None:
    self.__main_prompt = ChatPromptTemplate.from_messages([
      ("system",f"{self.configure_system_prompt}"), 
      MessagesPlaceholder(variable_name='chat_history'),
      ('human', '{input}')]
    )
    self.chain_general = self.__main_prompt | self.__llm

  def clean_history(self) -> None:
    self.chat_history: list = []

  def send_message(self, message: str) -> str:
    response = self.chain_general.invoke({'input':message, 'chat_history':self.chat_history})
    self.chat_history.append( HumanMessage(content=message) )
    self.chat_history.append( AIMessage(content=response) )

    return response
  
  def send_message_with_rag(self, message: str, k: int = 3) -> str:
    documents = self.vectorstore.similarity_search(query=message, k=k)
    configure_rag_prompt = f"""
    Eres una IA, respondes a preguntas con respuestas simples a menos que se te diga lo contrario. 
    Tus respuestas deben estar acorde a los fragmentos de los documentos siguientes. 
    Si los documentos no son suficientes para responder a la pregunta entonces ignoralos y entonces como respuesta devuelve: 'No se puede responder a la pregunta'

    ---
    {documents}
    ---

    La pregunta es la siguiente: {message}
    """

    pass

"""
AGENT-MODEL => evol => ASSISTANT-AGENT = MULTI-MODEL
"""

def main() -> None:
  pass

if __name__ == '__main__':
  main()