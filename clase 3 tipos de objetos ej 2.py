# tema 3 ej 2
''' Escribe un programa en la consola de python que pida al usuario su peso
(en kg) y estatura (en metros), calcule el índice de masa corporal y lo
almacene en una variable, e imprima por pantalla la frase
Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal
calculado redondeado con dos decimales.'''

''' El IMC es su peso en kilos divido por la altura (estatura) al cuadrado.

IMC = Peso (kg) / altura (m)2

Ejemp​lo:
Altura: 165 cm (1,65 m).

Peso: 68 kg

Cálculo: 68 ÷ 1,652 (2,7225) = 24,98 '''

peso = input ("Tu peso en kilos: ")
altura = input ("Tu altura en centímetros: ")
peso = float (peso) # lo fuerzo a float
altura = int (altura) 
altura = altura / 100 # Convierto a mts. porque es mas facil para el usuario
imc = peso / (altura * altura)

print ("Su índice de masa corporal <IMC> es %.2f" %imc)

