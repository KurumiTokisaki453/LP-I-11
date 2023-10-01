# def devolucion_celular():

#     with open("agenda.txt") as fichero:
#         return

import re

opcion=0
def inputDatos(text):
    if text==0:
        escribir='Nombre'
    elif text==1:
        escribir='Teléfono'
    while True:
        entrada=input(f"Ingrese el {escribir}: ")
        print(f"¿Su {escribir} es: {entrada}?")
        eligir=input("¿Desea continuar? 'S' ¿Quiere cambiar? 'N': ")
        if eligir=='s' or eligir=='S':
            if text!=1:
                return entrada
            else:
                patron = r'^9\d{8}$'  # Comienza con 9 y tiene 8 dígitos más
                if re.match(patron, entrada):
                    return entrada
                else:
                    print("Error... ingresó un número inválido para Perú\n")
        elif eligir=='n' or eligir=='N':
            print(f"Cambiando {escribir}\n")
        else:
            print("Elija una opcion válida.")

while (opcion<1) or (opcion>5):
    try:
        print("=================================================")
        print("                Menu de opciones                 ")
        print("=================================================")
        print("Opción 01: Consultar un celular (1)")
        print("Opción 02: Añadir un celular (2)")
        print("Opción 03: Eliminar un celular (3)")
        print("Opción 04: Crear la agenda (4)")
        print("Opción 05: Salir (5)")
        opcion=int(input("Digite el número de su pedido: "))
    except ValueError:
        print("Ingrese uno de los números mostrados mostrados.\n ")
if opcion == 1:
    name=inputDatos(0)
    fone=inputDatos(1)
elif opcion == 2:
    name=inputDatos(0)
    fone=inputDatos(1)
# elif opcion == 3:
# elif opcion == 4:
else:
    print('Ingrese una opción válida.')


'''
Crear agenda telefónica de clientes
el menú mostrará las siguientes opciones:

1. Consultar un celular.
2. Añadir un celular.
3. Eliminar un celular.
4. Crear la agenda.
5. Salir.

▪ La opción 1 ingresar nombre del cliente y mostrará el celular
si existe en el fichero agenda.txt, sino mostrará mensaje que no existe el cliente en la agenda.
▪ La opción 2 registrar el nombre y celular de un cliente y lo guardará en el
fichero agenda.txt
▪ La opción 3 eliminar el registro de nombre y celular de un cliente.
Ingresando el nombre del cliente que desea eliminarlo.
▪ La opción 4 Generar el fichero agenda.txt, si exista preguntar
si desea eliminarlo e iniciar con un nuevo fichero.
'''