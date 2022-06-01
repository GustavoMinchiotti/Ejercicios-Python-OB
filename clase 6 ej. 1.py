# Clases // clase 6 ejercicio 1
'''En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
    Color
    Ruedas
    Puertas
Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
    Velocidad
    Cilindrada
Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.'''

class Vehiculo:
    color = None
    ruedas = 4
    puertas = 4

class Coche (Vehiculo):
    velocidad = 0
    cilindrada = 3000

print(Coche) # clase
c = Coche() # objeto
print(c)

# muestro todas las variables

print(c.color)
print(c.ruedas)   
print(c.puertas)
print(c.velocidad)
print(c.cilindrada)
