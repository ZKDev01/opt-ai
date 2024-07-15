# Formulacion por programacion de metas



general_problem = """



"""

general_answer = """
**funcion objetivo:**
min Z = sum_{e=1}^E sum_{j in J_e} C_j * x_j + sum_{i=1}^I ( u_i * (d_i^-) - o_i * (d_i^+) ) 

**restricciones**
  sum_{e=1}^E sum_{j in J_e} a_1j * x_j + (d_1^+) - (d_1^-) = r_1 
  sum_{e=1}^E sum_{j in J_e} a_2j * x_j + (d_2^+) - (d_2^-) = r_2 
  sum_{e=1}^E sum_{j in J_e} a_3j * x_j + (d_3^+) - (d_3^-) = r_3 
  ...
  sum_{e=1}^E sum_{j in J_e} a_Ij * x_j + (d_I^+) - (d_I^-) = r_I 

**variables de decision**
"""


def main() -> None:
  print(general_answer)

if __name__ == '__main__':
  main()

