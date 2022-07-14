# En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que
# contenga un botón de reinicio para que deje todo como al principio.
# Al principio no tiene que haber una opción seleccionada.

# En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos
# seleccionables, también debe de tener un label con el texto que queráis.
import tkinter

# creo una ventana
from tkinter import ttk

window = tkinter.Tk()
'''
label_saludo = tkinter.Label(window, text='hola', bg='yellow', fg='blue')  # creo, formateo y nombro una etiqueta
label_saludo.pack(ipadx=50, ipady=10, fill='x')  # le asigno un tipo de geometría más 50 px hacia cada lado a partir
# del texto

label_adios = tkinter.Label(window, text='adios', bg='red', fg='white')  # creo, formateo y nombro una etiqueta
label_adios.pack(ipadx=50, ipady=10, fill='both')  # con fill rellena según el tamaño de la ventana

window.mainloop()'''


def resetear(event):
    print('a 0 nuevamente')


seleccionado = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text='Si', value='1', variable=seleccionado)
# text es el texto del radiobutton // value es el valor que se le asigna a nivel interno // variable es la var donde
# se almacena ese valor (se crea de una manera especial, con la sintaxis: seleccionado = tkinter.StringVar())
r2 = ttk.Radiobutton(window, text='No', value='2', variable=seleccionado)
r3 = ttk.Radiobutton(window, text='Quizá', value='3', variable=seleccionado)
r4 = tkinter.Button(window, text='reset', textvariable=seleccionado)


r1.grid(column=0, row=1, padx=5, pady=5)
r2.grid(column=0, row=2, padx=5, pady=5)
r3.grid(column=0, row=3, padx=5, pady=5)
r4.grid(column=3, row=4, padx=5, pady=5)

window.mainloop()
