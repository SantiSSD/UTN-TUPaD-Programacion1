# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
# último pasa a ser el primero).

numeros = [1,2,3,4,5,6,7]

ultimo_numero = numeros[-1]

resto = numeros[0:6]

print(ultimo_numero)
print(resto)

nueva_lista = [ultimo_numero] + resto

print(nueva_lista)