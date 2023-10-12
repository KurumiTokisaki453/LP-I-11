''' 
3. Crear propuesto3.py, serialice una colección de tres objetos de la clase tarea
tener atributos: descripción, fecha de vencimiento y estado (pendiente o finalizada).

Contará con los métodos agregar tarea, completar tarea, listar tareas.
Vuelque la información en un archivo pickle.
'''
import os
import pickle

conjunto=[]

def fechautil():
  vencimiento=input("Ingrese la Fecha de vencimiento de su Tarea: ")
  return vencimiento

def estadoutil():
  estado=""
  while (estado.lower())!="pendiente" and (estado.lower())!="finalizado":
    try:
      print("La tarea solo puede estar en 'Pendiente' o 'Finalizado'")
      estado=input("¿El estado de su Tarea?: ")
    except:
      print("Ingrese un Valor válido.")
  return estado

nombre_pickle = "tareas.pkl" #Nombre del archivo

class Tarea:
  def __init__(self,descripcion,vencimiento,estado):
    self.descripcion=descripcion
    self.vencimiento=vencimiento
    self.estado=estado[0].upper() + estado[1:].lower()
  
  def agregar(self):
    lista.append(self)
  
  def completar(self):
    if self.estado.lower()=="pendiente":
      self.estado="Finalizado"
    else:
      print("Su tarea ya está Finalizada")

  def listar(self):
    print("Lista de tareas:")
    for i,tarea in enumerate(lista):
      print(f"\nTarea {i}:\n{str(tarea)}")
  
  def getEstado(self): return self.estado.lower()
  def getTarea(self): return self.descripcion
            
  def __str__(self):
    return f"Descripción: {self.descripcion}\nFecha de Vencimiento: {self.vencimiento}\nEstado: {self.estado}"
    
lista=[]
try:
    with open(nombre_pickle, "rb") as archivo:
      oldlista = pickle.load(archivo)
      lista=list(oldlista)
  # else:
  #   lista=[]
    print("Terminando de leer los archivos existentes.")
except FileNotFoundError:
  with open(nombre_pickle, "wb") as archivo:
   lista=[]
except IOError as e:
    print(f"Error de E/S al trabajar: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")
print(f"Mi lista es: {lista} con typo {type(lista)}")

def leerPendientes():
  print(f"Seleccione de que Tarea quiere completar:")
  for i,tarea in enumerate(lista):
    if tarea.getEstado()=="pendiente":
      print(f"Tarea N°: {i}\nDescripción: {tarea.getTarea()}\n")
      conjunto.append(i)
  
tarea0=Tarea("Test","01-01-2000","Finalizado")

def menuPrincipal():
  while True:
    try:
      print("----------------Menú----------------")
      print("1) Agregar.")
      print("2) Completar.")
      print("3) Listar.")
      print("4) Salir.")
      seleccionar=int(input("Ingrese la opción deseada: "))
      if seleccionar==1:
        descripcion=input("Ingrese la descripción de su Tarea: ")
        opcion1=Tarea(descripcion,fechautil(),estadoutil())
        opcion1.agregar()
        print("Se agrego correctamente su Tarea.")
        
      elif seleccionar==2:
        if len(lista)!=0:
          leerPendientes()
          if len(conjunto)!=0:
            eligir=-2
            while eligir not in conjunto:
              try: 
                eligir=int(input("Seleccione el N° de su tarea a completar: "))
                if eligir in conjunto:
                  lista[eligir].completar()
                  conjunto.remove(eligir)
                  print("La tarea se completó.")
                  break
                elif eligir==-1:
                  print("Ninguna Tarea pendente se completó.")
                  break
                else:
                  print("Tarea no encontrada...")
                  leerPendientes()
              except ValueError:
                print("Error: Seleccione un número de la lista de Tareas.")
          else:
            print("No tiene tareas Pendientes")
        else:
          print("\nNo tiene ninguna tarea.\n")
          
      elif seleccionar==3:
        print("----------Mostrando Elementos de la lista----------")
        if len(lista)!=0:
          tarea0.listar()
        else:
          print("\nNo tiene Tareas.\n")
        print("--------------------------------------------")

      elif seleccionar==4:
        with open(nombre_pickle, "wb") as archivo:
            pickle.dump(lista, archivo)

        print(f"Los datos han sido guardados en {nombre_pickle}.")
        print("Terminando el Programa.")
        break
      elif seleccionar==5:
        with open(nombre_pickle, "rb") as archivo:
            newlista = pickle.load(archivo)
        for tarea in newlista:
            print(tarea)
    except:
      print("Error en el programa")
menuPrincipal()