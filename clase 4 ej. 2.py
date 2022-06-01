# Clase 4 ej 2
'''Escribe un programa capaz de mostrar todos los números impares desde
un número de inicio y otro final.

Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8,
el programa debe imprimir por consola: [3, 5, 7]'''

'''ciclo for y modulo'''
numIni = input("Ingrese un valor inicial: ")
numFin = input("Ingrese un valor final: ")

numIni = int(numIni)
numFin = int(numFin)

for n in range(numIni, numFin):
    
    #print(n)
    if n %2 != 0:  #tardé por no buscar los operadores 
        print(n)
