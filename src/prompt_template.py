from langchain_core.prompts import ChatPromptTemplate

def prompt_modify_query(model):
  prompt = ChatPromptTemplate.from_template(
    """
    RECONSTRUIR UN PROMPT
    """)
  chain = prompt | model
  return chain

def prompt_ask_yes_or_not(model):
  prompt = ChatPromptTemplate.from_template(
    """Solo responde con 'YES' or 'NO'
    
    Si no sabes responder la pregunta, di: 'NO'

    {ask}
    """)
  chain = prompt | model
  return chain

