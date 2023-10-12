#Creación de un archivo pickle
import pickle
lista = [1,2,3,4,5]
archivo = open('actividad3.pckl','wb')
pickle.dump(lista, archivo)
archivo.close()
del(archivo)
