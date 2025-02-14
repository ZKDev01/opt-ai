from typing import Optional
from langchain_ollama import ChatOllama
from pydantic import BaseModel,Field
from sympy import N
import ast 

json_schema = {
  "title": "basic-solver",
  "description": "La solucion factible basica es una asignacion de valores a las variables de deciones que cumplen con las restricciones del modelo",
  "type": "object",
  "properties": {
    "solucion": {
      "type": "string",
      "description": """
      asignacion de las variables de decision que cumplen con las restricciones del modelo (no necesariamente debe ser una asignacion optima)
      un ejemplo de salida es: {'x1': 1, 'x2': 2}, {'x1': 0, 'x2': 2, 'x3': 3}
      """,
    },
  },
  "required": ["solucion"],
}



llm = ChatOllama(model='llama3.2:latest')
structured_llm = llm.with_structured_output(json_schema)


r = structured_llm.invoke("""
variables de decision: x1, x2
objetive-function: max 2*x1 + 3*x2,
restriccion: [
  x1 + x2 <= 3,
  x1 + 2*x2 >= 4,
  x1 >= 0,
  x2 >= 0
],
que posibles valores enteros de x1,x2 sean factibles?
""")

print(r)
solucion = r['solucion']
print (solucion['x1'])
print (solucion['x2'])
#dict_data = ast.literal_eval(r['solucion'])
#print(dict_data)


r = structured_llm.invoke("""
variables de decision: x1, x2
objetive-function: max 2*x1 + 3*x2,
restriccion: [
  x1 + x2 <= 3,
  x1 + 2*x2 >= 4,
  x1 >= 0,
  x2 >= 0
],
que posibles valores enteros de x1,x2 sean factibles?
""")

print(r)
solucion = r['solucion']
print (solucion['x1'])
print (solucion['x2'])