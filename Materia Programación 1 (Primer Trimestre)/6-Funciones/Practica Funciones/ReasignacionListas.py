def remplazar_sublista(matriz):
    matriz[0] = [0,0,0] #Reasignacion interna, remplaza la referencia


matriz = [[1,2], [3,4]]
remplazar_sublista(matriz)
print("Matriz modificada", matriz)