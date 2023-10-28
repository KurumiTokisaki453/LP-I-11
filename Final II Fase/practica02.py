"clinica dental"
"""
2.       Desarrollar un proyecto en Python que contemple los siguientes puntos:

Base de Datos

·       Desarrolle el diseño de la Base de Datos asignada.

·       La base de datos por lo menos tres tablas, correctamente relacionadas, uso de claves primarias y secundarias de forma adecuada.

·       Cada tabla debe tener al menos 5 campos cada una.

·       Debe utilizar por lo menos 2 tipos de datos (texto, números, fecha, booleano).


Python

·       Por lo menos tres funciones.
·       Función que cree las tablas en caso no existan.

·       Función menú que contenga el nombre de por lo menos dos tablas, a una tabla debe permitir insertar, consultar, eliminar y actualizar registros de cada tabla.

·       Hacer uso de un módulo para las validaciones en el registro de información (antes de realizar el insertar, actualizar).

·       Agregar una opción en el menú con el nombre consulta, donde les permita seleccionar entre al menos 2 consultas diferentes que guarden relación con la base de datos seleccionada.

·       Luego de mostrar los resultados de la consulta se debe dar la opción de guardar los resultados en un archivo txt.

·       Agregar una opción en el menú con el nombre exportar que permita exportar una tabla de la base de datos a un archivo txt o pickle.

·       Su proyecto debe incluir el manejo de excepciones.
"""

import sqlite3
import validaciones
from datetime import datetime

name_db='clinica_dental.db'

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
      conexion.close()
      return lista
    elif opcion==2:
      primarykey=int(input("Ingrese id: "))
      if primarykey in lista:
        conexion.close()
        return primarykey
def crear_bd():
  try:
    conexion=sqlite3.connect(name_db)
    cursor=conexion.cursor()
    # Tablas maestras
    cursor.execute('''
    CREATE TABLE pacientes (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nombre VARCHAR (100) NOT NULL,
      apellido VARCHAR (100) NOT NULL,
      nacimiento DATE,
      direccion TEXT,
      telefono int,
      correo_electronico TEXT)
                   ''')
    cursor.execute('''
      CREATE TABLE dentistas (
        id_dentistas INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR (100) NOT NULL,
        apellido VARCHAR (100) NOT NULL,
        nacimiento DATE,
        direccion TEXT,
        telefono int,
        correo_electronico TEXT)
                   ''')
    # Tablas transaccional
    cursor.execute('''
    CREATE TABLE citas (
      id_cita INTEGER PRIMARY KEY AUTOINCREMENT,
      id_paciente INTEGER NOT NULL,
      fecha_cita DATE NOT NULL,
      hora INTEGER (2) NOT NULL,
      tipo_cita VARCHAR (50) NOT NULL,
      id_dentista INTEGER NOT NULL,
      FOREIGN KEY (id_paciente) REFERENCES pacientes(id),
      FOREIGN KEY (id_dentista) REFERENCES dentistas(id_dentistas)
        )''')
    conexion.commit()
    print("Se han creado adecuadamente la Base de datos y las tablas")
  except sqlite3.OperationalError as e:
    if "already exists" in str(e):
        print("Las tablas ya existen.")
    else:
        print("Error:", e)
  finally:
    conexion.close()
def agregar_usuarios(nombre_tabla):
  try:
    conexion=sqlite3.connect(name_db)
    cursor=conexion.cursor()
    # Ingresando datos
    primaryKey=validar(nombre_tabla,1)
    if primaryKey !=[]:
      primaryKey=max(primaryKey)+1
    else:
      primaryKey=1
    nombre_usuario=input("Ingrese el nombre: ")
    apellido_usuario=input("Ingresar el apellido: ")
    nacimiento=validaciones.validarFecha()
    direccion=input("Ingrese su dirección: ")
    telefono=validaciones.telefonovalidar()
    correo=input("Ingrese su correo electrónico: ")

    cursor.execute(f"""INSERT INTO {nombre_tabla}
                   VALUES ({primaryKey},'{nombre_usuario}', '{apellido_usuario}',
                   '{nacimiento}','{direccion}','{telefono}','{correo}'
                   )""")
    conexion.commit()
    print("Se han creado adecuadamente la Base de datos y las tablas")
  except sqlite3.IntegrityError as e:
    print("Error se ingresó datos repetidos para algun campo UNICO: ",e)
  except sqlite3.OperationalError as e:
    print("Error agregando:", e)
  finally:
    conexion.close()
def mostrar_tablas(nombre_tabla,seleccion=1):
  try:
    listaExportacion=[]
    conexion=sqlite3.connect(name_db)
    cursor=conexion.cursor()
    print("")
    print(f"----------Mostrar {nombre_tabla}----------")
    if seleccion==1:
      cursor.execute(f"""SELECT * FROM {nombre_tabla}""")
      resultados = cursor.fetchall()
      for result in resultados:
        exportar=(f"""ID {nombre_tabla}: {result[0]}\nNombre: {result[1]}\nApellido: {result[2]}\nFecha Nacimiento: {result[3]}\nDirección: {result[4]}\nTelefono: {result[5]}\nCorreo: {result[6]}""")
        listaExportacion.append(exportar)


    elif seleccion==2:
      cursor.execute(f"""SELECT citas.id_cita, pacientes.nombre, citas.fecha_cita, citas.hora, citas.tipo_cita, dentistas.nombre
                     FROM citas
                     INNER JOIN pacientes ON citas.id_paciente = pacientes.id
                     INNER JOIN dentistas ON citas.id_dentista = dentistas.id_dentistas
                     """)
      resultados=cursor.fetchall()
      for result in resultados:
        exportar=(f"""ID Citas: {result[0]}\nNombre del Paciente: {result[1]}\nHora y Fecha: {result[3]}:00 UTC - {result[2]}\nTipo de Cita: {result[4]}\nNombre del Dentista: {result[5]}""")
        listaExportacion.append(exportar)
    conexion.commit()
    for x in listaExportacion:
      print(x)
    print("------------------------------------")
    return listaExportacion
  except sqlite3.IntegrityError as e:
    print("Error se ingresó datos repetidos para algun campo UNICO: ",e)
  except sqlite3.OperationalError as e:
    print("Error mostrando:", e)
  finally:
    conexion.close()
def foreingKey(nombre_tabla, imprimir):
    lista_pacientes=validar(nombre_tabla,1)
    while True:
      try:
        nombre_usuario=int(input(f"Ingrese id {imprimir}: "))
        if nombre_usuario in lista_pacientes:
          return nombre_usuario
        else:
          print(f"'{nombre_tabla}' no tiene el id ingresado.")
      except ValueError:
        print("Error: ingrese un valor válido.")
def agregar_citas():
  try:
    conexion=sqlite3.connect(name_db)
    cursor=conexion.cursor()
    nombre_tabla="citas"
    # Ingresando datos
    primaryKey=validar(nombre_tabla,1)
    if primaryKey !=[]:
      primaryKey=max(primaryKey)+1
    else:
      primaryKey=1
      
    id_paciente=foreingKey("pacientes","Paciente")
    fecha_cita=validarFecha()
    hora_cita=validaciones.validarHora()
    tipo_cita=input("Ingrese el motivo de la cita: ")
    id_dentista=foreingKey("dentistas","Dentista")

    cursor.execute(f"""INSERT INTO {nombre_tabla}
                   VALUES ({primaryKey},'{id_paciente}', '{fecha_cita}',
                   '{hora_cita}','{tipo_cita}','{id_dentista}'
                   )""")
    conexion.commit()
    print("Se han creado adecuadamente la Base de datos y las tablas")
  except sqlite3.IntegrityError as e:
    print("Error se ingresó datos repetidos para algun campo UNICO: ",e)
  except sqlite3.OperationalError as e:
    print("Error agregando:", e)
  finally:
    conexion.close()
def eliminar(nombre_tabla):
  try:
    conexion=sqlite3.connect(name_db)
    cursor=conexion.cursor()
    
    id_eliminar=validar(nombre_tabla,2)
    cursor.execute(f"DELETE FROM {nombre_tabla} WHERE id = {id_eliminar}")
    
    conexion.commit()
  except sqlite3.IntegrityError as e:
    print("Error se ingresó datos repetidos para algun campo UNICO: ",e)
  except sqlite3.OperationalError as e:
    print("Error mostrando:", e)
  finally:
    conexion.close()

def menuPrincipal():
  crear_bd()
  while True:
    try:
      print("Bienvenido a la Clinica Dental.")
      print("1) Registrar nuevos registros")
      print("2) Consultar Registros")
      print("3) Eliminar Registros")
      print("4) Actualizar")
      print("7) Salir.")
      seleccion=int(input("Elige su opción: "))
      if seleccion==1:
        print("1) Agregar nuevo paciente.")
        print("2) Agregar nuevo dentista")
        print("3) Agregar nueva cita")
        submenu=int(input("Elige su opción: "))
        if submenu==1:
          agregar_usuarios("pacientes")
        elif submenu==2:
          agregar_usuarios("dentistas")
        elif submenu==3:
          agregar_citas()
      elif seleccion==2:
        print("1) Mostrar todos los pacientes")
        print("2) Mostrar todos los docentes")
        print("3) Mostrar todoas las citas")
        print("4) Mostrar todas las tablas")
        print("5) Regresar opción")
        submenu=int(input("Elige su opción: "))
        if submenu==1:
          texto=mostrar_tablas("pacientes")
        elif submenu==2:
          texto=mostrar_tablas("dentistas")
        elif submenu==3:
          texto=mostrar_tablas("citas",2)
        elif submenu==4:
          texto1=mostrar_tablas("pacientes")
          texto2=mostrar_tablas("dentistas")
          texto3=mostrar_tablas("citas",2)
          texto=str(texto1)+str(texto2)+str(texto3)
        elif submenu==5:
          print("Saliendo a menú principal")
        print("¿Guardar consulta en un archivo txt?")
        print("1) Si\n2) NO")
        guardartxt=int(input("Elige su opción: "))
        if guardartxt==1:
          print("Guardando")
          validaciones.ArchivoTxt(str(texto))
        elif guardartxt==2:
          print("No se guardó ninguna consulta")
      elif seleccion==3:
        print("1) Eliminar un Registro de pacientes")
        print("2) Eliminar un registro de dentistas")
        print("3) Eliminar un registro de citas")
        print("4) No eliminar ningún registro.")
        submenu=int(input("Elige su opción: "))
        if submenu==1:
          eliminar("pacientes")
        elif submenu==2:
          eliminar("dentistas")
        elif submenu==3:
          eliminar("citas")
        else:
          print("No se eliminó ningún registro.")
      elif seleccion==7:
        break
      elif seleccion==8:
        mostrar_tablas("pacientes")
        mostrar_tablas("dentistas")
        mostrar_tablas("citas",2)

        
    except:
      print("Ingrese un valor válido.")

print("Mostrando el menú principal.")
menuPrincipal()
