import csv
import os
NOMBRE_ARCHIVO = "catalogo.csv"

#Esta función se encarga de actualizar los ejemplares de un titulo en caso de presatamos(-1) y en caso de devolución (+2)
def actualizarEjemplares():
    catalogo = obtenerCatalogo()
    if not catalogo:
        return print("El catalogo esta vacio")
    while True:
        opcion = input("Ingrese 'P' si desea hacer un prestamos (-1) o 'D' si dese hacer una devolucion (+1): ").strip().lower()
        if opcion == "":
            print ("No se permite ingresar textos vacios")
            continue
        if opcion.isdigit():
            print("no se permiten digitos númericos, ingresa una de las opciones si desea hacer un prestamo o devolución")
            continue
        if opcion != 'p' and opcion != "d":
            print("Error, Ingresa una de las opciones 'P' o 'D' ")
            continue

        print("Opción Validada!")
        break
    if opcion == 'p':
        titulo = input("Ingresa el nombre del titulo al cual desea hacer el prestamo: ").strip().lower()
        titulo_encontrado = None

        for libro in catalogo:
            if titulo == libro["TITULO"].strip().lower():
                titulo_encontrado = libro
                break

        if titulo_encontrado:
            if titulo_encontrado["CANTIDAD"] > 0:
                titulo_encontrado["CANTIDAD"] -= 1
                guardarCatalogo(catalogo)
                print(f"Préstamo exitoso. Quedan {titulo_encontrado['CANTIDAD']} ejemplares de {titulo_encontrado['TITULO']}.")
            else: 
                # El libro se encontró, pero está agotado
                print("No es posible el prestamo porque el título no tiene ningún ejemplar.")
        
        else:
            print(f"Error: El título '{titulo}' no se encontró en el catálogo.")
            
    elif opcion == 'd':

        titulo = input("Ingresa el nombre del titulo al cual desea hacer el la devolución").strip().lower()
        titulo_encontrado = None

        for libro in catalogo:
            if titulo == libro["TITULO"].strip().lower():
                titulo_encontrado = libro
                break

        if titulo_encontrado:
            if titulo_encontrado["CANTIDAD"] >= 0:
                titulo_encontrado["CANTIDAD"] += 1
                guardarCatalogo(catalogo)
                print(f"Devolución exitosa. Quedan {titulo_encontrado['CANTIDAD']} ejemplares de {titulo_encontrado['TITULO']}.")   
        if not titulo_encontrado:
            print(print(f"Error: El título '{titulo}' no se encontró en el catálogo."))




#Esta funcion se encarga de la tarea de agregar titulos individualmente con su cantidad de ejemplares
def agregarTitulo():
    catalogo = obtenerCatalogo()
    while True:
        titulo = input("Ingrese el nombre del titulo: ").strip()
        if titulo == "":
            print("El titulo no puede estar vacio, ingrese otro titulo nuevamente")
            continue
        titulo_normalizado = titulo.strip().lower()
        es_duplicado = False
        for libro in catalogo:
            titulo_existente_normalizado = libro["TITULO"].strip().lower()
            if titulo_existente_normalizado == titulo_normalizado:
                es_duplicado = True
                break
        if es_duplicado:
            print("El titulo ingresado ya existe, elije otro titulo para ingresar")
            continue
        else:
            break     
        

    while True:
        cantidad_ejemplares = input("Ingrese la cantidad de ejemplares que desea: ").strip()
        if cantidad_ejemplares == "":
            print("No puedes dejar el campo vacio. Intentalo nuevamente")
            continue
        if not cantidad_ejemplares.isdigit():
            print("Solo se permiten numero enteros positivos. Intentalo nuevamente")
            continue

        cantidad_ejemplares = int(cantidad_ejemplares)
        
        if cantidad_ejemplares <= 0:
            print("La cantidad de ejemplares no puede ser menor a 0 o no puede ser otro caracter que no sea un numero, ingrese nuevamente un numero valido")
            continue
        else:
            break

    diccionario_titulos = {
        "TITULO" : titulo,
        "CANTIDAD": cantidad_ejemplares,
        }
    catalogo.append(diccionario_titulos)
    guardarCatalogo(catalogo)

#Esta funcion se encarga de mostrar unicamente los titulos agotados osea con 0 ejemplares   
def mostrarAgotados():
    catalogo = obtenerCatalogo()
    agotados = []
    print("Titulos Agotados")
    for titulo in catalogo:
        if titulo["CANTIDAD"] == 0:
            agotados.append(titulo)
    if titulo["CANTIDAD"] != 0:
        return "No existen titulos agotados"
    return agotados

#
def consultarDisponibilidad(nombre):
    catalogo = obtenerCatalogo()
    disponible = None
    encontrado = None
    for titulo in catalogo:
        if titulo["TITULO"].lower() == nombre:
            encontrado = titulo
            break
    if encontrado is None:
        return print(f"no se en contro el titulo ingresado {nombre}") 
    if encontrado["CANTIDAD"] == 0:
        return print(f"El titulo {nombre} no tiene ejemplares disponibles")
    if encontrado["CANTIDAD"] >= 0:
        return print(f" el titulo {nombre} esta disponible y tiene {encontrado["CANTIDAD"]} ejemplares disponibles")   


#la tarea de esta funcion es buscar el titulo al cual queremos agregar ejemplaress
def ingresarEjemplares():
    catalogo = obtenerCatalogo()
    mostrarCatalogo(catalogo)
    while True:
        nombre_titulo = input("Ingrese el nombre del titulo al cual desea ingresar Ejemplares (o 's' para salir):").strip().lower()
        if nombre_titulo == "s":
            break
        if nombre_titulo == "":
            print("El nombre ingresado no puede ser vacio")
            continue
        encontrado = None
        for titulo in catalogo:
            if titulo["TITULO"].lower() == nombre_titulo.lower().strip():
                    encontrado = titulo
                    break   
        if encontrado is None:
            print(f"Error, no se encuentra el titulo {nombre_titulo} en el catalogo")
            continue
        while True:
            ejemplares = input(f"Ingrese la cantidad de ejemplares que desea  añadir al título '{encontrado["TITULO"]}' : ").strip()

            if not ejemplares.isdigit():
                print("ERROR: Solo se permiten números enteros positivos.")
                continue

            ejemplares = int(ejemplares)
            
            if ejemplares <= 0:
                print("ERROR: La cantidad debe ser al menos 1.")
                continue
            else:
                break
        
        encontrado["CANTIDAD"] += ejemplares
        guardarCatalogo(catalogo)
        print(f"¡EXITO! Se añadieron {ejemplares} ejemplares al título '{encontrado["TITULO"]}'. Nueva cantidad: {encontrado["CANTIDAD"]}")

#Esta funcion se encarga de mostrar el catalogo disponible
def mostrarCatalogo(catalogo):
    if not catalogo:
        print("El catalogo esta vacio")
        return
    print("-------Catalogo Actual--------")
    for titulo in catalogo:
        print(f"TITULO : {titulo["TITULO"]} - CANTIDAD : {titulo["CANTIDAD"]}")


# La tarea de esta funcion es obtener los valores del catalogo si existe y en caso contrario se crea un catalogo vacio
def obtenerCatalogo():
    if not os.path.exists(NOMBRE_ARCHIVO):
        print("El archivo no existe")
        with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["TITULO", "CANTIDAD"])
            escritor.writeheader()
    catalogo = []
    with open(NOMBRE_ARCHIVO, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            catalogo.append({
                "TITULO" : fila["TITULO"],
                 "CANTIDAD": int(fila["CANTIDAD"] ) 
            })
    return catalogo

# la tarea de esta funcion es guardar los datos ingresados que fuimos acumulando en la funcion ingresar_titulos()
def guardarCatalogo(catalogo):
    with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
        campos = ["TITULO", "CANTIDAD"]
        escritor = csv.DictWriter(archivo, fieldnames= campos) 
        escritor.writeheader()
        escritor.writerows(catalogo)
    print("Catalogo Actualizado Correctamente")



# Se encarga de la logica de ingresar titulos como tambien ingresar la cantidad de ejemplares de cada titulo

def ingresarTitulos():
    catalogo = obtenerCatalogo()
    while True:
        cantidad_titulos = input("Ingrese la cantidad de titulos que desea ingresar: ").strip()
        if cantidad_titulos == "":
            print("No puedes dejar el campo vacio. Intentalo nuevamente")
            continue
        if not cantidad_titulos.isdigit():
            print("Solo se permiten numero enteros positivos. Intentalo nuevamente")
            continue
        cantidad_titulos = int(cantidad_titulos)
        if cantidad_titulos <= 0 :
            print("La cantidad de titulos debe ser mayor a 0. Intentalo nuevamente")
            continue
        else:
            break

    for i in range(cantidad_titulos):
        while True:
            titulo = input(f"Ingrese el nombre del titulo numero {i + 1}: ").strip()
            if titulo == "":
                print("El titulo no puede estar vacio, ingrese otro titulo nuevamente")
                continue
            titulo_normalizado = titulo.strip().lower()
            es_duplicado = False
            for libro in catalogo:
                titulo_existente_normalizado = libro["TITULO"].strip().lower()
                if titulo_existente_normalizado == titulo_normalizado:
                    es_duplicado = True
                    break
            if es_duplicado:
                print("El titulo ingresado ya existe, elije otro titulo para ingresar")
                continue
            else:
                break     

        while True:
            cantidad_ejemplares = input("Ingrese la cantidad de ejemplares que desea: ").strip()
            if cantidad_ejemplares == "":
                print("No puedes dejar el campo vacio. Intentalo nuevamente")
                continue
            if not cantidad_ejemplares.isdigit():
                print("Solo se permiten numero enteros positivos. Intentalo nuevamente")
                continue

            cantidad_ejemplares = int(cantidad_ejemplares)
            if cantidad_ejemplares <= 0:
                print("La cantidad de ejemplares no puede ser menor a 0 o no puede ser otro caracter que no sea un numero, ingrese nuevamente un numero valido")
                continue
            else:
                break

        diccionario_titulos = {
            "TITULO" : titulo,
            "CANTIDAD": cantidad_ejemplares,
        }
        catalogo.append(diccionario_titulos)
    guardarCatalogo(catalogo)

    return catalogo
        
# Esto mostrara el menu interactivo
def mostrar_menu():
    while True:
        print("-" * 20)
        print("1. Ingresar titulos")   
        print("2. Ingresar ejemplares")   
        print("3. Mostrar catálogo")   
        print("4. Consultar disponibilidad")    
        print("5. Listar agotados")   
        print("6. Agregar título")   
        print("7. Actualizar ejemplares (préstamo/devolución)")   
        print("8. Salir")
        print("-" * 20)

        opcion = input("Ingrese una opcion: ").strip()

        match opcion:
            case "1":
                print("Ingrese el titulo")
                ingresarTitulos()
            case "2":
                print("Ingrese los ejemplares")
                ingresarEjemplares()
            case "3":
                print("Mostrar catálogo")
                catalogo_Actual = obtenerCatalogo()
                mostrarCatalogo(catalogo_Actual)
            case "4":
                print("Consultar disponibilidad")
                nombre = input("Ingresa el nombre del titulo al que desea consultar su disponiblidad").strip().lower()
                consultarDisponibilidad(nombre)
            case "5":
                print("Listar agotados")
                print(mostrarAgotados())
            case "6":
                print("Agregar titulo")
                agregarTitulo()
            case "7":
                print("Actualizar Ejemplares")
                actualizarEjemplares()
            case "8":
                print("Saliendo del Programa...")
                break
            case _:
                print("La opción ingresada es invalida")


mostrar_menu()