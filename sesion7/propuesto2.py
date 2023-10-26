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
      print("4) Salir.")
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
      elif seleccion==4:
        print("Terminando programa.")
        break
    except:
      print("Ingrese un valor válido.")

print("Mostrando el menú principal.")
menuPrincipal()
