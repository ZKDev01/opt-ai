from tools import get_model

from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SequentialChain
from langchain.prompts import PromptTemplate

model = get_model()

template_base = """
Tengo un problema de optimizacion que necesito resolver.

PROBLEMA: {INPUT}

Provee {NUMBERS_OF_SOLUTIONS} soluciones distintas que sean capaces de resolver el problema en cuestion. 

El problema que se presenta anteriormente es un tipo de problema de: {TYPE}

A continuacion se mostrara una forma de resolver un problema, parecido al de la entrada 

{EXAMPLES}
"""

template_evaluate = """ 
Por cada solucion propuesta, evalua su potencial. 

Considerando:
- Ventajas del modelo propuesto 
- Desventajas del modelo propuesto
- Esfuerzo inicial requerido 
- Implementacion
- Dificultad 
- Desafios potenciales para ser un modelo valido
- Resultados esperados: si son validos para acertar el modelo

Asigna una probabilidad de exito 

{PROPOSED_SOLUTION}
"""

template_thought = """
Por cada solucion, profundice el proceso de pensamiento generando escenarios potenciales, 
esbozando estrategias para la implementacion, identificando las asociaciones o recursos 
necesarios y proponiendo soluciones a posibles obstaculos. Ademas, considere cualquier 
resultado inesperado 

{solns}
"""

template_final = """
Clasifique las soluciones basandose en evaluaciones y escenarios, asignando una probabilidad 
de exito en procentaje para cada una. Proporcione justificacion y pensamientos finales para 
cada clasificacion. Cada clasificacion debe desglosarse en 4 puntos: 
- Probabilidad de exito 
- Justificacion
- Modos de fallo 
- Pensamientos finales

Clasifique segun la mayor probabilidad de exito
{proc_output}
"""

def make_chain(template: str, input_variables: list[str], output_key: str ) -> LLMChain:
  
  chain = LLMChain(
    llm=model,
    prompt=PromptTemplate(
      input_variables=input_variables,
      template=template
    ),
    output_key=output_key
  )
  
  return chain

def make_tot() -> SequentialChain:
  chain_1 = make_chain(
    template=template_base,
    input_variables=['INPUT','NUMBERS_OF_SOLUTIONS','TYPE','EXAMPLES'],
    output_key=['PROPOSED_SOLUTION']
  )
  chain_2 = make_chain(
    template=template_base,
    input_variables=['PROPOSED_SOLUTION'],
    output_key=['SOLUTIONS']
  )
  chain_3 = make_chain(
    template=template_base,
    input_variables=['SOLUTIONS'],
    output_key=['PROCESSED_SOLUTIONS']
  )
  chain_4 = make_chain(
    template=template_base,
    input_variables=['PROCESSED_SOLUTIONS'],
    output_key=['RESULTS']
  ) 

  chain = SequentialChain(
    chains=[ chain_1,chain_2,chain_3,chain_4 ],
    input_variables=['INPUT','NUMBERS_OF_SOLUTIONS','TYPE','EXAMPLES'],
    output_variables=['RESULTS']
  )

  return chain

def get_answer_from_tot(req: dict[str, str]) -> str:
  chain = make_tot()

  answer = chain( {
    'INPUT': req['INPUT'],
    'NUMBERS_OF_SOLUTIONS': req['NUMBERS_OF_SOLUTIONS'],
    'TYPE': req['TYPE'],
    'EXAMPLES': req['EXAMPLES'] 
  } )

  return answer['RESULTS']
