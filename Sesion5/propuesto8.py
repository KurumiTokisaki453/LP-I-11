import ast
import re

mientras=0
def inputDatos(text):
    if text==0:
        escribir='Nombre'
    elif text==1:
        escribir='Teléfono'
    while True:
        entrada=input(f"Ingrese el {escribir}: ")
        print(f"¿Su {escribir} es: {entrada}?")
        eligir=input("¿Desea continuar? 'S' ¿Quiere cambiar? 'N': ")
        if eligir == '' or eligir.lower() == 's':
            if text!=1:
                print(f"Se ingresó correctamente su {escribir}\n")
                return entrada
            else:
                patron = r'^9\d{8}$'  # Comienza con 9 y tiene 8 dígitos más
                if re.match(patron, entrada):
                    print(f"Se ingresó correctamente su {escribir}\n")
                    return entrada
                else:
                    print("Error... ingresó un número inválido para Perú\n")
        elif eligir=='n' or eligir=='N':
            print(f"Cambiando {escribir}\n")
        else:
            print("Elija una opcion válida.")

def convertidor(param):
    try:
        copiando = param.strip("{}")
        diccionario = ast.literal_eval("{" + copiando + "}")
        return diccionario
    except SyntaxError as e:
        print(f"Error con el archivo de texto: {e}\n")
        newlocal={}
        diccionario=dict(newlocal)
        return diccionario

def consultar(nombre,buscando='1'):
    while buscando=='1':
        try:
            with open("agenda.txt","r",encoding="utf-8") as archivo:
                copiando=archivo.read()
                archivo.close()

            diccionario=convertidor(copiando)
            buscando=diccionario.get(nombre,"1")
            if buscando!="1":
                return buscando
            else:
                buscando='0'
                return buscando
        except FileNotFoundError:
            print("Archivo no encontrado... generando uno nuevo.\n")
            with open("agenda.txt", "w",encoding="utf-8") as creando:
                creando.close()
        except IOError as e:
            print(f"Error de E/S al trabajar con '{archivo}': {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

def agregar(nombre,telefono='1'):
    while True:
        try:
            with open("agenda.txt","a",encoding="utf-8") as archivo:
                texto=f'"{nombre}": {telefono},\n'
                archivo.write(texto)
                archivo.close()
                break
        except IOError as e:
            print(f"Error de E/S al trabajar con '{archivo}': {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

while (mientras!=1):
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
        if opcion == 1:
            name=inputDatos(0)
            numTelefono=consultar(name)
            if numTelefono!='0':
                print(f"Nombre: {name}\nTelefono: {numTelefono}\n")
            else:
                print("El nombre ingresado no se encuentra en la agenda.\n")
        elif opcion == 2:
            name=inputDatos(0)
            fone=inputDatos(1)
            agregar(name,fone)
        # elif opcion == 3:
        # elif opcion == 4:
        elif opcion == 5:
            print("Terminando el programa.")
            mientras=1
        else:
            print('Ingrese una opción válida.')
    except ValueError:
        print("Ingrese uno de los números mostrados mostrados.\n ")



'''
Crear agenda telefónica de clientes
el menú mostrará las siguientes opciones:

▪ Opción 1._ingresar nombre del cliente y mostrará el celular si existe en el fichero agenda.txt, sino mostrará mensaje que no existe el cliente en la agenda.
    verificar nombre y su telefono existe. (r)
▪ Opción 2._registrar nombre y celular de un cliente y lo guardará en el fichero agenda.txt
    crear nombre y telefono nuevo. (a)
▪ Opción 3._eliminar registro de nombre y celular de un cliente. Ingresando el nombre del cliente que desea eliminarlo.
    eliminar nombre y telefono. (w+)
▪ Opción 4._Generar fichero agenda.txt, si exista preguntar si desea eliminarlo e iniciar con un nuevo fichero.
    Generar agenta.txt, o eliminar existencias. (w)
'''