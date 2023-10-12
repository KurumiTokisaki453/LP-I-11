#Lectura de un archivo pickle
import pickle
archivo = open('actividad3.pckl','rb')
lista = pickle.load(archivo)
print(lista)
archivo.close()
del(archivo)