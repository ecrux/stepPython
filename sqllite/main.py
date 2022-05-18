
import sqlite3

conexion = sqlite3.connect("test.db")
cursor = conexion.cursor()

# cursor.execute("CREATE TABLE users ( name VARCHAR(100), yeard INTEGER , email VARCHAR(100) )")

#cursor.execute("INSERT INTO users  VALUES('Nala Cruz', 5, 'nalalamejor@gmail.com')")

# users = [
#     ('Edwar C' , 23 , 'edwar@gmail.com'),
#     ('Camilo D' , 19 , 'cami@gmail.com'),
#     ('Katherine C' , 32 , 'kae@gmail.com')
# ]
# cursor.executemany("INSERT INTO users VALUES (? , ?, ?)", users)

cursor.execute("select * from users")
users = cursor.fetchall()
for u in users:
    print(u)


conexion.commit()
conexion.close()