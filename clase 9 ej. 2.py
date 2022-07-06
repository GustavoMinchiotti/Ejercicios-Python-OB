# EJ. 2 En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una
# lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.
from functools import reduce

lista = {5, 6, 8, 2, 3}
lista2 = {5, 6, 8, 2, 3}


# para poder utilizar filter necesito, filter( una función que devuelve true o false, lista)
def funcFiltro(x):  # soporta un parámetro de entrada
    if x % 2 != 0:
        return True
    return False


resultado = filter(funcFiltro, lista)
print(list(resultado))

copiares = list(resultado)


# reduce(function, lista)
def suma(a, b):
    return a + b


res = reduce(suma, copiares)
print(res)
