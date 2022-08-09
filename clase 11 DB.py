import sqlite3
conn = sqlite3.connect('clase11.sqlite')
cursor = conn.cursor()

rows = cursor.execute('SELECT * FROM prueba')
for row in rows:
    print(row)

cursor.close()
conn.close()
