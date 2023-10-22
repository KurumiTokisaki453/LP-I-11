# III Actualización y eliminación de registros.
""" 1. Crear 'ejemplo3.db' con tabla alumnos, con:
id clave primaria autoincremental y dni Unico.
"""
import sqlite3

conexion=sqlite3.connect('ejemplo3.db')
cursor=conexion.cursor()

cursor.execute('''
              CREATE TABLE alumnos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre VARCHAR(100),
               edad INTEGER,
               dni VARCHAR(8) UNIQUE,
               correo VARCHAR(100)
              ) ''')

alumnos=[
  ('Leandro',17,'11111111','1lazo@ucsm.edu.pe'),
  ('Delia',16,'22222222','dlazo@ucsm.edu.pe'),
  ('Juan',18,'33333333','jsoto@ucsm.edu.pe'),
  ('Jose',17,'44444444','jcorrales@ucsm.edu.pe')
]
cursor.executemany("INSERT INTO alumnos VALUES (null, ?,?,?,?)",alumnos)
print("1. Tabla alumnos con su clave primaria y DNI unico credo correctamente.")
conexion.commit()
conexion.close()


# 2. Verificar inserción para dato único
# import sqlite3
conexion=sqlite3.connect('ejemplo3.db')
cursor=conexion.cursor()

# cursor.execute("INSERT INTO alumnos VALUES (null, 'Sonia', 19,'11111111','ssalas@ucsm.edu.pe')")
"""
Traceback (most recent call last):
  File "\Actividad03.py", line 33, in <module>
  cursor.execute("INSERT INTO alumnos VALUES (null, 'Sonia', 19,'11111111','ssalas@ucsm.edu.pe')")
  sqlite3.IntegrityError: UNIQUE constraint failed: alumnos.dni
"""
print("2. Error al Ingresar: Fallo por DNI dato único no puede repetirse.")
conexion.commit()
conexion.close()


# 3. Consultar con criterios a tabla alumnos
# import sqlite3
conexion=sqlite3.connect('ejemplo3.db')
cursor=conexion.cursor()

# cursor.execute("SELECT * FROM alumnos WHERE dni='22222222'")
cursor.execute("SELECT * FROM alumnos WHERE edad=17")
alumnos=cursor.fetchall()

print("3. Consultando la tabla alumnos.")
print(alumnos)
conexion.commit()
conexion.close()


# 4. Actualizar el nombre Leandro por Leonardo en tabla alumnos
# import sqlite3
conexion=sqlite3.connect('ejemplo3.db')
cursor=conexion.cursor()

cursor.execute("""UPDATE alumnos
               SET nombre='Leonardo'
               WHERE nombre LIKE 'Leandro'
               """)
print("4. Actualizando el nombre Leando por Leonardo de la tabla.")
conexion.commit()
conexion.close()


# 5. Eliminar el registro dni='44444444'
# import sqlite3
conexion=sqlite3.connect('ejemplo3.db')
cursor=conexion.cursor()

cursor.execute("DELETE FROM alumnos WHERE dni='44444444'")
print("5. Se eliminaron todos los registro con el dni='44444444'")
conexion.commit()
conexion.close()

