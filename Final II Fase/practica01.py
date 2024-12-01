import pickle

def leertxt(ruta_archivo):
  while True:
    try:
      with open(ruta_archivo, 'r') as lectura:
        texto= lectura.readlines()
        numero_a_buscar = int(input(f"Ingrese el múltiplo a buscar en {ruta_archivo}: "))
        multiplos = []
        for numero in texto:
            if int(numero) % numero_a_buscar == 0:
                multiplos.append(int(numero))
        print(f"Sus múltiplos son: {multiplos}")
      return multiplos
    except FileNotFoundError:
      with open(ruta_archivo, "w") as archivo:
        print(f"Se creó nueva '{ruta_archivo}'.")
    except PermissionError:
      return "Error 2: No se tiene permisos necesarios."
    except Exception as e:
      return f"Error 3: {e}"

def escribir(ruta_destino):
  while True:
    multiplos=leertxt("entrada.txt")
    try:
      with open(ruta_destino, "wb+") as archivo:
        datos_serializados=pickle.dumps(multiplos)
        archivo.write(datos_serializados)

      return f"Se guardo el contenido en '{ruta_destino}'"
    except FileNotFoundError:
      with open(ruta_destino, "wb") as archivo:
        print(f"Se creo nuevo archivo {ruta_destino}")
    except IOError as e:
        print(f"Error de E/S al trabajar: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
print(escribir("salida.bin"))