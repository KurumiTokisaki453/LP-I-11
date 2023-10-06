import pickle
fichero = open('actividad2.pckl','rb')
fichero.seek(0)
lista = pickle.load(fichero)
print(lista)