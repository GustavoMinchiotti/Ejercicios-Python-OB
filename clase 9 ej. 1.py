# EJ. 1 Crea un script que le pida al usuario una lista de países (separados por comas). Estos se deben almacenar en una
# lista. No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países
# ordenados alfabéticamente y separados por comas.

# listaPaises = list(input('ingrese lista de países separados por comas: '))
# print(listaPaises)

# puta lista..
from numpy import sort

listaIspas = ['ar', 'mex', 'esp', 'can', 'den']
orden = sort(listaIspas)
print(orden)

# EJERCICIO RESUELTO
# Asking the user to input a list of countries separated by commas.
items = input("Introduce países separados por comas:\n")

# Creating a list of countries.
paises = [pais for pais in items.split(",")]

# Joining the list of countries with a comma.
# Creating a set of the list of countries and then converting it back to a list.

print(",".join(sorted(list(set(paises)))))
