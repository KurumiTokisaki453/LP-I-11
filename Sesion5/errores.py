import os
archivo='name_archivo.txt'
try:
    # Intenta abrir el archivo en modo lectura
    with open(archivo, "w+") as archivo:
        # Realiza operaciones de lectura aquí
        contenido = archivo.read()
    print("Archivo existente leído correctamente.")
except FileNotFoundError:
    # El archivo no existe, puedes crearlo o manejarlo según tus necesidades
    # Por ejemplo, puedes crear un nuevo archivo con un contenido inicial
    with open(archivo, "w") as archivo:
        archivo.write("Este es un nuevo archivo.")
    print(f"Archivo '{archivo}' creado y listo para su uso.")
except IsADirectoryError:
    # El archivo es un directorio en lugar de un archivo
    print(f"'{archivo}' es un directorio, no se puede abrir como archivo.")
except IOError as e:
    # Otros errores de E/S, como problemas de lectura o archivo
    print(f"Error de E/S al trabajar con '{archivo}': {e}")
except Exception as e:
    # Otras excepciones inesperadas
    print(f"Error inesperado: {e}")
else:
    # Este bloque se ejecutará si no se lanza ninguna excepción
    print("Operación de archivo completada sin errores.")
finally:
    # Este bloque se ejecutará siempre, se puede usar para realizar limpieza
    print("Cierre del programa y limpieza de recursos.")