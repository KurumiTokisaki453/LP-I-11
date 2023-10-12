#Escritura de una archivo binario

datos = bytearray(10)
for i in range(len(datos)):
  datos[i] = 10 + i
try:
  fichero = open('actividad1.bin', 'wb')
  fichero.write(datos)
  fichero.close()
except Exception as e:
  print("no se puede aperturar el archivo",e)

