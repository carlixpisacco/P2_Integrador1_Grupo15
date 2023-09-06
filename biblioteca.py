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
   
    return None

#segunda funcion

def registrar_nuevo_libro():
   nuevo_libro = l.nuevo_libro()
   libros.append(nuevo_libro)
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
    #completar
    return None

#cuarta funcion

def prestar_ejemplar_libro():
    opc_volver_ingresar = "1"
    while opc_volver_ingresar == "1":
        busc_prestamo = input('Ingresar el código del libro:\n')
        encontrado = False 
        for libro in libros:
            if busc_prestamo == libro.get('cod'):
                encontrado = True
                print("Información del libro:")
                print("Código:", libro['cod'])
                print("Cantidad de ejemplares disponibles:", libro["cant_ej_ad"])
                print("Cantidad de ejemplares prestados:", libro["cant_ej_pr"])
                print("Título:", libro["titulo"])
                print("Autor:", libro["autor"])

                if libro["cant_ej_ad"] > 0:
                    opc = input("Desea aprobar este préstamo? Si/No: ")
                    if opc.lower() == "si":
                        libro['cant_ej_pr'] += 1
                        libro['cant_ej_ad'] -= 1
                        print("Préstamo aprobado.")
                    else:
                        print("No se aprobó el préstamo.")
                else:
                    print("Error. Ya no quedan ejemplares para prestar.")
                opc_volver_ingresar = "0"
                break
            
        if encontrado == False:
            print("\nEl libro con el código", busc_prestamo, "no fue encontrado.")
            print("¿Desea volver a ingresar otro código?")
            print("Presione 1 si quiere buscar con otro código.")
            print("Cualquier otra tecla para salir de este menú.")
            opc_volver_ingresar = input("-")
            if opc_volver_ingresar == "1":
                continue
            elif opc_volver_ingresar != "1":
                break
    return None

#quinta funcion

def devolver_ejemplar_libro():
    opc_volver_ingresar = "1"
    while opc_volver_ingresar == "1":
        busc_devolucion = input("Ingresar el código del libro que desea devolver:\n")
        encontrado = False
        for libro in libros:
            if busc_devolucion == libro.get('cod'):
                encontrado = True
                if libro["cant_ej_pr"] > 0:
                    opc = input("Desea devolver el ejemplar? Si/No:\n")
                    if opc.lower() == "si":  
                        print("\nDevolución exitosa.\n")
                        libro["cant_ej_ad"] += 1
                        libro["cant_ej_pr"] -= 1
                        print("La cantidad actualizada de ejemplares disponibles es: ", libro["cant_ej_ad"])
                        print("La cantidad actualizada de ejemplares prestados es: ", libro["cant_ej_pr"])

                    else:
                        print("No se gestionó la devolución")          
                else:
                    print("Error. No hay ejemplares de este libro prestados.")
                    print("¿Desea volver a ingresar otro código?")
                    print("Presione 1 si quiere buscar con otro código.")
                    print("Cualquier otra tecla para salir de este menú.")
                    opc_volver_ingresar = input("-")
                    if opc_volver_ingresar == "1":
                        continue
                    elif opc_volver_ingresar != "1":
                        break
                opc_volver_ingresar = "0"

        if encontrado == False:
            print("\nEl libro con el código", busc_devolucion, "no fue encontrado.")
            print("¿Desea volver a ingresar otro código?")
            print("Presione 1 si quiere buscar con otro código.")
            print("Cualquier otra tecla para salir de este menú.")
            opc_volver_ingresar = input("-")
            if opc_volver_ingresar == "1":
                continue
            elif opc_volver_ingresar != "1":
                break
    return None




