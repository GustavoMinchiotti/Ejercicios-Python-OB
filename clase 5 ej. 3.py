# Escribe una función que pueda decirte si un año(número entero) 
#es bisiesto o no.
'''Un año es bisiesto en el calendario Gregoriano, si es divisible entre 4
y no divisible entre 100, y también si es divisible entre 400.

En programación, el algoritmo para calcular si un año es bisiesto es un
algoritmo útil para la realización de calendarios.

Considérese las siguientes proposiciones o enunciados lógicos:

p: Es divisible entre 4
¬q: No es divisible entre 100
r: Es divisible entre 400

La fórmula lógica que se suele usar para establecer si un año es bisiesto
p y [¬q ó r]

'''
# https://es.wikibooks.org/wiki/Algoritmo_bisiesto

def bisiesto (year):
    "calcula año bisiesto"
    if year % 4 ==0 and year % 100 != 0 or year % 400 ==0 :
        print(year," es bisiesto")
    else:
        print(year," no es bisiesto")



bisiesto(2024)        
