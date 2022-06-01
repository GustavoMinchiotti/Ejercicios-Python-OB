# Escribe una función que pueda decirte si un número
# (número entero) es primo o no.
# https://medium.com/@eddydecena/validando-si-un-n%C3%BAmero-es-primo-en-python-a622cf6b4363

def isPrime(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


resultado= isPrime(8)

if resultado == True:
    print("es primo")
else:
    print("no es primo")

# print(resultado)

'''no lo entendia y lo googlee'''
