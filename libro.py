import cod_generator
# Crear un diccionario para cada libro
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}
   
def nuevo_libro():
    librox={}
    print("Ingrese los datos del libro que quiere registrar:\n")
    librox['cod'] = generar_codigo()
    while True:
        ingreso_cant_ejemplares = input("Cantidad de ejemplares disponibles:\n")
        if ingreso_cant_ejemplares.isnumeric():
            ingreso_cant_ejemplares = int(ingreso_cant_ejemplares)
            if ingreso_cant_ejemplares <= 0:
                print("El número de ejemplares disponibles debe ser mayor a 0")
            else:
                librox['cant_ej_ad'] = ingreso_cant_ejemplares
                break
        else:
            print("El número de ejemplares disponibles debe ser un número entero positivo, por favor vuelva a ingresarlo.")
    
    while True:
        ingreso_ejem_prestados = input("Cantidad de ejemplares prestados:\n")
        if ingreso_ejem_prestados.isnumeric():
            ingreso_ejem_prestados = int(ingreso_ejem_prestados)
            if ingreso_ejem_prestados >= 0:
                librox['cant_ej_pr'] = ingreso_ejem_prestados
                break
            else:
                print("El número de ejemplares disponibles debe ser un número entero positivo, por favor vuelva a ingresarlo.")
        else:
            print("El número de ejemplares disponibles debe ser un número entero positivo, por favor vuelva a ingresarlo.")
    
    librox["titulo"] = input("Título:\n")
    librox["autor"] = input("Autor:\n")
    return librox

def generar_codigo():
    gen_cod = cod_generator.generar()
    return gen_cod


