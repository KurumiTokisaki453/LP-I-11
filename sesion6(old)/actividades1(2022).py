'''
Actividad 01 segunda fase 2022
'''
import pickle

datos = bytearray(10)
for i in range(len(datos)):
  datos[i] = 10 + i
  try:
    fichero = open('ejemplo1.bin','wb')
    fichero.write(datos)
    fichero.close()
  except Exception as e:
    print('No se puede abrir el archivo',e )
