# Escribe un programa que pregunte al usuario su edad y muestre por pantalla
#  si es mayor de edad o no.

'''necesito imprimir la pregunta escanear la respuesta (para eso, generar
la variable que luego voy a parcear en int), asegurar que es un numero y que
pase el limite de edad establecido.'''

edad = input ('ingrese su edad en numeros por favor:')
edad = int (edad)
print("-"*80)
if edad >=18:
    print("Usted tiene: ",edad,'años y puede beber Cerveza')
else :
    edad < 18    
    print("Usted tiene: ",edad,'años y puede beber Agua')
    

print("-"*80)

# faltaria que si no es un valor aceptable no se rompa y que sean solo positivos.
