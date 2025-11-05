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
# print("\nInformación general del DataFrame:")
# print(gastos_df.info())
# print("\nValores nulos por columna:\n", gastos_df.isnull().sum())

#Mostrar estadísticas básicas de las columnas numéricas.
# print("\nDescripción estadística:\n", gastos_df.describe())

#Extras:
# Valores unicos por columnas
# print("\nValores únicos por columna:")
""" for columna in gastos_df.columns:
    print(f" - {columna}: {gastos_df[columna].nunique()} únicos")
 """
# Revisar duplicados
duplicados = gastos_df.duplicated().sum()
# print(f"\nCantidad de filas duplicadas: {duplicados}")

## Parte 2: Limpieza y normalización de datos

#Estandarizar los nombres de países y meses (todo en minúscula y sin espacios).
gastos_df['pais'] = gastos_df['pais'].str.strip().str.lower()
gastos_df['mes'] = gastos_df['mes'].str.strip().str.lower()

# Reemplazar los NaN de tipo_cambio_local por la media del tipo de cambio por país.
gastos_df['tipo_cambio_local'] = gastos_df.groupby('pais')['tipo_cambio_local'].transform(
    lambda x: x.fillna(x.mean())
)

# Reemplazar NaN en ingresos_usd o gastos_operativos_usd por 0 temporalmente.
gastos_df['ingresos_usd'] = gastos_df['ingresos_usd'].fillna(0)
gastos_df['gastos_operativos_usd'] = gastos_df['gastos_operativos_usd'].fillna(0)

# Convertir la columna fecha_reporte a tipo datetime.
gastos_df['fecha_reporte'] = pd.to_datetime(gastos_df['fecha_reporte'], errors='coerce')

# Eliminar filas donde país o centro_costo estén vacíos.
gastos_df = gastos_df.dropna(subset=['pais', 'centro_costo'])

#Mas sugerencias
# Capitalizar nombres de países
gastos_df['pais'] = gastos_df['pais'].str.title()

# Revisar si quedaron fechas no convertidas (NaT)
print("Fechas no convertidas:", gastos_df['fecha_reporte'].isna().sum())
