lista = [1,2,3,4,5,6,7]

print("Lista ordenada:")
print(lista)

# pedimos al usuario un numero de la lista 

numero_solicitado = int(input("Ingrese un numero para encontrar en la lista"))

# Inicializamos las variables que utilizaremos en el algoritmo de busqueda binaria

# primer indice de la lista

indice_inicio = 0

indice_final = len(lista) - 1

indice_encontrado = -1



while(indice_inicio <= indice_final) and (indice_encontrado == -1):

    # calculamos el indice del medio
    indice_medio = (indice_inicio + indice_final) // 2

    # Comparamos el valor en la posicion del medio con el valor buscado
    if lista[indice_medio] == numero_solicitado:
        # si son iguales, encontramos el numero y guardamos en que indice lo encontramos
        indice_encontrado = indice_medio
    else:
        # si no lo encontramos, decidimos en que mitad seguir buscando
        if lista[indice_medio] < numero_solicitado:
            # si el valor en medio es menor, bucamos la mitad derecha
            indice_inicio = indice_medio+ 1
        else:
            # si el valor del medio es mayor, buscamos en la mitad izquierda
            indice_final = indice_medio - 1

print()
# Mostramos el resultado final

if indice_encontrado == -1:
    print("No se encuentra el número en la lista")
else:
    print("Numero encontrado! Esta en la posicion: ", indice_encontrado )