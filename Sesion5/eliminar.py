#Manejando diccionarios para su uso en open,write,read '.txt'
# import ast

# texto = "'b': 1, 'a': 1, 'c': 1, "
# diccionario = ast.literal_eval("{" + texto + "}")
# print(diccionario)
# print(type(diccionario))
# print(str(diccionario).strip("{}"))

mi_diccionario = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Lima'}

nombre = mi_diccionario.get('nombre') # Buscar el valor asociado a la clave 'nombre' con get()
print(nombre)  # Esto imprimirá 'Juan'

valor = mi_diccionario.get('apellido') # Si la clave no existe, get() devuelve None por defecto
print(valor)  # Esto imprimirá None

valor = mi_diccionario.get('apellido', 'Apellido no encontrado') # Especifica un valor predeterminado si la clave no existe
print(valor)  # Esto imprimirá 'Apellido no encontrado'
print(type(mi_diccionario))
