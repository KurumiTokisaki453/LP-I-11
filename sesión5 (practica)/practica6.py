'''
6. Crear el archivo propuesto6.py, en la cual figure una clase GrupoEmpleados que contenga
una lista de objetos Empleado.

Luego, calcula el salario promedio de todos los empleados
en el grupo.

'''

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

class GrupoEmpleados:
    def __init__(self):
        self.lista_empleados = []

    def agregarEmpleados(self, empleado):
        self.lista_empleados.append(empleado)

    def salario_promedio(self):
        sumaSalario=0
        if self.lista_empleados==[]:
            return sumaSalario
        else:
          for todos in self.lista_empleados:
              sumaSalario+=todos.salario
          promedio=sumaSalario / len(self.lista_empleados)
          return promedio

empleado1 = Empleado("Mario", 2000)
empleado2 = Empleado("Maria", 2500)
empleado3 = Empleado("Juan", 1800)

grupo = GrupoEmpleados()
grupo.agregarEmpleados(empleado1)
grupo.agregarEmpleados(empleado2)
grupo.agregarEmpleados(empleado3)

salario_promedio = grupo.salario_promedio()
print(f"Salario promedio de los empleados: {salario_promedio:.2f}")
