
precios = { 

    "manzana" : 3.5,
    "banana": 2.0,
    "naranja": 4.0,
}
precios["banana"] = precios["banana"] + 1
precios["pera"] = 2.5

del precios["naranja"]

print(precios)