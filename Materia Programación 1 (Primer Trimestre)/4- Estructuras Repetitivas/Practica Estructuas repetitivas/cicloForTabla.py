"Desarrollar un algoritmo que permita ingresar un numero entero entre"
" 1 y 10 (inclusive) la computadora debe mostrar la tabla de multiplicador del numero ingresado "

numero = int(input("Ingrese un numero del 1 al 10"))

if numero > 0 and numero <=10:
    for contador in range(1,11):
        tabla = numero * contador        
        print(f"{numero} X {contador} = {tabla}")
else:
    print("Ingrese un numero del 1 al 10 porfavor....")
