''' 
5. Crear propuesto5.py, que guarde y carge los datos a un archivo.
Debe tener dos clases:

• La clase Película, tendrá atributos: titulo, duración y año de lanzamiento.
Contará con método especial constructor y mostrar que se encargará de visualizar
los atributos de la clase.

• La clase Catálogo que cargará los objetos Películas a un archivo pickle,
tener una lista de películas como atributo de clase y métodos:
constructor, agregar (adicionar la película al listado de películas)
mostrar (visualiza el listado de las películas)
cargar (lee el archivo pickle)
y guardar (almacena los datos en el archivo pickle).
• Guardar y cargar los datos a un fichero.
'''
import pickle

nombre_pickle = "peliculas.pkl" #Nombre del archivo

class Pelicula:
  def __init__(self,titulo,duracion,lanzamiento):
    self.titulo=titulo
    self.duracion=duracion
    self.lanzamiento=lanzamiento
  def __str__(self):
    return (f"Título: {self.titulo}\nDuración: {self.duracion}\nLanzamiento: {self.lanzamiento}")
peliculas=[]
class Catalogo(Pelicula):

  def agregar(self):
    peliculas.append(self)
    print("Se terminó de agregar los elementos")
    
  def mostrar():
    if len(peliculas)==0:
      print("\nNo hay peliculas para mostrar\n")
    else:
      for i,classPelicula in enumerate(peliculas):
        print(f"\nPelícula {i}:\n{str(classPelicula)}")
      print("\nSe terminó de mostrar los elementos.\n")
      
  def cargar():
    while True:
      try:
          with open(nombre_pickle, "rb") as archivo:
            oldlista = pickle.load(archivo)
            if bool(oldlista):
              print(f"Su archivo {nombre_pickle}, está vacío.")
              return peliculas
            else:
              # listacombinada=list(set(peliculas+list(oldlista)))
              peliculas=(list(oldlista))
              print("Terminando de leer los archivos existentes.")
              print("Se guardo en la lista temporal, ver con opción MOSTRAR.")
            del(archivo)
            # peliculas=listacombinada
            return peliculas
      except FileNotFoundError:
        with open(nombre_pickle, "wb") as archivo:
          print("No hay archivo de pickle.")
          print(f"Se creó nueva '{nombre_pickle}'.")
      except IOError as e:
          print(f"Error de E/S al trabajar: {e}")
      except Exception as e:
        print(f"Error inesperado: {e}")
        break
      
  def guardar():
    with open(nombre_pickle, "ab+") as archivo:
      pickle.dump(peliculas, archivo)
      print(f"Los datos han sido guardados en {nombre_pickle}.\n")
    return peliculas
  def guardarycargar():
    ejemplo0=Catalogo("2",200,"2000")
    ejemplo0.cargar()
    ejemplo0.guardar()
    print("Archivos guardados y cargados.")

# pelicula1 = Catalogo("Titanic", 195, "19 de diciembre de 1997")
# pelicula2 = Catalogo("El Padrino", 175, "24 de marzo de 1972")
# pelicula4 = Catalogo("Jurassic Park", 127, "11 de junio de 1993")
# pelicula3 = Catalogo("Star Wars: Una Nueva Esperanza", 121, "25 de mayo de 1977")
# pelicula5 = Catalogo("El Señor de los Anillos: La Comunidad del Anillo", 178, "19 de diciembre de 2001")

# pelicula1.__str__()
# pelicula2.__str__()
# pelicula3.__str__()
# pelicula4.__str__()
# pelicula5.__str__()

# pelicula1.agregar()
# Catalogo.mostrar()
# pelicula2.agregar()
# Catalogo.mostrar()
print("Los 2 elementos agregados.")
# Catalogo.guardar()
Catalogo.mostrar()
peliculas=Catalogo.cargar()
Catalogo.mostrar()
