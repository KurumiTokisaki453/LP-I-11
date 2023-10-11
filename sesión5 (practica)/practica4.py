'''
4. Crear el archivo propuesto4.py que lea un archivo de texto y
exporte en un archivo.txt las palabras que sólo aparecen una sola vez en el texto.

'''
listaElement=[]
def leer(nametxt):
  while True:
    try:
      with open(nametxt,"r",encoding="utf-8") as leerArchivo:
          leendo=leerArchivo.read()
          print(f"Leendo el texto: \n{leendo}\n")
          leerArchivo.close()

      with open(nametxt,"w",encoding="utf-8") as EscribirArchivo:
          entrada=input("Ingrese el nuevo texto a escribir: ")

          for e in entrada:
            i=0
            for igual in entrada:
              if e==igual: i+=1
            if i==1:
              listaElement.append(e)

          for i in listaElement:
              EscribirArchivo.write(i)
          EscribirArchivo.close()

      return listaElement
    except FileNotFoundError:
            with open(nametxt, "w",encoding="utf-8") as creando:
                creando.close()
    except IOError as e:
        print(f"Error de E/S al trabajar: {e}")
    except Exception as e:
          print(f"Error inesperado: {e}")

texto=leer("archivo.txt")
