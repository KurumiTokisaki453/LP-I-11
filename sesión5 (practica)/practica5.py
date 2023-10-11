'''
5. Crear el "Empleados.txt" propuesto5.py que contenga una clase Empleado con atributos como
nombre, salario y cargo.

Luego lee un "Empleados.txt" de texto que contiene información sobre
empleados (uno por línea) y crea una lista de objetos Empleado.

'''
import pandas as pd
class Empleado:
  def __init__(self, nombre, salario, cargo):
    self.nombre=nombre
    self.salario=salario
    self.cargo=cargo

  def tranformPandas(self):
    diccionario = {
            'Nombre': [self.nombre],
            'Salario': [self.salario],
            'Cargo': [self.cargo],
        }
    frameData=pd.DataFrame(diccionario)
    return str(frameData)

  def escribir(self):
      try:
        with open("Empleados.txt","w",encoding="utf-8") as escritura:
          escritura.write(self.tranformPandas())
          escritura.close()
        return self.tranformPandas()
      
      except IsADirectoryError:
              print(f"'Empleados.txt' es un directorio, no se puede abrir como .txt.")
      except IOError as e:
              print(f"Error trabajando con 'Empleados.txt': {e}")
      except Exception as e:
              print(f"Error inesperado: {e}")
  
  def leer(self):
    try:
      i=0
      with open("Empleados.txt","r",encoding="utf-8") as lectura:
        
        lineas = lectura.readlines()
        for linea in lineas:
          print(f"linea N°{i}: {linea.strip()}")
          i+=1
        lectura.close()
      return lineas
    except FileNotFoundError:
            print("Archivo no encontrado... generando uno nuevo.\n")
            with open("Empleados.txt", "w",encoding="utf-8") as creando:
                creando.close()
    except IsADirectoryError:
            print(f"'Empleados.txt' es un directorio, no se puede abrir como .txt.")
    except IOError as e:
            print(f"Error trabajando con 'Empleados.txt': {e}")
    except Exception as e:
            print(f"Error inesperado: {e}")
empleado=Empleado("Mario",200,"Gerente")    
empleado.escribir()
empleado.leer()
empleado1=Empleado("Maria",233,"Gerenta")    
empleado1.escribir()
empleado1.leer()
empleado3 = Empleado("Juan", 180, "Asistente")
empleado3.escribir()
empleado3.leer()
  
  
