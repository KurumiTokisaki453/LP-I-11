# text="'num': 2,'example': 3"
# diccionario={text}
# print(diccionario)

import ast

texto = "'b': 1, 'a': 1, 'c': 1, "
diccionario = ast.literal_eval("{" + texto + "}")

print(diccionario)

print(type(diccionario))
print(str(diccionario).strip("{}"))