
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

