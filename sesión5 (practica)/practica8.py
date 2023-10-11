'''
gestión de productos para una tienda

deberá usar clases y objetos para los productos y almacenar sus datos en un archivo de texto.
1. Agregar producto
2. Mostrar lista de productos
3. Buscar producto por nombre
4. Actualizar precio de un producto
5. Eliminar producto
6. Salir

Agregar producto: Al seleccionar esta opción, el programa debe solicitar los siguientes
datos del producto: nombre, precio y cantidad en stock. Luego, debe crear un objeto de tipo
"Producto" con estos datos y agregarlo a una lista de productos.

Mostrar lista de productos: Esta opción debe mostrar en la consola la información de todos
los productos registrados, incluyendo nombre, precio y cantidad en stock.

Buscar producto por nombre: El programa debe permitir al usuario ingresar el nombre de
un producto y mostrar su información si existe en el registro.

Actualizar precio de un producto: El usuario podrá ingresar el nombre de un producto y
su nuevo precio. El programa deberá buscar el producto en la lista y actualizar su precio.
Eliminar producto: El usuario podrá ingresar el nombre de un producto y el programa
deberá eliminarlo de la lista de productos.

Salir: Al seleccionar esta opción, el programa debe guardar los datos de los productos en
un archivo de texto llamado "productos.txt" y finalizar su ejecución.

Además, debes utilizar un diccionario para almacenar temporalmente los productos, donde
la clave será el nombre del producto y el valor será un objeto de la clase "Producto". Al iniciar
el programa, debes cargar los datos de productos desde el archivo "productos.txt" en este
diccionario (si el archivo existe).
Cada producto debe ser representado por una clase llamada "Producto" que tenga atributos
como nombre, precio y cantidad en stock.

Al finalizar el programa (opción 6), los datos actualizados de los productos deben ser
guardados en el archivo "productos.txt".

Realice el control de excepciones y validaciones que considere.
'''

import os

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

def cargar_productos():
    productos = {}
    if os.path.exists("productos.txt"):
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, stock = linea.strip().split(',')
                productos[nombre] = Producto(nombre, float(precio), int(stock))
    return productos

def guardar_productos(productos):
    with open("productos.txt", "w") as archivo:
        for producto in productos.values():
            archivo.write(f"{producto.nombre},{producto.precio},{producto.stock}\n")

def agregar_producto(productos):
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    stock = int(input("Cantidad en stock: "))
    productos[nombre] = Producto(nombre, precio, stock)
    print("Producto agregado correctamente.")

def mostrar_productos(productos):
    for producto in productos.values():
        print(f"Nombre: {producto.nombre}")
        print(f"Precio: ${producto.precio:.2f}")
        print(f"Cantidad en stock: {producto.stock}")
        print("-" * 30)

def buscar_producto(productos, nombre):
    if nombre in productos:
        producto = productos[nombre]
        print(f"Nombre: {producto.nombre}")
        print(f"Precio: ${producto.precio:.2f}")
        print(f"Cantidad en stock: {producto.stock}")
    else:
        print("Producto no encontrado.")

def actualizar_precio(productos, nombre):
    if nombre in productos:
        nuevo_precio = float(input("Nuevo precio: "))
        productos[nombre].precio = nuevo_precio
        print("Precio actualizado correctamente.")
    else:
        print("Producto no encontrado.")

def eliminar_producto(productos, nombre):
    if nombre in productos:
        del productos[nombre]
        print("Producto eliminado correctamente.")
    else:
        print("Producto no encontrado.")

def main():
    print("Bienvenido a la gestión de productos")
    productos = cargar_productos()
    
    while True:
        print("\nMenú:")
        print("1. Agregar producto")
        print("2. Mostrar lista de productos")
        print("3. Buscar producto por nombre")
        print("4. Actualizar precio de un producto")
        print("5. Eliminar producto")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto(productos)
        elif opcion == "2":
            mostrar_productos(productos)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            buscar_producto(productos, nombre)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a actualizar: ")
            actualizar_precio(productos, nombre)
        elif opcion == "5":
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            eliminar_producto(productos, nombre)
        elif opcion == "6":
            guardar_productos(productos)
            print("Datos guardados en 'productos.txt'. Hasta luego.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

main()
