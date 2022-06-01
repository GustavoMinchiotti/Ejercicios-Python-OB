# Tema 3 tipos de objetos
'''
Para este ejercicio tenéis que crear un archivo main.py y dentro tienes que crear
variables que representen los siguientes datos de un contacto:


- Nombre
- Apellidos
- Edad
- Email
- Teléfono
- Casado (verdadero o falso)
- Con Hijos (verdadero o falso)
- Lista de amigos
- Películas vistas (diccionario con clave y valor. El valor será el título de la película)

Una vez hayas creado todas las variables, muéstralas por consola haciendo uso de la función print().
'''
nombre = "Gustavo"
apellido= "MMB"
edad= 42
email= "gustavominchiotti@gamil.com"
tel= 5491130150870
casado = True
conHijos = True
lista = ["amigo1","amigo2","amigo3"]
diccionario = {"Movies": "Drácula", "Movies2": "Torrente 1", "Movies3": "Batman"}

estado = 'a'
niños = 'b'

if casado == True:
    estado = "Casado"
else:
    estado = "Soltero y feliz"
    
if conHijos == True:
    niños = "Si, se le acabó la paz"
else:
    niños = "No, vive relajado y tranquilo"
    
#print(nombre,apellido,edad,email,tel,casado,conHijos, lista,(diccionario["Movies"])) #prueba
print("Nombre: ",nombre)
print("Apellido:", apellido)
print("Edad: ", edad)
print("Eamil: ", email)
print("Teléfono: ", tel)
print("Estado civil: ", estado )
print("Tiene hijos: ", niños)
print("Estos son los amigos: ", lista)
print("Vió las siguientes peliculas: ",(diccionario["Movies"]),',',(diccionario["Movies2"])
      ,',',(diccionario["Movies3"]) )
