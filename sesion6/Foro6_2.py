''' 
Guardar el nombre de artículos en un txt para luego pasarlo a un archivo.pkl (binario)
'''
import pickle

name_txt=nombre_pickle="articulos"
def leer():
  while True:
    try:
        with open(f"{name_txt}.txt","r",encoding="utf-8") as leerArchivo:
          comprobar1=leerArchivo.read()
          print(f"Leendo el texto: \n{comprobar1}\n")
          leerArchivo.close()
          del(leerArchivo)
        return comprobar1
        
    except FileNotFoundError:
      with open(f"{name_txt}.txt", "w",encoding="utf-8") as creando:
        entrada=input("Ingrese el nombre de un artículo que quiera agregar: ")
        creando.write(entrada)
        del(creando)
    except IOError as e:
        print(f"Error de E/S al trabajar: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
        
def escribir():
  while True:
    try:
      txtlectura=leer()
      
      with open(f"{nombre_pickle}.pkl", "rb") as aarchivo:
        leerpickle = pickle.load(aarchivo)
        aarchivo.close()
        del(aarchivo)
      if not leerpickle:
        print("El archivo está vacío.")
        break
      else:
        if leerpickle!=txtlectura:
          with open(f"{nombre_pickle}.pkl", "wb") as earchivo:
            pickle.dump(txtlectura, earchivo)
        else:
          print("\nTerminando de leer los archivos existentes.") 
          print(f"El archivo contiene:\n\n{leerpickle}\n")
      break
    except FileNotFoundError:
      with open(f"{nombre_pickle}.pkl", "wb") as earchivo:
        pickle.dump(txtlectura, earchivo)
        print(f"Se creó nueva '{nombre_pickle}.pkl'.")
    except IOError as e:
        print(f"Error de E/S al trabajar: {e}")
    except Exception as e:
      print(f"Error inesperado: {e}")
      break
escribir()
print("Terminó el programa.")