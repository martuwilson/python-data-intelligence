# Importacion de librerias 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = r"C:\Users\004543613\Desktop\python_data_intelligence\EjerciciosApartados\contaduria\gastos_globales.csv"

#Lectura csv a df
gastos_df = pd.read_csv(path)

#Print de los primeros 10 registros
# print("Primeros 10 registros:\n", gastos_df.head(10))

# Verificar info general del df y detectar columnas con nulos
print("\nInformación general del DataFrame:")
print(gastos_df.info())
print("\nValores nulos por columna:\n", gastos_df.isnull().sum())

#Mostrar estadísticas básicas de las columnas numéricas.
print("\nDescripción estadística:\n", gastos_df.describe())

#Extras:
# Valores unicos por columnas
print("\nValores únicos por columna:")
for columna in gastos_df.columns:
    print(f" - {columna}: {gastos_df[columna].nunique()} únicos")

# Revisar duplicados
duplicados = gastos_df.duplicated().sum()
print(f"\nCantidad de filas duplicadas: {duplicados}")

