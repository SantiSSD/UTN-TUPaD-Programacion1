def repetir(num,frase):
    if num >= 1:
        print(frase)
        repetir(num -1, frase)


repetir(5, "Hola mundo")
