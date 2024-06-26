from tools import get_model, get_embedding
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SequentialChain
from langchain.prompts import PromptTemplate

model = get_model()

template_1 = """
Tengo un problema de optimizacion por resolver: {problem}
Para este problema devuelve {number} soluciones distintas que traten de resolver el problema. 
Cada solucion debe contener una funcion objetivo y un criterio: [minimizar, maximizar]

Notar que tienes que devolver solo la funcion objetivo y el criterio de dicha forma:
OUTPUT:
  FUNCION OBJETIVO: f(x_1,x_2,...,x_n)    ... donde x_i son las variables de decision del problema
    EXPLICACION DEL POR QUE SE DECIDIO LA FUNCION OBJETIVO: ...
  CRITERIO: x que pertenece a C           ... donde C = [minimizar, maximizar]
"""

template_2 = """
Tengo las posibles soluciones siguientes:

{results}

Por cada solucion posible, coge cada una y evalua su potencial. 
Considera sus pros y contras. Asigna una probabilidad de exito y 

  FUNCION OBJETIVO: f(x_1,x_2,...,x_n)      ... donde x_i son las variables de decision del problema
  CRITERIO: x                               ... x pertenece a [ minimizar, maximizar ]

Y tengo el problema {problem}
Necesito que me obtengas un conjunto de restricciones para evaluar la funcion objetivo
"""

prompt_1 = PromptTemplate(
  input_variables=['problem', 'number'],
  template=template_1
)
chain_1 = LLMChain(
  llm=model,
  prompt=prompt_1,
  output_key='prop_soln'
)

