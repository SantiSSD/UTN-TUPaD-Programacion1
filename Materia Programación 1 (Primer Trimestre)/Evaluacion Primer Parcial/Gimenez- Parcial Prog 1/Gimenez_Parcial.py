opcion = ""
titulos = []
ejemplares = []

while opcion != 8:
        print("""
------Menú Biblioteca------
1) Ingresar títulos
2) Ingresar ejemplares
3) Mostrar catálogo
4) Consultar disponibilidad
5) Listar agotados
6) Agregar título (con ejemplares)
7) Actualizar ejemplares (prestamos o devolución)
8) Salir
    """)
        opcion = input("------Ingrese la opción que desea------")
        print("--------------------------------------------------")

        if not opcion.isdigit():
            print("Debe ingresar un número entero entre el 1 y el 8")
            continue
        opcion = int(opcion)
        if opcion < 1 or opcion > 8:
            print("------Ingresaste un número fuera del rango------ ")
            continue

        match opcion:
            case 1:
                titulo = input("Ingresa la cantidad inicial de titulos que desea... ")
                if not titulo.isdigit():
                    print("Error, Debes ingresar un numero entero")
                    continue
                titulo = int(titulo)
                
                    
                for i in range(titulo):
                        nombre = input(f"Ingrese del nombre del titulo numero {i + 1}").strip().lower()
                        while nombre in titulos or nombre == "":
                            print("Titulo Repetido o en blanco. Intentalo nuevamente... ")
                            nombre = input("Ingrese nuevamente un titulo").strip().lower()
                        
                        titulos.append(nombre)
                        ejemplares.append(0)



            case 2:
                if not titulos:
                    print("No hay titulos ingresados. Primero deben existir titulos para poder ingresar cantidad de ejemplares")
                    continue
                
                print("Recorriendo los titulos...")
                for i, titulo in enumerate(titulos):
                    print(f"{i + 1}. {titulo}")
                
                entrada = input("Seleccione el número de título para ingresar ejemplares: ")
                while not entrada.isdigit() or int(entrada) < 1 or int(entrada) > len(titulos):
                    print("Posición inválida, intente nuevamente..")
                    entrada = input("Seleccione el número de título para ingresar ejemplares: ")
                posicion = int(entrada)-1
                entrada_cantidad = input("Ingrese la cantidad de ejemplares que desea: ")
                while not entrada_cantidad.isdigit() or int(entrada_cantidad) <= 0:
                    print("Error: ingrese un número entero mayor a 0")
                    entrada_cantidad = input("Ingrese la cantidad de ejemplares que desea: ")
                cantidad = int(entrada_cantidad)
                ejemplares[posicion] = ejemplares[posicion] + cantidad
                print(f"ejemplares disponibles actualmente para {titulos[posicion]} : {ejemplares[posicion]}")



            case 3:
                if not titulos:
                    print("No hay titulos ingresados. Primero deben existir titulos para poder ingresar cantidad de ejemplares")
                    continue
                
                print("----MOSTRANDO CATÁLOGO DE LIBROS----")
                for i, titulo in enumerate(titulos):
                    print(f"{i + 1}. {titulo}")
                    

                        

            case 4:
                if not titulos:
                    print("No hay titulos ingresados. Primero deben existir titulos para poder ingresar cantidad de ejemplares")
                    continue
                 
                titulo_consulta = input("Ingresa el titulo a consultar").strip().lower()
                while True:
                    if titulo_consulta in titulos:
                        posicion = titulos.index(titulo_consulta)
                        print(f"Ejemplares disponible para {titulo_consulta}: {ejemplares[posicion]}")
                        break
                    
                    else: 
                        print(f"El titulo: {titulo_consulta} no se encuentra en el catálogo.")
                        print("¿Desea ingresarlo nuevamente? (S: vuelve a ingresar / N: vuelve al menú principal)" )

                        if input().upper() == "S":
                            titulo_consulta = input("Ingrese el titulo a consultar")
                        else:
                            break
            case 5:
                 if not titulos:
                    print("No hay titulos ingresados. Primero deben existir titulos para poder ingresar cantidad de ejemplares")
                    
                 
                 agotados = False

                 for i in ejemplares:
                     if i == 0:
                         agotados = True
                         break
                 if agotados:
                    print("Libros Agotados")
                    for titulo in titulos:
                        posicion = titulos.index(titulo)
                        if ejemplares[posicion] == 0:
                            print(titulo)
                  
            case 6:
                nuevo_titulo = input("Ingrese un nuevo titulo: ").strip().lower()
                if nuevo_titulo in titulos or nuevo_titulo == "":
                    print(f"El titulo ingresado {nuevo_titulo} ya existe o ingresaste un titulo en vacio")
                else:
                    titulos.append(nuevo_titulo)
                    entrada_cantidad = input(f"Ingrese cantidad de ejemplares para {nuevo_titulo}: ")
                    while not entrada_cantidad.isdigit() or int(entrada_cantidad) <= 0:
                       print("Error: Ingrese un número entero mayor a 0")
                       entrada_cantidad = input(f"Ingrese cantidad de ejemplares para {nuevo_titulo}: ")
                    cantidad = int(entrada_cantidad)
                    posicion = titulos.index(nuevo_titulo)
                    ejemplares.insert(posicion, cantidad)    
                    print(f"Titulo {nuevo_titulo} agregado al catalogo con {cantidad} ejemplares disponibles")
            case 7:
                if not titulos:
                    print("No hay titulos ingresados. Primero deben existir titulos para poder ingresar cantidad de ejemplares")
                    continue

                for i, titulo in enumerate(titulos, start=1):
                    print(f"{i}. {titulo}")
                
                entrada_posicion = input("Ingrese el número del libro")
                while not entrada_posicion.isdigit() or int(entrada_posicion) <= 0 or int(entrada_posicion) > len(titulos):
                    print("Posición invalida, intentalo nuevamente")
                    entrada_posicion = input("Seleccione nuevamente el número de titulo ")
                
                posicion = int(entrada_posicion) -1 
                
                accion = input("Ingrese 'P' para préstamo y 'D' para devolución").strip().upper()

                if accion == "P":
                    if ejemplares[posicion] > 0:
                        ejemplares[posicion] -= 1
                        print(f"Préstamo realizado. Ejemplares disponibles para: {titulos[posicion]}: {ejemplares[posicion]}")
                    else:
                        print(f"No hay ejemplares disponibles de {titulos[posicion]}")
                
                elif accion == "D":
                    ejemplares[posicion] += 1
                    print("Devolución realizada.")
                else:
                    print("Acción invalida. Use 'P' para prestamos, o 'D' para devolución ")
            case 8:
                print("Hasta luego!")
                break
            

                
                          

