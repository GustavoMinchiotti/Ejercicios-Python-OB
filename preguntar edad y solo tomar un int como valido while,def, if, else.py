edad = input("Ingrese su edad: ")

def tomador (edad):
    "calcula si es tomador"
    if edad >=18:
        print('Usted tiene: ',edad,' años y puede beber Cerveza')
    else:
        edad < 18    
        print("Usted tiene: ",edad,'años y puede beber Agua')

# Trying to convert the input to an integer. If it can't, it will set the variable `es` to `False`.
try:
    int(edad)
    es = True
    edad = int(edad)
    print("-"*80)
    tomador(edad)
    print("-" * 80)
except ValueError:
    es = False
#print(es)

# It's a loop that will keep asking for an input until the user enters a number.
while es == False:
    print("el valor debe ser un numero")
    edadLoop = input("Ingrese su edad: ")
    try:
        int(edadLoop)
        si = True
        edadLoop = int(edadLoop)
        print('transformado exitoso')
        tomador(edadLoop)
        break
    except ValueError:
        print('solo numeros enteros')