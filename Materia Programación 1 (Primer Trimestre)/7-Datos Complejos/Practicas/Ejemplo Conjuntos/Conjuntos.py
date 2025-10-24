
# Crear conjunto
# c = {1,2,3,4}
# print(c)

# Los repetidos los ignora
# c = {1,2,2,2,3,4,5}
# print(c)

# Conjunto vacio
# c = set()
# print(c)


# Convertimos una lista
# l = [1,2,2,2,3,4,5,6,7,8]
# c = set(l)

# print(c)


# Operaciones

c = set()
c.add("Pedro")
c.add("Santiago")
c.add("Gonzalo")
c.add("Rodrigo")
c.add("Lautaro")
c.add("Lautaro")
print(c)


# Eliminacion de un elemento
# podemos usar c.discard que te elimina un elemento y en caso de que no exista no te arroja un error 
# o podemos usar remove que si en caso de que el elemento no exista te va a tirar error
c.discard("Pedro")
print(c)

print(len(c))


# Tambien tenemos la función clear que elimina todos los elementos del conjunto

# c.clear()
# print(c)

# Como recorrer un conjunto?

# for i in c:
#     print(i)

# verificar si un elemento existe en el conjunto

frutas = {"manzana","Pera","Mandarina"}

if "manzana" in frutas:
    print("Existe este elemento en el conjunto")
else:
    print("No existe este elemento en el conjunto")