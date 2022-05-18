import sqlite3

conexion = sqlite3.connect('test2.db')
cursor = conexion.cursor()

# cursor.execute("""
#     CREATE TABLE users2 (
#         dni VARCHAR(10) PRIMARY KEY,
#         name VARCHAR(100) ,
#         edad INTEGER , 
#         email VARCHAR(100)
#     )
# """)

# users = [
#     ('12314' ,'Edwar C' , 23 , 'edwar@gmail.com'),
#     ('147852','Camilo D' , 19 , 'cami@gmail.com'),
#     ('123654' ,'Katherine C' , 32 , 'kae@gmail.com')
# ]
# try:
#     cursor.executemany("INSERT INTO users2 values (?,?,?,?)", users)
# except Exception as e:
#     print(type(e).__name__)
#     print("Parece que los datos no se almacenaron")
# finally:
#     print("Verifica los datos y vuelve a intentar el registro")


# cursor.execute("""
#     CREATE TABLE products (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         product VARCHAR(100) not null,
#         marca VARCHAR(50) not null,
#         price FLOAT not null
#     )
# """)


# cursor.execute("insert into products values (null ,'Camara fotografica' , 'Cannon', 1500)")
# product = ('Camara fotografica' , 'Cannon', 1500)

conexion.commit()
conexion.close()