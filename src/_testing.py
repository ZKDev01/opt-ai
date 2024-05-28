import os
import load_env as lenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatGoogleGenerativeAI(
  model="gemini-pro",
  google_api_key=lenv.geminiapi_key)

result = llm.invoke("Is apple a fruit?")
print(result)
