from typing import (
  Any,
  List,
  Dict
)

from src.core import (
  get_model,
  get_embedding,
  prompt_template_QA
)

from langchain_google_genai import (
  GoogleGenerativeAI,
  GoogleGenerativeAIEmbeddings
)

from langchain_core.messages import (
  HumanMessage,
  AIMessage
)
from langchain_core.prompts import (
  ChatPromptTemplate,
  MessagesPlaceholder
)
from langchain_core.output_parsers import (
  JsonOutputParser
)




class BaseHistory : 

  def __init__(self) -> None:
    pass

  def clean_history (self) -> Any:
    return "clean history function"

  def process_query (self, query: str) -> str:
    return prompt_template_QA (question=query, k=10, model=get_model())



