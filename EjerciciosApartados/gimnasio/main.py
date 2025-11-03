# Ejercicio Integrador - Gimnasio
# Objetivo: limpiar, transformar y analizar datos de un gimnasio

# 1 - Importar librerías necesarias
import pandas as pd
import numpy as np

# 2 - Cargar el CSV en un dataframe
path= r"C:\Users\004543613\Desktop\python_data_intelligence\EjerciciosApartados\gimnasio\socios_gimnasio.csv"
df = pd.read_csv(path);

# 3 - Mostrar info general:
print("\nInformación general del DataFrame:")
# Primeras 5 filas
print('Primeras 5 filas:\n', df.head())
#Tipos de datos
print('\nTipos de datos:\n', df.dtypes)
# Cantidad de filas y columnas
print('\nShape (filas, columnas):', df.shape)
# Descripcion estadistica
print('\nDescripción estadística:\n', df.describe())
# Cantidad de valores nulos
print('\nValores nulos por columna:\n', df.isnull().sum())