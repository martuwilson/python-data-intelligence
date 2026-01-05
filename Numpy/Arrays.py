## crear un array entero con primeros 10 números enteros positivos, comenzando desde el 1.
import numpy as np

array_enteros = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Array de enteros:", array_enteros)

##Forma del array (shape)

forma_array = array_enteros.shape
print("Forma del array:", forma_array)

## array bidimensional de 3x3 con números enteros del 1 al 9.
array_bidimensional = np.array([[1, 2, 3],
                               [4, 5, 6],
                               [7, 8, 9]])
print("Array bidimensional 3x3:\n", array_bidimensional)

## Largo array bidimensional
print(len(array_bidimensional))

## Forma del array bidimensional
forma_array_bidimensional = array_bidimensional.shape
print("Forma del array bidimensional:", forma_array_bidimensional)