import pandas as pd
import numpy as np

# Cargar el archivo CSV
path= r"/Users/martinezequielwilliner/Desktop/personal/data_analyst/EjerciciosApartados/ventas2/ventas_sucias.csv"
df = pd.read_csv(path);

# Mostrar las primeras filas del DataFrame
#print(df.head())

#EDA clasico:
print("\nInformación general del DataFrame:")
# Primeras 5 filas
print('Primeras 5 filas:\n', df.head())

#Cantidad de filas y columnas
print('\nShape (filas, columnas):', df.shape)

#Columnas con nulos
print('\nValores nulos por columna:\n', df.isnull().sum())

#Tipo de dato de cada columna
print('\nTipos de datos:\n', df.dtypes) 

#Descripción estadística de las columnas numéricas
print('\nDescripción estadística:\n', df.describe())

# Ver valores únicos en columnas categóricas clave
for col in ['status', 'region', 'product_category']:
    print(f"\nValores únicos en '{col}':")
    print(df[col].value_counts())
