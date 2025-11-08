import os
def listar_archivos(directorio,lista):
    for elemento in os.listdir(directorio):
        ruta = os.path.join(directorio, elemento)
        if os.path.isdir(ruta):
            print(f"Direccion padre: {ruta}")
            print("----------------------------------")
            listar_archivos(ruta,lista)
        else:
            lista.append(ruta)
            print(ruta)




lista_rutas = []
listar_archivos(r"D:\Demostracion", lista_rutas)    
print (lista_rutas)