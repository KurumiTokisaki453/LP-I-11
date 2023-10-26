import sqlite3
name_db='restaurante.db'
texto="categoria"
def modelo():
  try:    # modelo de conexión de base de datos..
    conexion=sqlite3.connect(name_db)
    cursor=conexion.cursor()
    
    conexion.commit()
    print("Se han creado adecuadamente la Base de datos y las tablas")
  except sqlite3.OperationalError as e:
    print("Error:", e)
  finally:
    conexion.close()

def validar(nombre_tabla,opcion=0):
  lista=[]
  conexion=sqlite3.connect(name_db)
  cursor=conexion.cursor()
  cursor.execute(f"SELECT * FROM {nombre_tabla}")
  todo=cursor.fetchall()
  for i in todo:
    lista.append(i[0])
    
  while True:
    if opcion==0:
      primarykey=int(input("Ingrese id: "))
      if primarykey not in lista:
        conexion.close()
        return primarykey
      else:
        print("El id no puede repetirse.")
    elif opcion==1:
      return lista

def crear_bd():
  try:    # Creación de tabla categoria y plato.
    conexion=sqlite3.connect(name_db)
    cursor=conexion.cursor()

    cursor.execute('''
    CREATE TABLE categoria (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nombre VARCHAR (100) UNIQUE NOT NULL)
                   ''')
    cursor.execute('''
    CREATE TABLE plato (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nombre VARCHAR (100) UNIQUE NOT NULL,
      categoria_id INTEGER NOT NULL,
      FOREIGN KEY (categoria_id) REFERENCES categoria(id))
                   ''')
    conexion.commit()
    print("Se han creado adecuadamente la Base de datos y las tablas")
  except sqlite3.OperationalError as e:
    if "already exists" in str(e):
        print("Las tablas ya existen.")
    else:
        print("Error:", e)
  finally:
    conexion.close()
def agregar_categoria():
  try:
    conexion=sqlite3.connect(name_db)
    cursor=conexion.cursor()
    id_categoria=validar("categoria")
    nombre_cat=input("Ingrese el nombre de la categoria: ")
    cursor.execute(f"INSERT INTO categoria VALUES({id_categoria},'{nombre_cat}')")
    conexion.commit()
    print("Se han creado adecuadamente la Base de datos y las tablas")
  except sqlite3.IntegrityError as e:
    print("Error se ingresó datos repetidos para algun campo UNICO: ",e)
  except sqlite3.OperationalError as e:
    print("Error agregando:", e)
  finally:
    conexion.close()
def mostrar_menu():
  try:
    conexion = sqlite3.connect(name_db)
    cursor = conexion.cursor()

    # consulta para obtener los platos y sus categorías
    cursor.execute('''
        SELECT categoria.nombre, plato.nombre
        FROM categoria
        JOIN plato ON categoria.id = plato.categoria_id
        ORDER BY categoria.nombre, plato.nombre
    ''')

    resultados = cursor.fetchall()

    # Crea un diccionario para organizar los platos por categoría
    platos_por_categoria = {}
    for categoria, plato in resultados:
        if categoria not in platos_por_categoria:
            platos_por_categoria[categoria] = []
        platos_por_categoria[categoria].append(plato)
        
    for categoria, platos in platos_por_categoria.items():
        print(f'▪ {categoria}: {", ".join(platos)}')
    conexion.close()
  except sqlite3.OperationalError as e:
    print("Error mostrando:", e)
def agregar_plato():
  conexion=sqlite3.connect(name_db)
  cursor=conexion.cursor()
  while True:
    lista_categoria=validar("categoria",1)
    cursor.execute("SELECT * FROM categoria")
    categorias=cursor.fetchall()
    for categoria in categorias:
      print(f"{categoria[0]}) {categoria[1]}")
    try:
      seleccionar=int(input("A qué categoría se agregará su plato: "))
      if seleccionar in lista_categoria:
        id_plato=validar("plato")
        nombre_plato=input("Ingrese el nombre de su plato: ")
        cursor.execute(f"INSERT INTO plato VALUES({id_plato},'{nombre_plato}',{seleccionar})")
        conexion.commit()
        conexion.close()
        return f"Se agrego correctamente ({id_plato},{nombre_plato},{seleccionar})"
      else:
        print("El número ingresado no corresponde a ninguna de nuestra categoria.")
    except sqlite3.IntegrityError as e:
      print("Error se ingresó datos repetidos para algun campo UNICO: ",e)
    except sqlite3.OperationalError as e:
      print("Error agregando:", e)
    
  
def menuPrincipal():
  crear_bd()
  while True:
    try:
      print("Bienvenido al menú restaurante.")
      print("1) Crear nueva categoria.")
      print("2) Crear nuevo plato")
      print("3) Mostrar menú.")
      print("x) Salir.")
      seleccion=int(input("Elige su opción: "))
      if seleccion==1:
        print("Agregando nueva categoria")
        agregar_categoria()
      elif seleccion==2:
        print(agregar_plato())
        print("Agregando nuevo plato")
      elif seleccion==3:
        print("Mostrando el menú")
        mostrar_menu()
      elif seleccion=='x':
        print("Terminando programa.")
        break
    except:
      print("Ingrese un valor válido.")
# 
# print("Crear Base de Datos")
# crear_bd()
# print("Crear las categorias.")
# agregar_categoria()
# print("Mostrar el menú.")
# mostrar_menu()
# print("Agregar los platos.")
# agregar_plato()
print("Mostrar el menú principal.")
menuPrincipal()

''' # Ejercicio
Crear propuesto2.py para gestionar los platos de menú de un restaurante.
Desarrolla una función crear_bd() que creará una base de datos restaurante.db con las tablas:

▪ Si ya existieran las tablas tratar la excepción y mostrar que las tablas ya existen.

Caso contrario mostrará un mensaje que se han creado adecuadamente.
---las tablas---
CREATE TABLE categoria (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR (100) UNIQUE NOT NULL)
CREATE TABLE plato (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR (100) UNIQUE NOT NULL,
  categoria_id INTEGER NOT NULL,
  FOREIGN KEY (categoria_id) REFERENCES categoria(id)
    # -- NOTA: La línea FOREIGN KEY (categoria_id) REFERENCES categoria(id) --
    
Indica un tipo de clave especial (foránea), por la cual se crea una relación entre la
categoría de un plato con el registro de categorías.
Llame a la función y compruebe que la base de datos se crea correctamente

▪ Cree función agregar_categoria() que solicite al usuario un nombre de
categoría y crear la categoría en la base de datos
(Si ya existe la categoría, generará un error porque el nombre(categoria) es UNIQUE).

▪ "Bienvenida (saludo)", crear menú de opciones, luego le permita crear una categoría o Salir.
Añadir tres categorías utilizando este menú de opciones:
  ▪ Primeros.
  ▪ Segundos.
  ▪ Postres.

▪ Crear funcion agregar_plato() y muestra las categorías disponibles, y le permita escoger un (submenú).
Luego introducir el nombre del plato y lo añadirá a la base de datos, entendiendo que la categoría del plato
concuerde con el id de la categoría y que el nombre(UNIQUE) no pueda repetirse
(no es necesario comprobar si la categoría realmente existe, en ese caso simplemente no
se insertará el plato).


▪ Crear función mostrar_menu() muestra el menú de todos los platos de forma ordenada: los primeros, los segundos y los postres. 
  ▪ Primeros: Ensalada, Caldo
  ▪ Segundos: Estofado de res, Pollo al horno
  ▪ Postres: Mazamorra Morada, Flan
'''



