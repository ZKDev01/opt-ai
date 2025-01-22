from langchain_ollama import OllamaLLM

model = OllamaLLM(model="llama3.2:latest")
response:str = model.invoke("what is a LLM?")
print (response)