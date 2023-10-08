from io import open

listaElement=[]
diccionario={}
def writefuncion():
    while True:
        nametxt=input("Nombra el archivo '.txt' que usaremos: ")
        try:
            entrada=input("Ingrese su texto: ")

            for a in entrada:
                    listaElement.append(a)

            for e in listaElement:
                i=0
                for igual in listaElement:
                    if e==igual:
                        i+=1
                        diccionario.update({e:i})

            with open(f"{nametxt}.txt", "w",encoding='utf-8') as archivo:
                archivo.write(str(diccionario))
                archivo.close()
                for a in entrada:
                    listaElement.append(a)
        except IsADirectoryError:
            print(f"'{archivo}' es un directorio, no se puede abrir como archivo.")
        except IOError as e:
            print(f"Error trabajando con '{archivo}': {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
        finally:
            return entrada
print(f"\nSu texto es: {writefuncion()}\n")

print(diccionario)

'''
permita al usuario ingresa un nombre de un archivo de texto con su respectiva extensión

lo lea y genere un diccionario teniendo como clave cada
letra y como valor la cantidad de veces que aparece en el texto.
Ejemplo:
la vida es bella y la vida es hermosa
{'l': 4, 'a': 6, ' ': 8, 'v': 2, 'i': 2, 'd': 2, 'e': 4, 's': 3, 'b': 1, 'y': 1, 'h': 1, 'r': 1, 'm': 1, 'o': 1}
'''