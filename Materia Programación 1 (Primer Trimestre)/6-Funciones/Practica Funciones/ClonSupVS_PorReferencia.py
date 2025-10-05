
import copy


def modificar_lista(original, copia_shallow, copia_deep):
    original[0][0] = "x"
    copia_shallow[0][1] = "y"
    copia_deep[0][2] = "Z"

data = [[1,2,3], [4,5,6]]
copia_superficial = copy.copy(data)
copia_Prof = copy.deepcopy(data)

modificar_lista(data, copia_superficial, copia_Prof)

print("Original: ", data)
print("Copia Superficial: ", copia_superficial)
print("Copia Produnda: ", copia_Prof)
