

concepts = """
un problema de optimizacion en dimension finita consiste en hallar el menor o mayor valor de una funcion f(x) si x pertenece a M, 
donde M es el subconjunto de soluciones factibles

min f(x) o max f(x)

- se sabe que f(x) es la funcion objetivo
- se sabe que x es un vector formado por las variables del problema o variables de decision
- se sabe que un problema de programacion lineal contiene lo que se denominan como restricciones.

las restricciones son funciones g(x) o h(x) tales que g(x) < 0, g(x) > 0, g(x) >= 0, g(x) <= 0, mientras que h(x) = 0.
g(x) representan las inecuaciones que tienen que cumplirse para que f(x) sea minima o maxima
h(x) representan las ecuaciones que tienen que cumplirse para que f(x) sea minimia o maxima 
"""



def main() -> None:
  print(concepts)


if __name__ == '__main__':
  main()

