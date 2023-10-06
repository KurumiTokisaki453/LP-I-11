'''
3. Crear el archivo propuesto3.py que lea el contenido de un archivo de texto llamado
"entrada.txt", convierta todo el texto en mayúsculas y escriba el resultado en un archivo
llamado "salida.txt".

'''

def mayusTxt():
    try:
        with open("entrada.txt","r",encoding="utf-8") as leerArchivo:
            comprobar1=leerArchivo.read()
            leerArchivo.close()
        with open("salida.txt","w",encoding="utf-8") as mayuscula:
          mayuscula.write(comprobar1.upper())
          mayuscula.close()
          print(f"Archivo de texto convertido CORRECTAMENTE\ntexto nuevo:\n\n{comprobar1.upper()}")
          return comprobar1.upper()
    except FileNotFoundError:
            with open("entrada.txt", "w",encoding="utf-8") as creando:
                creando.close()
    except IOError as e:
        print(f"Error de E/S al trabajar: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
mayusTxt()
