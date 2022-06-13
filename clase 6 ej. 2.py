# Clases // clase 6 ejercicio 2
'''En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno
que tenga como atributos su nombre y su nota.
Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje
con el resultado de la nota y si ha aprobado o no.'''


class Alumno():
    nombre = 'Juan'
    nota = 0

    def calificacion(nota):
        """ Saber si aprueba o no la materia"""
        if nota <= 6:
            print(Alumno.nombre, ' No aprueba')
        else:
            print(Alumno.nombre, ' aprobado')


class Alumno2():

    def __init__(self, nombre, nota):
        self.nombre = nombre  # digo al constructor que tome el parametro
        self.nota = nota
        self.resultado = 0

    def califica(self):
        """ Saber si aprueba o no la materia"""
        res = self.resultado + self.nota
        if res <= 6:
            print('No aprueba')
        elif res == 10:
            print('Excelente')
        else:
            print('aprueba')


a1 = Alumno2('Jaimito', 3)
a2 = Alumno2('Wolfgang', 10)
a3 = Alumno2('Charo', 9)
print(a1.nombre, a1.nota)  # muy importante pasar objeto + . + parametro

print('*-**-*-*' * 10)

print('Alumno: ', a1.nombre, '\nNota: ', a1.nota)
a1.califica()  # llamo a la funcion

print('*-**-*-*' * 10)

print('Alumno: ', a2.nombre, '\nNota: ', a2.nota)
a2.califica()

print('*-**-*-*' * 10)

print('Alumno: ', a3.nombre, '\nNota: ', a3.nota)
a3.califica()
