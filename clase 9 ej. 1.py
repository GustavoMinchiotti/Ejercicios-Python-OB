# EJ. 1 Crea un script que le pida al usuario una lista de países (separados por comas). Estos se deben almacenar en una
# lista. No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países
# ordenados alfabéticamente y separados por comas.

# EJ. 2 En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista
# pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.
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
    if str(z).startswith('pep'):
        return True

    return False


resultado2 = filter(funcFiltro2, ['pepe', 'pepito', 'juan'])
print(list(resultado2))
