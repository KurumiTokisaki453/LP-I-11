''' 
Con nuestro programa, puedes crear y guardar una lista de alumnos de una manera sencilla y eficiente:

1. Ingresa la cantidad de alumnos que deseas en tu lista.
2. Añade los nombres de los alumnos uno por uno.
3. ¡Listo! Tu lista se guarda automáticamente en un archivo binario.
Nuestro programa utiliza Python y la biblioteca pickle para gestionar tus listas de alumnos y protegerlos en formato binario.
'''

import pickle
lista=[]
cantidad=int(input("Ingrese la cantidad de alumnos que tendra la lista: "))
for x in range(cantidad):
  entrada=input("Ingrese el nombre de los alumnos: ")
  lista.append(entrada)
fichero = open('actividad2.pckl','wb')
pickle.dump(lista, fichero)
fichero.close()