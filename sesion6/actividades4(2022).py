import pickle
class Persona:
  def __init__(self,nombre):
    self.nombre = nombre
  def __str__(self):
    return self.nombre
nombres =['Luis','Leandro','Juan']
personas = []
for x in nombres:
  p = Persona(x)
  personas.append(p.nombre)
print(personas)
fichero = open('actividad4.pckl','wb')
pickle.dump(personas, fichero)
fichero.close()