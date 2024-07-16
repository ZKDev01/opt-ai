# Formulacion clasica o por cobertura de conjuntos

general_problem = """
Una organizacion necesita garantizar que sus operaciones diarias esten adecuadamente cubiertas por personal suficiente,
pero tambien 

Se tiene una organizacion, escuela o empresa, y esta necesita garantizar que los empleados esten presentes en turnos definidos. 
Se tienen J turnos y para cada turno se necesitan r_i personas minimas para cubrirlo
  r_1: numero de personas que como minimo se necesitan para cubrir el turno 1
  r_2: numero de personas que como minimo se necesitan para cubrir el turno 2
  r_3: numero de personas que como minimo se necesitan para cubrir el turno 3 
  ... 
  r_J: numero de personas que como minimo se necesitan para cubrir el turno J

Cada turno puede tener diferentes periodo de trabajos. Se tienen un total de I periodos para cada turno
"""

general_answer = """
**variables de decision:**
  W     : numero total de empleados asignados a todos los turnos J
  x_j   : numero de empleados asignados al turno j
  a_ij  : 1 si el periodo i es un periodo de trabajo para el turno j, 0 de lo contrario
  r_j   : minima cantidad de empleados requeridos en el turno j
  I     : numero de periodos a ser asignados en la semana 
  J     : numero de turnos considerados

**restricciones**
  
  (a_11 * x_1) + (a_12 * x_2) + (a_13 * x_3) + ... + (a_1J * x_J) >= r_1
  (a_21 * x_1) + (a_22 * x_2) + (a_23 * x_3) + ... + (a_2J * x_J) >= r_2
  (a_31 * x_1) + (a_32 * x_2) + (a_33 * x_3) + ... + (a_3J * x_J) >= r_3
  ...
  (a_I1 * x_1) + (a_I2 * x_2) + (a_I3 * x_3) + ... + (a_IJ * x_J) >= r_I
  
  x_1 >= 0
  x_2 >= 0
  x_3 >= 0
  ...
  x_J >= 0

  x_i es un numero entero 

**funcion objetivo:**
min W = x_1 + x_2 + x_3 + ... + x_J 
"""



def main() -> None:
  print(general_problem)
  print(general_answer)

if __name__ == '__main__':
  main()

