ciudades = [
    "New York",
    "Paris",
    "Tokyo",
    "London",
    "Sydney"
]

print(ciudades[0])
print(ciudades[4])

#######################################
numeros = [1, 2, 3, 4, 5]
print(numeros)

numeros.append(6)
print(numeros)

numeros.remove(1)
print(numeros)

##Insertar numero 7 en la posicion 1
numeros.insert(1, 7)
print(numeros)

##Ordernar lista
numeros.sort()
print(numeros)

####################################################
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

combinada = lista1 + lista2
print(combinada)

repetida = lista1 * 3
print(repetida)

sublista = combinada[1:4]
print(sublista)