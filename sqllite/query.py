import sqlite3

conexion = sqlite3.connect("test2.db")
cursor = conexion.cursor()

cursor.execute("select * from users2 where dni = 1")

user = cursor.fetchone()
print(user)

conexion.commit()
conexion.close()