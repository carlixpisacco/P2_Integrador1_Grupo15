import cod_generator
# Crear un diccionario para cada libro
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}
librox = {}
def nuevo_libro():
    print("____________")
    librox['cant_ej_ad'] = int(input("Ingresar cantidad de ejemplares disponibles.\n"))
    librox['cant_ej_pr'] = int(input("Ingresar cantidad de ejemplares prestados.\n"))
    librox["titulo"] = input("Ingresar titulo.\n")
    librox["autor"] = input("Ingresar autor.\n")
    librox['cod'] = generar_codigo()
    print("--------------------")
    print(librox)
    return librox

def generar_codigo():
    gen_cod = cod_generator.generar()
    return gen_cod


