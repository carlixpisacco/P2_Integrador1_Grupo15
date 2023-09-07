import libro as l
import os

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

#primera funcion
def ejemplares_prestados():
   print("\nEjemplares prestados:")
   for libro in libros:
    print(f"Título: {libro['titulo']} - Ejemplares prestados: {libro['cant_ej_pr']}")
   return None

#segunda funcion

def registrar_nuevo_libro():
   libros = nuevo_libro()
   print("\nLibros disponibles e información:")
   for libro in libros:
        print("\nCódigo:", libro['cod'])
        print("Cantidad de ejemplares disponibles:", libro["cant_ej_ad"])
        print("Cantidad de ejemplares prestados:", libro["cant_ej_pr"])
        print("Título:", libro["titulo"])
        print("Autor:", libro["autor"])
   return None

#tercera funcion

def eliminar_ejemplar_libro():
    opc_volver_ingresar = "1"
    while opc_volver_ingresar == "1":
        busc_devolucion = input("\nIngrese el código del libro que desea eliminar ejemplar:\n")
        encontrado = False
        for libro in libros:
            if busc_devolucion == libro.get('cod'):
                encontrado = True
                if libro["cant_ej_ad"] > 0:
                    opc = input(f"\nDesea eliminar un ejemplar del libro '{libro['titulo']}'? Si/No:\n").lower()
                    if opc == "si":
                        print("\nEl ejemplar se ha eliminado con éxito.\n")
                        libro["cant_ej_ad"] -= 1
                        print("La cantidad actualizada de ejemplares disponibles es:", libro["cant_ej_ad"])
                        print("La cantidad actualizada de ejemplares prestados es:", libro["cant_ej_pr"])
                    else:
                        print("\nEl libro no fue eliminado.")
                else:
                    print("\nError. No hay ejemplares disponibles de este libro para ser eliminados.")
        if not encontrado:
            print("\nEl libro con el código '",busc_devolucion,"' no fue encontrado.")
    
        print("\n¿Desea volver a ingresar otro código?")
        print("Presione 1 si quiere volver a ingresar un código.")
        print("Cualquier otra tecla para salir de este menú.")
        opc_volver_ingresar = input("-")

        if opc_volver_ingresar != "1":
            break
    return None

#cuarta funcion

def prestar_ejemplar_libro():
    opc_volver_ingresar = "1"
    while opc_volver_ingresar == "1":
        busc_prestamo = input('\nIngrese el código del libro que desea retirar:\n')
        encontrado = False 
        for libro in libros:
            if busc_prestamo == libro.get('cod'):
                encontrado = True
                print("\nInformación del libro:")
                print("Código:", libro['cod'])
                print("Cantidad de ejemplares disponibles:", libro["cant_ej_ad"])
                print("Cantidad de ejemplares prestados:", libro["cant_ej_pr"])
                print("Título:", libro["titulo"])
                print("Autor:", libro["autor"])

                if libro["cant_ej_ad"] > 0:
                    opc = input(f"\nDesea aprobar el prestamo del libro '{libro['titulo']}'? Si/No: ")
                    if opc.lower() == "si":
                        libro['cant_ej_pr'] += 1
                        libro['cant_ej_ad'] -= 1
                        print("\nPréstamo aprobado.")
                    else:
                        print("\nNo se aprobó el préstamo.")
                else:
                    print(f"\nError. Ya no quedan ejemplares de {libro['titulo']} para prestar.")
                break  
        if not encontrado:
            print("\nEl libro con el código '",busc_prestamo,"' no fue encontrado.")
        
        print("\n¿Desea volver a ingresar otro código?")
        print("Presione 1 si quiere volver a ingresar un código.")
        print("Cualquier otra tecla para salir de este menú.")
        opc_volver_ingresar = input("-")

        if opc_volver_ingresar != "1":
            break
    return None
#quinta funcion

def devolver_ejemplar_libro():
    opc_volver_ingresar = "1"
    while opc_volver_ingresar == "1":
        busc_devolucion = input("\nIngrese el código del libro que desea devolver:\n")
        encontrado = False
        for libro in libros:
            if busc_devolucion == libro.get('cod'):
                encontrado = True
                if libro["cant_ej_pr"] > 0:
                    opc = input(f"\nDesea devolver el ejemplar de {libro['titulo']}? Si/No:\n").lower()

                    if opc == "si":
                        print("\nDevolución exitosa.\n")
                        libro["cant_ej_ad"] += 1
                        libro["cant_ej_pr"] -= 1
                        print("La cantidad actualizada de ejemplares disponibles es:", libro["cant_ej_ad"])
                        print("La cantidad actualizada de ejemplares prestados es:", libro["cant_ej_pr"])
                    else:
                        print("\nNo se gestionó la devolución.")
                else:
                    print(f"\nError. No hay ejemplares de {libro['titulo']} prestados.")
    
        if not encontrado:
            print("\nEl libro con el código '",busc_devolucion,"' no fue encontrado.")
    
        print("\n¿Desea volver a ingresar otro código?")
        print("Presione 1 si quiere volver a ingresar un código.")
        print("Cualquier otra tecla para salir de este menú.")
        opc_volver_ingresar = input("-")

        if opc_volver_ingresar != "1":
            break
    return None

#sexta funcion

def nuevo_libro():
   nuevo_libro = l.nuevo_libro()
   libros.append(nuevo_libro)
   return libros


