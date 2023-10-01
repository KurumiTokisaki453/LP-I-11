import os

class RegistroAlumnos():
  def __init__(self,seccion,nombre,notas):
    self.seccion=seccion
    self.nombre=nombre
    self.notas=notas
  def seccionUbi(self):
    text=''
    while text!='A' and text!='C' and text!='B':
      try:
        print("Las secciones disponibles son: 'A','B','C'")
        text=input('Ingrese la sección del Alumno: ')
        self.seccion=text
      except ValueError:
        print('Ingrese un valor válido')
  def writeNota(self):
    num=-1
    while num<0 or num>20:
      try:
        print("La nota es de 0 a 20")
        num=int(input('Ingrese la nota del Alumno: '))
        self.notas=num
      except ValueError:
        print('Ingrese un valor válido')
  def nombreAlum(self):
    boolean=False
    while boolean==False:
      try:
        text1=input('Ingrese el nombre del Alumno: ')
        print(f'Su nombre es: {text1}?')
        val=input('¿Continuar? "s" ¿Cambiar nombre? "n": ')
        if val=='s' or val=='S':
          self.nombre=text1
          boolean=True
        elif val=='n' or val=='N':
          print('Cambiando nombre...')
      except ValueError:
        print('Ingrese un valor válido')
  def __str__(self):
    print(f'Seccion: {self.seccion}\nNombre: {self.nombre}\nNota: {self.notas}')
  def writer(self):
    return str(f"{self.seccion};{self.nombre};{self.notas}")
    
obj=RegistroAlumnos('A','name1',0)
obj.seccionUbi()
obj.nombreAlum()
obj.writeNota()
obj.__str__()

while True:
  try:
    if os.path.exists("Notas.txt"):
        print(f"El archivo existe.")
        with open('Notas.txt','r',encoding='utf-8') as reader:
          contenido=reader.read()
          print(contenido)
          reader.close()
        break
    else:
      print(f"El archivo no existe.")
      with open('Notas.txt','a+',encoding='utf-8') as allNotes:
        allNotes.write(obj.writer())
        allNotes.close()
      break
  except:
    print('Error en el sistema...')