import getpass
import sqlite3


def main():
    """
    It prompts the user for a username and password, and then checks if the username and password are valid
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
    rows = cursor.execute(f'SELECT id FROM prueba WHERE username = {usuario} AND pass = {clave}')
    data = rows.fetchone()
    print('data es ', type(data))
    cursor.close()
    conn.close()


# This is a common pattern in Python. It allows you to run the main function of your program by running the script,
# but it also allows you to import the script and call the main() function yourself.
if __name__ == '__main__':
    main()

'''
conn = sqlite3.connect('clase11.sqlite')
cursor = conn.cursor()

rows = cursor.execute('SELECT * FROM prueba WHERE username = "Charo"')
for row in rows:
    print(row)

cursor.close()
conn.close()
'''