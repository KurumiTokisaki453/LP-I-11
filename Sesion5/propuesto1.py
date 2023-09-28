from io import open


def tablaMulti(a):
  txt=open("tabla_propuesto.txt","w+")
  for i in range(11):
    multiplicar=a*i
    texto=f"{a} x {i} = {multiplicar}\n"
    txt.write(texto)
    #print(texto)
  txt.close()
  return a

while True:
  try:
    obj=int(input("Ingrese un número entre 1 y 10: "))
    if obj>=1 and obj<=10:
      break
    else:
      print("Ingrese un número entre 1 y 10")
  except ValueError:
    print("Ingrese un número.")

tablaMulti(obj)







'''
Crear propuesto1.py que solicite un entero entre 1 y 10 y guarde
en fichero con nombre tabla_propuesto.txt la tabla de multiplicar de ese número.
Realice las validaciones y excepciones que considere.
'''