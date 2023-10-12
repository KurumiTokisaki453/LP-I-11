#Serialización de objetos con pickle
'''
1. Realizar la creación de una clase Vehículo,
crear tres objetos y escribir en un archivo pickle,
luego leerlo e imprimir por pantalla.
'''
import pickle
class Vehiculo():
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo
    self.enmarcha = False
    self.acelera = False
    self.frena = False

  def arrancar(self):
    self.enmarcha = True
  def acelerar(self):
    self.acelera = True
  def frenar(self):
    self.frena = True 

  def estado(self):
    estado_str = "Marca: "+self.marca+      \
    "\nModelo: "+self.modelo +             \
    "\nEn marcha: " + str(self.enmarcha) + \
    "\nAcelerando: " + str(self.acelera) + \
    "\nFrenando: " + str(self.frena) +     \
    "\n----------------------------------"
    return estado_str
#Creamos tres objetos de la clase Vehiculo
auto1=Vehiculo("Honda","CRV")
auto2=Vehiculo("Toyota","Yaris")
auto3=Vehiculo("Nissan","Sentra")
#Colección de objetos
autos=[auto1,auto2,auto3]

#Escribimos en el archivo binario la colección de objetos
archivo_binario=open("actividad5.pckl","wb")
pickle.dump(autos,archivo_binario)
archivo_binario.close()
del(archivo_binario)

#Leemos del archivo binario la colección de objetos
archivo_apertura=open("actividad5.pckl","rb")
vehiculos=pickle.load(archivo_apertura)
archivo_apertura.close()
for item in vehiculos:
  print(item.estado())
del(archivo_apertura)