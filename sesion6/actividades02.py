#Lectura de un archivo binario

datos = bytearray(10)
try:
  fichero = open('actividad1.bin', 'rb')
  fichero.readinto(datos)
  fichero.close()
  for ele in datos:
    print(hex(ele), end=' ')
except Exception as e:
  print("no se puede aperturar el archivo", e)
