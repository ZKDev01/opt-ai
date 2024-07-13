from tools import get_model

from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SequentialChain
from langchain.prompts import PromptTemplate

NUMBERS_OF_SOLUTIONS = 10
model = get_model()

template_base = """
Tengo un problema de optimizacion que necesito resolver.

PROBLEMA: {input}

Provee {NUMBERS_OF_SOLUTIONS} soluciones distintas que sean capaces de resolver el problema en cuestion. 

El problema que se presenta anteriormente es un tipo de problema de: {problem_type}

A continuacion se mostrara una forma de resolver un problema, parecido al de la entrada 

{EXAMPLES}

"""

template_evaluate = """ 
Por cada solucion propuesta, evalua su potencial. 

Considerando:
- Pros 
- Contras
- Initial effort required
- Implementacion 
- Difficulty
- Potential callenges
- Expected outcomes

Asigna una probabilidad de exito 

{PROPOSED_SOLUTION}
"""

template_final = """
For each solution, elaborate on the thought process by generating potential scenarios, outlining strategies for implementation, 
identifying necesary partnership or resources, and proposing solutions to potential obstacles.
Additionally, consider any unexpected outcomes and outline contingency plans for their managment
{solns}
"""

template_result = """
Rank the solutions based on evaluations and scenarios, assigning a probability of sucess in percentage for each.
Provide justification and final thought for each ranking.
Each ranking should be broken down into 4 points, Probability of sucess, justification, modes of failure and final thoughts. 
Rank according to the highest probability of sucess
{proc_output}
"""

def make_chain(
    template: str, 
    input_variables: list[str], 
    output_key: str ) -> LLMChain:
  
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
    input_variables=[],
    output_key=[]
  )
  chain_2 = make_chain(
    template=template_base,
    input_variables=[],
    output_key=[]
  )
  chain_3 = make_chain(
    template=template_base,
    input_variables=[],
    output_key=[]
  )
  chain_4 = make_chain(
    template=template_base,
    input_variables=[],
    output_key=[]
  ) 

  chain = SequentialChain(
    chains=[ chain_1,chain_2,chain_3,chain_4 ],
    input_variables=[],
    output_variables=['result']
  )

  return

def get_answer_from_tot() -> str:
  chain = make_tot()
  answer = chain( {
    '': [],
  } )
  return answer['result']

