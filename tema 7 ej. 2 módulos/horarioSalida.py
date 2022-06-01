
# tema 7 ej nº2
# Este archivo es el modulo

import time

print("He importado el modulo Clase 7 parte 2")

def horarioSalida():
    salir = time.localtime()
    if salir.tm_hour  < 19:
        a = 18 - salir.tm_hour 
        b = 60 - salir.tm_min
        print('faltan:',a, 'Horas y ',b, 'minutos')
        print()
        print('Siga tra-ba-jan-do')
    else:
        print('YA,  a su  C A S A')
    
