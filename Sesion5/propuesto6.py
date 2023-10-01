'''
Ingresar nombre de archivo de texto con su extensión
lo lea y genere un diccionario teniendo como clave la palabra
y como valor la cantidad de veces que aparece en el texto.

Ejemplo:
la vida es bella y la vida es hermosa
la: 2
vida: 2
es: 2
bella: 1
y: 1
hermosa: 1
'''

from io import open
# import ast

listaMain=[]
diccionario={}
def writefuntion():
    nametxt=input("Nombra el archivo '.txt' que usaremos: ")
    entrada=input("Ingrese su texto: ")
    listaMain = entrada.split()

    for e in listaMain:
        i=0
        for igual in listaMain:
            if e==igual:
                i+=1
                diccionario.update({e:i}) #comentar esta linea y descomentar las otras lineas de código :)
                # agrego="'{}':{}".format(e,i)
        # mostrar_datos.append(agrego)
    # for elemento in mostrar_datos:
    #     dicionariolocal = ast.literal_eval(f'{{{elemento}}}')
    #     diccionario.update(dicionariolocal)    
    
    try:
        with open(f"{nametxt}.txt", "w",encoding='utf-8') as archivo:
            for clave, valor in diccionario.items(): # archivo.write(str(diccionario)) #Para enviar como diccionario
                archivo.write(f'{clave}: {valor}\n')
            archivo.close()
    
    except IsADirectoryError:
        print(f"'{archivo}' es un directorio, no se puede abrir como archivo.")
    except IOError as e:
        print(f"Error de E/S al trabajar con '{archivo}': {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        with open(f"{nametxt}.txt", "r",encoding='utf-8') as archivo:
          imprimir=archivo.read()
          print(imprimir)
          archivo.close()
        return entrada
writen=writefuntion()
print('Su texto: ',writen)