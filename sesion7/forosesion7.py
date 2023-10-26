# banco
import sqlite3
name_db='banco.db'
conexion=sqlite3.connect(name_db)
cursor=conexion.cursor()
# 3 tablas, agregar, eliminar, modificar, listar
cursor.execute('''
CREATE TABLE clientes (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  nombre VARCHAR (100) NOT NULL,
  apellido VARCHAR (100),
  saldo INTEGER)
               ''')
cursor.execute('''
CREATE TABLE banco (
  idbanco INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  nombre VARCHAR (100) NOT NULL,
  numclientes INTEGER,
  clientes_id INTEGER,
  FOREIGN KEY (clientes_id) REFERENCES clientes(id))
               ''')
cursor.execute('''
CREATE TABLE sistema_financiero (
  idsistem INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  nombre VARCHAR (100) NOT NULL,
  clientes_id INTEGER,
  bancos_id INTEGER,
  FOREIGN KEY (bancos_id) REFERENCES banco(idbanco),
  FOREIGN KEY (clientes_id) REFERENCES clientes(id))
               ''')
print("Agregar clientes.")
cursor.execute("INSERT INTO clientes (nombre, apellido, saldo) VALUES (?, ?, ?)", ("Juan", "Pérez", 500))
cursor.execute("INSERT INTO clientes (nombre, apellido, saldo) VALUES (?, ?, ?)", ("María", "López", 750))
cursor.execute("INSERT INTO clientes (nombre, apellido, saldo) VALUES (?, ?, ?)", ("Carlos", "Gómez", 1000))
print("----------------Mostrar clientes----------------")
cursor.execute("SELECT * FROM clientes")
clientes=cursor.fetchall()
for cliente in clientes:
  print(f"Id: {cliente[0]}\nNombre: {cliente[1]}\nApellido: {cliente[2]}\nSaldo: {cliente[3]}")
print("*******Borrar clientes*********")
cursor.execute("DELETE FROM clientes WHERE id = ?", (2,))
print("----------------Mostrar clientes----------------")
cursor.execute("SELECT * FROM clientes")
clientes=cursor.fetchall()
for cliente in clientes:
  print(f"Id: {cliente[0]}\nNombre: {cliente[1]}\nApellido: {cliente[2]}\nSaldo: {cliente[3]}")

conexion.close()