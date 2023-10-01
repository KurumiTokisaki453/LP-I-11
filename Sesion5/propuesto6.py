'''
permita ingresar nombre de un archivo de texto con su extensión

lo lea y genere un diccionario teniendo como clave la palabra
y como valor la cantidad de veces que aparece en el texto.

Ejemplo:
la vida es bella y la vida es hermosa
la: 2
vida: 2
es: 2
bella: 1
y: 1
hermosa: 1
'''

diccionario = {'la':2,'vida':2,'es':2,'bella':1,'y':1,'hermosa':1}
print(diccionario)
for clave,valor in diccionario.items():
  print(f'{clave}: {valor}')
diccionario.update({'la':3})
diccionario.update({'las':3})
print(diccionario)
