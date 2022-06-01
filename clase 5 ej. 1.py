# Escribe una función que calcule el área de un triángulo, recibiendo la altura
# y la base como parámetros y otra función que calcule el área de un círculo
# recibiendo el radio del mismo.

import math
math.pi     #googlee como importar pi para el calculo

def triangulo(base,altura):
    "calcular área triángulo"
    area=base*altura/2
    print("El área del triangulo es ",area)

def circulo(radio):
    "calcular área círculo"
    areaC= math.pi*(radio*radio)
    print("El área del círculo es ",areaC)


#print(math.pi)

triangulo(2,4)    
circulo(2)

