'''
7. Crear el archivo propuesto7.py que tenga una lista de objetos Libro y guarda su información
en un archivo de texto llamado "libros.txt"
'''

class Libro:
    def __init__(self, titulo, autor, publicacion):
        self.titulo = titulo
        self.autor = autor
        self.publicacion = publicacion

libro1 = Libro("El Gran Gatsby", "F. Scott Fitzgerald", 1925)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
libro3 = Libro("1984", "George Orwell", 1949)
libro4 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605)


lista_libros = [libro1, libro2, libro3,libro4]

with open("libros.txt", "w", encoding="utf-8") as archivo:
    for libro in lista_libros:
        print(libro)
        archivo.write(f"Título: {libro.titulo}\n")
        archivo.write(f"Autor: {libro.autor}\n")
        archivo.write(f"Año de Publicación: {libro.publicacion}\n\n")

print("Información de los libros guardada en 'libros.txt'.")
