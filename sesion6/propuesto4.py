'''
4. Crear propuesto4.py que muestre los datos de la colección de objetos tareas
que se volcaron en el archivo pickle en el ejercicio anterior.
'''
import pickle

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

tarea0=Tarea("Test","01-01-2000","Finalizado")

lista=[]
try:
    with open(nombre_pickle, "rb") as archivo:
      oldlista = pickle.load(archivo)
      lista=list(oldlista)
    print("Terminando de leer los archivos existentes.")
except FileNotFoundError:
  with open(nombre_pickle, "wb") as archivo:
    lista=[]
    print("Se creó nueva 'tareas.pkl'.")
except IOError as e:
    print(f"Error de E/S al trabajar: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")
    
print("----------Mostrando Elementos de la lista----------")
if len(lista)!=0:
  tarea0.listar()
else:
  print("\nNo tiene Tareas.\n")
print("--------------------------------------------")