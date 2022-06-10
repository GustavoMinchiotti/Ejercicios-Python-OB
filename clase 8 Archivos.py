# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt,
# lo abráis y escribáis dentro del archivo.
# Para ello, tendréis que acceder dos veces al archivo creado.

'''voy a crear el archivo desde esta misma ventana y lo voy a escribir'''

'''arch=open('archClase8.txt','w')
contenido='este archivo es un ejemplo de manejo de archivos justamente'
arch.write(contenido + '\n')


arch.close
print(contenido)'''

# Escribimos 5 letras ----este metodo funciona pero no sin el while----
'''
while n<5:
    texto=input('Dame un texto ')
    archivo.write(texto+'\n') #con esta funcion escribe una letra por linea.
    n=n+1
    '''

# Con este metodo no explicado en Nicosio tuve el resultado esperado

arch= 'archClase8.txt'
with open(arch,'w') as archivo:
    archivo.write('este archivo es un ejemplo de manejo de archivos justamente,lo obtuve de: https://www.youtube.com/watch?v=lwZidFVrV9A')
archivo.close    
    
