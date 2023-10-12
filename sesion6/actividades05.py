#Determinar si un archivo es tipo imagen BMP
'''.
Realizar un programa que tome un archivo y determine si es una imagen de tipo
BMP. Un archivo de tipo BMP tiene sus dos primeros bytes con los valore B y M
(0x42 y 0x4D)
'''
#Programar si un archivo esta en formato BMP
class TipoImagen:
 @staticmethod
 def chequearImagenBMP(archivo):
  archivo_binario=open(archivo,"rb")
  contenido=archivo_binario.read(2)
  if contenido[0]==0x42 and contenido[1]==0x4D:
    return True
  return False

#Prueba de revision
print("Prueba 1:",TipoImagen.chequearImagenBMP("imagen_bmp.bmp"))
print("Prueba 2:",TipoImagen.chequearImagenBMP("imagen_jpg.jpg"))
print("Prueba 3:",TipoImagen.chequearImagenBMP("imagen_png.png"))
