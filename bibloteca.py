import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)
libros.append(l.librox)
#primera funcion
def ejemplares_prestados():
   
    return None

#segunda funcion

def registrar_nuevo_libro():
    l.nuevo_libro()
    print(libros)
    return None

#tercera funcion

def eliminar_ejemplar_libro():
    #completar
    return None

#cuarta funcion

def prestar_ejemplar_libro():
    buscador = input('Ingresar el código del libro:\n')
    encontrado = False  

    for libro in libros:
        if buscador == libro.get('cod'):
            encontrado = True
            print("Información del libro:")
            print("Código", libro['cod'])
            print("Cantidad de ejemplares disponibles:", libro["cant_ej_ad"])
            print("Cantidad de ejemplares prestados:", libro["cant_ej_pr"])
            print("Título", libro["titulo"])
            print("Autor", libro["autor"])

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
            
            break 
    
    if not encontrado:
        print("El libro con el código", buscador, "no fue encontrado.") 
    return None

#quinta funcion

def devolver_ejemplar_libro():
    busc = input("Ingresar el código del libro:\n")
    encontrado = False
    for libro in libros:
        if busc == libro.get('cod'):
            if libro["cant_ej_pr"] > 0:
                opc = input("Desea devolver el ejemplar? Si/No:\n")
                if opc.lower() == "si":  
                    encontrado = True
                    print("-------------------")
                    print("Devolución exitosa.\n")
                    libro["cant_ej_ad"] += 1
                    libro["cant_ej_pr"] -= 1
                    print("La cantidad actualizada de ejemplares disponibles es: ", libro["cant_ej_ad"])
                    print("La cantidad actualizada de ejemplares prestados es: ", libro["cant_ej_pr"])           
            else:
                print("Error. No hay ejemplares de este libro prestados.") #cuando salta el error de que no hay ejemplares prestados, tambien tira el if not del encontrado.
                break
    if not encontrado:
        print("El libro con el código", busc, "no fue encontrado.\n")  
    return None



#sexta funcion

def nuevo_libro1():
    #completar
    return None


