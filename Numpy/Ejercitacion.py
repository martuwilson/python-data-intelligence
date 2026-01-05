import pandas as pd
import numpy as np

datos = {
    "Ciudad": ["Ciudad de México", "Buenos Aires", "Río de Janeiro", "Lima", "Bogotá", "Santiago de Chile", "São Paulo", "La Habana", "Cancún", "Cartagena"],
    "País": ["México", "Argentina", "Brasil", "Perú", "Colombia", "Chile", "Brasil", "Cuba", "México", "Colombia"],
    "Población": [9265833, 3059574, 6748314, 9756020, 7181663, 6199241, 12333146, 2164182, 888124, 1036671],
    "Visitantes": [21000000, 15000000, 13000000, 9000000, 8000000, 7500000, 20000000, 4000000, 5000000, 3000000]
}

""" 
Utilizando los métodos adecuados de numpy  para calcular el promedio de la población de todas estas ciudades
y redondea el resultado, el cual debes almacenar en una variable llamada: promedio_poblacion
"""

df = pd.DataFrame(datos)
promedio_poblacion = np.round(np.mean(df["Población"]))
print("El promedio de la población de las ciudades es:", promedio_poblacion)

## Valor minimo de visitantes
min_visitantes = np.min(df["Visitantes"])
print("El valor mínimo de visitantes es:", min_visitantes)

## Valor maximo de visitantes
max_visitantes = np.max(df["Visitantes"])
print("El valor máximo de visitantes es:", max_visitantes)