'''
2. Crear el archivo propuesto2.py en el cual figure una clase Libro
atributos como título, autor y número de páginas

Objetos de tipo Libro y muestra su información en
la consola y genera un archivo csv.

'''
import pandas as pd

class Libro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de Páginas: {self.num_paginas}")

libro1 = Libro("El Gran Gatsby", "F. Scott Fitzgerald", 180)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 368)
libro3 = Libro("Matar a un ruiseñor", "Harper Lee", 324)

data = {
    'Título': [libro1.titulo, libro2.titulo, libro3.titulo],
    'Autor': [libro1.autor, libro2.autor, libro3.autor],
    'Número de Páginas': [libro1.num_paginas, libro2.num_paginas, libro3.num_paginas]
}
df = pd.DataFrame(data)
print("Creando Libro en formato csv")
df.to_csv('libros.csv', index=False)

print("Leendo el libro.csv")
dfread = pd.read_csv('libros.csv')
print(dfread)

