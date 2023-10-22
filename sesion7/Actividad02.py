# II Clave primaria y sus restricciones.
# 1. Crear en Python una base de datos "ejemplo2.db" y tabla alumnos con clave primaria.
import sqlite3
conexion=sqlite3.connect('ejemplo2.db')
cursor=conexion.cursor()

cursor.execute('''
              CREATE TABLE alumnos (
                id VARCHAR(4) PRIMARY KEY,
                nombre VARCHAR(100),
                edad INTEGER,
                correo VARCHAR(100)
               )''')
alumnos=[
  (1000,'Leandro',17,'qlazo@ucsm.edu.pe'),
  (1001,'Delia',17,'dlazo@ucsm.edu.pe'),
  (1002,'Juan',18,'jsoto@ucsm.edu.pe'),
  (1003,'Jose',17,'jcorrales@ucsm.edu.pe')
]

cursor.executemany("INSERT INTO alumnos VALUES (?,?,?,?)",alumnos)
print("1. Base de datos y tabla creados en 'ejemplo2.db'.")
conexion.commit()
conexion.close()


# 2. Verificar inserción sin repetirse el dato clave primaria.
# import sqlite3
conexion=sqlite3.connect('ejemplo2.db')
cursor=conexion.cursor()

# cursor.execute("""INSERT INTO alumnos VALUES
              #  (1000,'Leandro',17,'1lazo@ucsm.edu.pe')
              #  """)
'''Traceback (most recent call last):
  File "\Actividad02.py", line 29, in <module>
  cursor.execute("""INSERT INTO alumnos VALUESsqlite3.IntegrityError: UNIQUE constraint failed: alumnos.id'''
print("2. Error Clave Primaria: 'UNIQUE constraint failed: alumnos.id'")
conexion.commit()
conexion.close()


# 3. Agregar tabla productos con campo incremental y sea clave primaria.
# import sqlite3
conexion=sqlite3.connect('ejemplo2.db')
cursor=conexion.cursor()

cursor.execute('''
              CREATE TABLE productos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre VARCHAR (100) NOT NULL,
               marca VARCHAR(50) NOT NULL,
               precio FLOAT NOT NULL
              ) ''')
print("3. Tabla productos con Clave primaria Agregados correctamente.")
conexion.commit()
conexion.close()


# 4. Insertar 3 registro en productos desde Python.
# import sqlite3
conexion=sqlite3.connect('ejemplo2.db')
cursor=conexion.cursor()

productos= [
  ('Teclado','Genius',18.99),
  ('Ratón', 'Genius',12.99),
  ('Pantalla','LG',1250.00)
]

cursor.executemany("INSERT INTO productos VALUES (null, ?,?,?)", productos)
print("4. 3 Registros ingresados correctamente a tabla productos.")
conexion.commit()
conexion.close()


# 5. Retornar n registros de tabla productos de sqlite a Python.
# import sqlite3

conexion=sqlite3.connect('ejemplo2.db')
cursor=conexion.cursor()

cursor.execute("SELECT * FROM productos")

productos= cursor.fetchall()
print("{:<4} | {:<13} | {:<13} | {:<10}".format("ID","Nombre", "Marca", "Precio"))
print("-" * 48)
for product in productos:
  print("{:<4} | {:<13} | {:<13} | {:<10}".format(
    product[0],
    product[1],
    product[2],
    product[3]))
print("5. Se mostró toda la tabla registrada en productos.")
conexion.commit()
conexion.close()
