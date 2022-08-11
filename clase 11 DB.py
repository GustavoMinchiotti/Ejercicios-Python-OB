import getpass
import sqlite3


def main():
    """
    usuario = input('Nombre de usuario: ')
    clave = getpass.getpass('Contraseña: ')

    if verifica_credenciales(usuario, clave):
        print('Logging correcto')
    else:
        print('Logging incorrecto')


def verifica_credenciales(usuario, clave):
    conn = sqlite3.connect('clase11.sqlite')
    cursor = conn.cursor()

    query = f"SELECT id FROM prueba WHERE username ='{usuario}' AND pass = '{clave}'"
    print('query a ejecutar: ', query)

    rows = cursor.execute(query)

    data = rows.fetchone()
    print('data es ', type(data))
    cursor.close()
    conn.close()
"""


# This is a common pattern in Python. It allows you to run the main function of your program by running the script,
# but it also allows you to import the script and call the main() function yourself.
if __name__ == '__main__':
    main()

"""
conn = sqlite3.connect('clase11.sqlite')
cursor = conn.cursor()

rows = cursor.execute('SELECT * FROM prueba WHERE username = "Charo"')
for row in rows:
    print(row)

cursor.close()
conn.close()
# 'CREATE TABLE alumnos (id INTEGER PRIMARY KEY, nombre TEXT NOT NULL, apellido TEXT NOT NULL);'
"""
conn = sqlite3.connect('clase11.sqlite')
cursor = conn.cursor()

query = '''INSERT INTO alumnos(id, nombre, apellido) VALUES(?,"?","?");'''
rows = cursor.execute(query, (3, 'Ind', 'Ste'))

conn.commit()
cursor.close()
conn.close()
