# 1. Conexión a SQlite y crear la base de datos ejemplo1.db
import sqlite3
conexion = sqlite3.connect('ejemplo1.db')
conexion.close()

# 2. Crear tabla alumnos en la base de datos creada.
# import sqlite3
conexion = sqlite3.connect('ejemplo1.db')
cursor =conexion.cursor()
cursor.execute('''CREATE TABLE alumnos (
              nombre VARCHAR(100),
              edad INTEGER,
              correo VARCHAR(100)
               )''')
conexion.close()
# 3. Crear un registro en la tabla alumnos
# import sqlite3
conexion = sqlite3.connect('ejemplo1.db')
cursor =conexion.cursor()
cursor.execute('''INSERT INTO alumnos values (
               'Leandro',
               17,
               '1Campos@ucsm.edu.pe'
              )''')
conexion.commit()
conexion.close()
# 4. Mostrar el primer registro de la tabla alumnos.
# import sqlite3
conexion = sqlite3.connect('ejemplo1.db')
cursor =conexion.cursor()
cursor.execute("SELECT * FROM alumnos")

print(cursor)
primer_alumno=cursor.fetchone()
primer_alumno=('Leandro', 17, '1Campos@ucsm.edu.pe')
print(primer_alumno)
print("{:<14} | {:<7} | {:<20}".format("Nombre", "Edad", "Correo"))
print("-" * 48)
print("{:<14} | {:<7} | {:<20}".format(primer_alumno[0],primer_alumno[1],primer_alumno[2]))
print("-" * 48)
conexion.close()
# 5. Insertar n registros desde la Python
# import sqlite3
conexion = sqlite3.connect('ejemplo1.db')
cursor =conexion.cursor()
alumnos= [
  ('Delia',16,'dlazo@ucsm.edu.pe'),
  ('Juan',18,'jsoto@ucsm.edu.pe'),
  ('Jose',17,'jcorrales@ucsm.edu.pe')
]
cursor.executemany("INSERT INTO alumnos VALUES (?,?,?)", alumnos)
conexion.commit()
conexion.close()

# 6 Retornar n registros desde SQlite a Python
# import sqlite3
conexion = sqlite3.connect('ejemplo1.db')
cursor =conexion.cursor()
cursor.execute("SELECT * FROM alumnos")
alumnos=cursor.fetchall()
print(alumnos)
print("-" * 48)
print("{:<14} | {:<7} | {:<20}".format("Nombre", "Edad", "Correo"))
print("-" * 48)
for alumn in alumnos:
  print("{:<14} | {:<7} | {:<20}".format(alumn[0],alumn[1],alumn[2]))

conexion.close()
