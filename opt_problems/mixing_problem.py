
# problema de mezcla o mixing problem



mixing_problem_1 = """ 
una fábrica produce aceite mezclando aceites refinados, dos de origen vegetal y tres de origen no vegetal 
en un mes sólo es posible refinar 200 toneladas de vegetal y 250 de no vegetal 
el aceite resultante debe cumplir un valor de dureza comprendido entre 3 y 6 
el costo de una tonelada para cada aceite refinado junto con su dureza aparecen en la siguiente tabla:

|        | Veg_1     | Veg_2     | NoVeg_1     | NoVeg_2     | NoVeg_3     |
| ------ | --------- | --------- | ----------- | ----------- | ----------- |
| costo  | 110       | 120       | 130         | 110         | 115         |
| dureza | 8.8       | 6.1       | 2.0         | 4.2         | 5.0         |

se trata de refinar las cantidades apropiadas de cada aceite a fin de maximizar el beneficio de la producción final sabiendo que una tonelada del aceite producido se vende a 150
"""

mixing_answer_1 = """ 
**variables de decision**

  x_1: cantidad de aceite refinado Veg_1
  x_2: cantidad de aceite refinado Veg_2
  x_3: cantidad de aceite refinado NoVeg_1
  x_4: cantidad de aceite refinado NoVeg_2
  x_5: cantidad de aceite refinado NoVeg_3
  y: cantidad de aceite a producir

**restricciones**

aceite no vegetal refinado <= capacidad de refino vegetal
  x_1 + x_2 <= 200 

aceite no vegetal refinado <= capacidad de refino no vegetal
  x_3 + x_4 + x_5 <= 250   

límite superior de dureza del aceite producido
  8.8 * x_1 + 6.1 * x_2 + 2 * x_3 + 4.2 * x_4 + 5 * x_5 <= 6 * y 

límite inferior de dureza del aceite producido  
  8.8 * x_1 + 6.1 * x_2 + 2 * x_3 + 4.2 * x_4 + 5 * x_5 >= 3 * y   

suma de las cantidades de los aceites refinados = cantidad de aceite producido
  x_1 + x_2 + x_3 + x_4 + x_5 = y 

no negatividad
  x_1 >= 0
  x_2 >= 0
  x_3 >= 0
  x_4 >= 0
  x_5 >= 0
  x_6 >= 0

**funcion objetivo**

max z = 150 * y - 110 * x_1 - 120 * x_2 - 130 * x_3 - 110 * x_4 - 115 * x_5
"""




mixing_general = """
  PROBLEMA
una fabrica produce un producto X mezclando N materiales: m_1, m_2, m_3, ..., m_N, donde se cumple que estos pueden agruparse en diferentes categorias o tipos:

  x_1 materiales de tipo 1 formados por el conjunto C_1 in set (  m_1, m_2, m_3, ..., m_N  )
  x_2 materiales de tipo 2 formados por el conjunto C_2 in set (  m_1, m_2, m_3, ..., m_N  )
  x_3 materiales de tipo 3 formados por el conjunto C_3 in set (  m_1, m_2, m_3, ..., m_N  )
  ...
  x_T materiales de tipo T formados por el conjunto C_T in set (  m_1, m_2, m_3, ..., m_N  )

Pueden ser o no disjuntos los conjuntos C_i

en un periodo de tiempo determinado es posible un maximo de materiales de tipo i, se puede expresar de la siguiente forma:
  t_1 cantidades que entran a la fabrica de los materiales de tipo 1
  t_2 cantidades que entran a la fabrica de los materiales de tipo 2
  t_3 cantidades que entran a la fabrica de los materiales de tipo 3
  ...
  t_T cantidades que entran a la fabrica de los materiales de tipo T

El producto X tiene que cumplir con un valor f, que viene proporcionado de la mezcla de los materiales

TABLA: Costo de los tipo de materiales y lo que aportan al producto X para el valor f

|          | material 1  | material 2  | material 3  | ... | material N  | 
| -------- | ----------- | ----------- | ----------- | --- | ----------- | 
| costo    | c_1         | c_2         | c_3         | ... | c_N         |
| valor f  | v_1         | v_2         | v_3         | ... | v_N         |

se trata de maximizar el beneficio de la produccion final conociendo que el producto se vende a un precio P

  RESPUESTA

**variables de decision**
  m_1: cantidad del material 1 
  m_2: cantidad del material 2
  m_3: cantidad del material 3
  ... 
  m_N: cantidad del material N
  
  x_1: materiales de tipo 1 formados por el conjunto C_1 in set (  m_1, m_2, m_3, ..., m_N  )
  x_2: materiales de tipo 2 formados por el conjunto C_2 in set (  m_1, m_2, m_3, ..., m_N  )
  x_3: materiales de tipo 3 formados por el conjunto C_3 in set (  m_1, m_2, m_3, ..., m_N  )
  ...
  x_T: materiales de tipo T formados por el conjunto C_T in set (  m_1, m_2, m_3, ..., m_N  )

  t_1: cantidades que entran a la fabrica de los materiales de tipo 1
  t_2: cantidades que entran a la fabrica de los materiales de tipo 2
  t_3: cantidades que entran a la fabrica de los materiales de tipo 3
  ...
  t_T: cantidades que entran a la fabrica de los materiales de tipo T

  c_1: costo del material 1
  c_2: costo del material 2
  c_3: costo del material 3
  ...
  c_N: costo del material N 

  v_1: valor f que proporciona el material 1 al producto final
  v_2: valor f que proporciona el material 2 al producto final
  v_3: valor f que proporciona el material 3 al producto final
  ...
  v_N: valor f que proporciona el material N al producto final

  N: cantidad de materiales de la fabrica
  T: cantidad de tipos de materiales de la fabrica 
  P: precio del producto final

  f: funcion que tiene que cumplirse que esta regido por los valores v_i 

  X: cantidad del producto que se tiene que producir  

**restricciones**

**funcion objetivo**

"""

mixing_examples = f"""
EJEMPLO 1:
  PROBLEMA:
{mixing_problem_1}
  RESPUESTA:
{mixing_answer_1}

EJEMPLO 2:
  PROBLEMA:

  RESPUESTA:

"""


def main() -> None:
  print(mixing_general)
  print(mixing_examples)

if __name__ == '__main__':
  main()

