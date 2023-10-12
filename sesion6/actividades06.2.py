#Actividad 06 parte 2
'''
2. Realizar la creación de una clase Docente y ListarDocentes,
crear tres objetos y escribir en un archivo pickle,
luego leerlo e imprimir por pantalla
'''
import pickle
class Docente:
  def __init__(self, nombre, edad, horas):
    self.nombre=nombre
    self.edad=edad
    self.horas=horas
    print("Se ha creado un docente nuevo " + self.nombre )
  
  def __str__(self):
    return f"{self.nombre} {self.edad} {self.edad}"
 
class ListaDocentes:
  docentes=[]
   #Programamos el constructor para que la lista docentes se carga con los datos del archivo
  def __init__(self):
    listaDeDocentes=open("actividad6.bin","ab+")
    listaDeDocentes.seek(0)
    try:
      self.docentes=pickle.load(listaDeDocentes)
      print("Se cargaron {} personas al archivo.".format(len(self.docentes)))
    except:
      print("EL archivo está vacío.")
    finally:
      listaDeDocentes.close()
      del(listaDeDocentes)
 
   #Agrega un docente a la lista y lo guarda en el Archivo
  def agregarDocente(self,d):
    self.docentes.append(d)
    self.guardarDocentesEnArchivo()

  #Muestra el listado de Docentes en pantalla
  def mostrarDocentes(self):
    for d in self.docentes:
      print(d)

  #Guarda el listado de Docentes en el Archivo
  def guardarDocentesEnArchivo(self):
    listaDeDocentes=open("actividad6.bin","wb")
    pickle.dump(self.docentes,listaDeDocentes)
    listaDeDocentes.close()
    del(listaDeDocentes)

  #Muestra la información del Archivo
  def mostrarInformacionArchivo(self):
    print("La información del archivo es:")
    for docente in self.docentes:
      print(docente)

miLista=ListaDocentes()
docente=Docente("Dely",43,30)
miLista.agregarDocente(docente)
docente=Docente("Miguel",24,24)
miLista.agregarDocente(docente)
docente=Docente("Leandro",30,18)
miLista.agregarDocente(docente)
miLista.mostrarDocentes()
print("Lectura de Archivo .bin")
miLista.mostrarInformacionArchivo()

