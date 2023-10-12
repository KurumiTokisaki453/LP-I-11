'''
1. Crear el archivo propuesto1.py, el cual tome un archivo y determine si es una imagen de tipo
JPG. Un archivo de tipo JPG tiene sus dos primeros bytes con los valores FF D8.

'''
def es_archivo_jpg(ruta_archivo):
  try:
    with open(ruta_archivo, 'rb') as archivo:
      primeroBytes=archivo.read(2)
      return primeroBytes== b'\xFF\xD8'
  except FileNotFoundError:
    print("El archivo no se encontró.")
    return False
rutaArchivo=input("Ingrese la ruta del archivo que desea verificar: ")

if es_archivo_jpg(rutaArchivo):
  print("Es JPG")
else:
  print("No es una imagen JPG o no se puede ingresar al archivo.")