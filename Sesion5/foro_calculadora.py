from io import open

def sum(a,b):
  sumar=a+b
  texto=str(sumar)+'\n'
  txta=open("historial_calculadora.txt","a+")
  txtw=open("historial_calculadora.txt","w+")
  
  txtr=open("historial_calculadora.txt","r")
  print(txtr.read())
  txtr.close()
  
  try:
    print("Escribir 1 para sobreescribir el contenido")
    print("Escribir 2 para continuar la escritura\n")
    ar=int(input("Ingrese 'S' o '3' para Salir: "))
    if ar==1:
      txta.close()
      txtw.write(texto)
      txtw.close()
    elif ar==2:
      txtw.close()
      txta.write(texto)
      txta.close()
    elif ar==3 or ar=='S' or ar=='s':
      print(sumar,"esta es la suma de salir")
      return sumar
  except:
    print("Ingrese una opcion válida.")
  print("numero ingresado: ",sumar)
  return sumar

while True:
  try:
    obj1=int(input("Ingrese un número positivo: "))
    obj2=int(input("Ingrese un número positivo: "))
    if obj1>=0 and obj2 >=0:
      break
    else:
      print("Ingrese un número positivo")
  except ValueError:
    print("Ingrese un número.")

sum(obj1,obj2)