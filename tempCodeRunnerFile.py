 buscador = input("Ingresar el código del libro: ")
    encontrado = False  
    for libro in libros:
        if buscador == libro['cod']:
            encontrado = True
            print("Información del libro:")
            print("Código", libro["cod"])
            print("Cantidad de ejemplares disponibles:", libro["cant_ej_ad"])
            print("Cantidad de ejemplares prestados:", libro["cant_ej_pr"])
            print("Título", libro["titulo"])
            print("Autor", libro["autor"])
            if libro["cant_ej_ad"] > 0:
                opc = input("Desea aprobar este prestamo? Si/No ")
            elif opc.lower() == "si":
             libro["cant_ej_pr"] += 1
             libro["cant_ej_ad"] -= 1
             print(libro)
            else:
                print("Error. Ya no quedan ejemplares para prestar.")
            break 
    if not encontrado:
        print("El libro con el código", buscador, "no fue encontrado.") 
    return None
