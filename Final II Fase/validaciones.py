def validarFecha():
  fecha_por_defecto = "2000-12-31"  # Fecha por defecto
  while True:
        fecha_str = input("Ingrese una fecha (YYYY-MM-DD) o Enter para usar la fecha por defecto (2000-12-31): ")
        if fecha_str == "":
            return fecha_por_defecto
        try:
            datetime.strptime(fecha_str, '%Y-%m-%d')
            return fecha_str
        except ValueError:
            print("Fecha no válida. Intente nuevamente.")
def telefonovalidar():
  while True:
    try:
      numero=int(input("Ingrese su número telefónico: "))
      inicial=str(numero)
      if len(inicial)==9:
        return numero
      else:
        print("Ingrese 9 dígitos y número +51(Perú) inicia con 9")
    except:
      print("Ingresó un valor inválido.")
def validarHora():
  while True:
    try:
      hora=int(input("Ingrese la hora de la cita (formato 24 horas): "))
      if len(str(hora))==2 and (hora>=0 and hora<=24):
        return hora
      else:
        print("Solo se permite 2 dígitos, formato 24 horas")
    except:
      print("Error: ingrese un valor válido.")
def ArchivoTxt(resultado):
  try:
    with open("consultas.txt", "w",encoding='utf-8') as archivo:
      archivo.write(resultado)
      archivo.close()
  except IsADirectoryError:
    print(f"'{archivo}' es un directorio, no se puede abrir como archivo.")
  except IOError as e:
    print(f"Error trabajando con '{archivo}': {e}")
  except Exception as e:
    print(f"Error inesperado: {e}")
  finally:
    return entrada