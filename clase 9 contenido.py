# EJ. 1 Crea un script que le pida al usuario una lista de países (separados por comas). Estos se deben almacenar en una
# lista. No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países
# ordenados alfabéticamente y separados por comas.

# EJ. 2 En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista
# pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante la función reduce.
"""Código de la clase"""
import logging

logging.basicConfig(level=logging.WARNING)  # aquí digo desde que nivel inclusive comienza a mostrarme las alertas
logging.info('arrancando programa')
logging.warning('hace calor')
logging.error('test')
logging.critical('adios')

# Ejemplo con función filter
números = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# para poder utilizar filter necesito, filter( una función que devuelve true o false, lista)
def funcionFiltro(x):  # soporta un parámetro de entrada
    if x % 2 == 0:
        return True
    return False


resultado = filter(funcionFiltro, números)
print(list(resultado))


def funcFiltro2(z):
    """
    Si la cadena comienza con 'pep', devuelve True, de lo contrario, devuelve False

    :param z: El valor a probar
    :return: Verdadero o falso
    """
    if str(z).startswith('pep'):
        return True

    return False


resultado2 = filter(funcFiltro2, ['pepe', 'pepito', 'juan'])
print(list(resultado2))


def cuadrado(y):
    return y * y


resultado3 = map(cuadrado, [1, 2, 3, 4, 5, 6, 7, 8, 9, ])
print(list(resultado3))

from functools import reduce


# reduce(function, lista)
def suma(a, b):
    return a + b


res = reduce(suma, [1, 2, 3, 4, 5])
print(res)

# Función zip
# Creating a list of strings.
cursos = ['java', 'python', 'git']
asistentes = [15, 20, 4]
# Creating a list of tuples.
demo1 = zip(cursos, asistentes)
# Converting the zip object into a list.
print(list(demo1))

# Palabras reservadas all y any
listA = (1 == 1, 2 == 2, 3 == 4)
resu1 = any(listA)
print('uso de any = ', resu1)
resu2 = all(listA)
print('uso de all = ', resu2)

# funciones round y min
a = 5.4
b = 5.5
c = 5.6
print(round(a))
print(round(b))
print(round(c))
print('uso de min = ', min(2, 3, 4, 5, 6, 1))

# Función pow
print(pow(2, 4))  # es igual a 2 ** 4

# Algunas funciones con listas
listaB = ['z', 'c', 'd', 'a']
# Sorting the list in ascending order and then in descending order.
ordenada = sorted(listaB)
ordenadaR = sorted(listaB, reverse=True)
print('lista ordenada', ordenada)
print('lista ordenada inversa ', ordenadaR)

# Función input
# Asking the user to input a value and then assigning that value to the variable `a`.
a = input('¿cómo de llamas? ')
# Using a new feature of Python 3.6 called f-strings.
print(f'Hola {a}')

