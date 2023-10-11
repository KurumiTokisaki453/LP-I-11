'''
1. Crear el archivo propuesto1.py en el que cree una clase llamada Estudiante con atributos
como nombre, edad, género y una diccionario de calificaciones. Luego, cree objetos de tipo
Estudiante y calcule su promedio de calificaciones.
***********************************************************************
Clase Estudiante, atributos: nombre, edad, género, lista_de_calificaciones.
----
objetos Estudiante, calcular promedio de calificaciones.
'''

import pandas as pd

class Estudiante:
  def __init__(self, nombre, edad, genero,notas):
    self.nombre=nombre
    self.edad=edad
    self.genero=genero
    self.notas=notas
  
  def promedio(self):
    suma = sum(self.notas)
    resultado=suma / len(self.notas)
    return resultado
  
  def tranformPandas(self):
    diccionario = {
            'Nombre': [self.nombre],
            'Edad': [self.edad],
            'Género': [self.genero],
            'notas': [self.promedio()]
        }
    return pd.DataFrame(diccionario)
  
  def imprimirpandas(self):
    dataframe = self.tranformPandas()
    print(f"La diccionario es: \n{dataframe}")

  def __str__(self):
    print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nGénero: {self.genero}")

claseEstudiante1=Estudiante('maria',15,"Femenino",[10,10,5,15])
claseEstudiante1.imprimirpandas()
  











# claseEstudiante=Estudiante('Juan',10,"Masculino")
# claseEstudiante.imprimirpandas()

# diccionario={'Nombre': ['Juan','Roberta'],
#        'Edad': [10,15],
#        'Género':['Masculino','Femenino'],
#       }







