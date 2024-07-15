from src.tools import get_model, get_embedding
from src.create_vectorstore import FAISS_VECTORSTORE

from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder



class BaseHistory():
  


  def __init__(self) -> None:
    self.model: GoogleGenerativeAI = get_model()
    self.embedding: GoogleGenerativeAIEmbeddings = get_embedding()
    self.chat: list = []
    self.prompt = """
    Eres un asistente, capaz de responder detalladamente las respuestas que se te hagan
    Tambien debes tener conocimiento sobre la conversacion que tengas con el usuario
    """
    self.vectorstore = FAISS_VECTORSTORE(load=True)  



  def make_chain(self) -> None:
    self.prompt = ChatPromptTemplate.from_messages([
      ('system', f'{self.prompt}'),
      MessagesPlaceholder(variable_name='chat'),
      ('human', '{input}')
    ])
    self.chain = self.prompt | self.model



  def clean_history(self) -> None:
    self.chat: list = []



  def send_processed_query(self, query: str) -> str:
    response = self.chain.invoke({'input':query, 'chat':self.chat})
    self.chat.append( HumanMessage(content=query) )
    self.chat.append( AIMessage(content=response) )

    return response


