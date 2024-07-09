from tools import get_model, get_embedding
from create_vectorstore import FAISS_VECTORSTORE

from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

class BaseHistory():
  
  def __init__(self) -> None:
    self.model: GoogleGenerativeAI = get_model()
    self.embedding: GoogleGenerativeAIEmbeddings = get_embedding()
    self.chat: list = []
    self.prompt = 'Eres una IA capaz de responder preguntas complejas con respuestas sencillas'
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

  def send_message(self, message: str) -> str:
    response = self.chain.invoke({'input':message, 'chat':self.chat})
    self.chat.append( HumanMessage(content=message) )
    self.chat.append( AIMessage(content=response) )

    return response




class RAGHistory(BaseHistory):
  
  def __init__(self) -> None:
    super().__init__()

    self.prompt = """
    PREPARATION: 
    - Debes ser capaz de responder a la respuesta segun el contenido de DOCUMENTS que se te presenten de la mejor forma posible
    - Si el contenido de DOCUMENTS no aporta informacion para responder la pregunta, entonces ignora la pregunta y el contenido presentado y no respondas. Responde que no eres capaz de responder dicha pregunta
    
    OUTPUT FORMAT:
    - La respuesta debe contener dos campos: RESPUESTA, NEW_DOCUMENTS
      - RESPUESTA: Respuesta a la pregunta usando el contenido presentado
      - USED DOCUMENTS: Resumen de las ideas que se tomaron de los contenidos de DOCUMENTS presentados

    INTERACTION EXAMPLES: Un ejemplo es el siguiente:
    ```
    DOCUMENTS: 
    'Los LLM se entrenan con grandes volúmenes de datos y usan miles de millones de parámetros para generar resultados originales en tareas como responder preguntas, traducir idiomas y completar frases.'
    QUESTION: 
    'Que es un LLM?'
    OUTPUT:
      RESPUESTA POSIBLE: Los LLM son entrenados con grandes volumenes de datos para generar resultados originales 
      USED DOCUMENTS: 'Los LLM se entrenan con grandes volúmenes de datos para generar resultados originales en tareas como responder preguntas y completar frases.'
    ```
    """
    self.make_chain()

  def send_message(self, message: str, k: int = 5) -> str:  
    results = self.vectorstore.similarity_search(query=message, k=k)
    input = f"""
    DOCUMENTS: 
      {results}
    QUESTION: {message}

    OUTPUT:
      RESPUESTA POSIBLE: 
      USED DOCUMENTS:
    """
    response = self.chain.invoke({'input': input, 'chat': self.chat})
    self.chat.append( HumanMessage(content=input) )
    self.chat.append( AIMessage(content=response) )
    return response




class ContextHistory(BaseHistory):

  def __init__(self) -> None:
    super().__init__()
    self.prompt = """
    PREPARATION: 
    - Debes ser capaz de responder a la respuesta segun el contenido de CONTEXT que se te presenten de la mejor forma posible
    - La respuesta debe abarcar los puntos de CONTEXT y no puede irse de estas 'areas' que define CONTEXT

    OUTPUT FORMAT:
    - La respuesta debe contener dos campos: RESPUESTA, NEW_DOCUMENTS
      - RESPUESTA: Respuesta a la pregunta usando el contenido presentado
      - TAGS: Tags de context que se usaron para obtener la respuesta

    INTERACTION EXAMPLES: 
    
    Ejemplo 1: 
    ```
    CONTEXT: [ Inteligencia Artificial, Machine Learning ]

    QUESTION: 
    'Que es un LLM?'
    OUTPUT:
      RESPUESTA POSIBLE: Los LLM son entrenados con grandes volumenes de datos para generar resultados originales 
      TAGS: [ Inteligencia Artificial, Machine Learning ]
    ```

    Ejemplo 2:
    ```
    CONTEXT: [ Comida, Competicion ]

    QUESTION:
    'Que se puede hacer con el arroz?'
    OUTPUT:
      RESPUESTA POSIBLE: 
        Con el arroz, puedes preparar una amplia variedad de platos tanto para la comida como para competencias culinarias. Aquí te presento algunas ideas simples y deliciosas:
        - Arroz blanco
        - Paella
        - Arroz con marisco

      TAGS: [ Comida, Competicion ]
    ```

    EJEMPLO 3: 
    ```
    CONTEXT: [ Inteligencia Artificial, Programacion ]

    QUESTION: 
    'Que se puede hacer con el arroz?'
    ```

    OUTPUT:
      RESPUESTA POSIBLE: No es posible responder a las preguntas dadas anteriormente con el CONTEXT proporcionado 
      TAGS: [ ]
      CONTEXT: [ Inteligencia Artificial, Programacion ]
    """
    self.make_chain()

  def send_message(self, message: str, context: list[str]) -> str:
    input = f"""
    CONTEXT: {context}
    QUESTION: {message}

    OUTPUT:
      RESPUESTA POSIBLE: 
      USED DOCUMENTS:
    """
    response = self.chain.invoke({'input': input, 'chat': self.chat})
    self.chat.append( HumanMessage(content=input) )
    self.chat.append( AIMessage(content=response) )
    return response

def main():
  test_rag()
  #test_context()

def test_rag():
  history = RAGHistory()
  response = history.send_message(message='que diferencia existe entre la busqueda semantica y RAG', k=10)
  print(response)

  ## PENDIENTE 
  #response = history.send_message(message='explicame mas lo anterior', k = 5)
  #print(response)

def test_context():
  history = ContextHistory()
  response = history.send_message(message='que diferencia existe entre la busqueda semantica y RAG', context=['RAG', 'Inteligencia Artificial', 'Machine Learning', 'Busqueda Semantica'])
  print(response)

if __name__ == '__main__':
  main()

