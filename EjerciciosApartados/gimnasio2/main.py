#1 Importacion de librerias a usar

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#2 Cargar los datos desde un archivo CSV
ruta = r"C:\Users\Martin\Desktop\Python\python-data-intelligence\EjerciciosApartados\gimnasio2\socios_gimnasio.csv"
gimnasio_df = pd.read_csv(ruta)

# 3 Verificar la carga de datos
# print(gimnasio_df.head()) -> check, carga el csv

# ver duplicados y eliminarlos
duplicados = gimnasio_df.duplicated() # Devuelve una serie booleana indicando filas duplicadas
num_duplicados = duplicados.sum() # Cuenta cuántos duplicados hay
#print(f"Número de filas duplicadas: {num_duplicados}")
gimnasio_df = gimnasio_df.drop_duplicates() # Elimina filas duplicadas

# 4 chequear si hay valores faltantes
gimnasio_df.fillna(gimnasio_df.mean(numeric_only=True), inplace=True)
""" if gimnasio_df.isnull().sum().sum() == 0:
    print("No hay valores faltantes en el DataFrame después de la imputación.")
else:
    print("Todavía hay valores faltantes en el DataFrame después de la imputación.") """
    
# PANORAMA GENERAL DEL DATAFRAME
""" print("\nInformación general del DataFrame después de la limpieza:")
print(gimnasio_df.describe()) """

