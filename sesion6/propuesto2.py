''' 
2. Crear el archivo propuesto2.py, el cual tome un archivo y determine si es una imagen de tipo
PNG. Un archivo de tipo PNG tiene sus ocho primeros bytes con los valores 89 50 4E 47 0D
0A 1A 0A.
'''

def es_archivo_png(ruta_archivo):
  try:
    with open(ruta_archivo, 'rb') as archivo:
      primeroBytes=archivo.read(8)
      return primeroBytes== b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'
  except FileNotFoundError:
    return "Error 1: No se encontró el archivo."
  except PermissionError:
    return "Error 2: No se tiene permisos necesarios."
  except Exception as e:
    return f"Error 3: {e}"
  
if __name__=='__main__':
  rutaArchivo=input("Ingrese la ruta del archivor: ")
  resultado= es_archivo_png(rutaArchivo)
  if resultado:
    print("Es PNG")
  else:
    print("El archivo no es PNG.")