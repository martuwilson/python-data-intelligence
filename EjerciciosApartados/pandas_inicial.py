## Objetivo general: aplicar filtros, crear columnas nuevas y practicar operaciones simples de dataframes

import pandas as pd

## 1 - Cargar CSV generado previamente arriba.
path = r"C:\Users\004543613\Desktop\python_data_intelligence\EjerciciosApartados\ventas.csv"
ventas_dataframe = pd.read_csv(path)

## 2 - Mostrar cuantas filas y columnas tiene el DataFrame
print("Shape del DataFrame de Ventas (filas, columnas):")
print(ventas_dataframe.shape) ## shape retorna una tupla con (filas, columnas)

## 3- Filtrar productos vendidos en Rosario
ventas_rosario = ventas_dataframe[ventas_dataframe["ciudad"] == "Rosario"] ## puede hacerse con .loc también
print("\nVentas en Rosario:")
print(ventas_rosario)

## 4 - crear columna nueva llamada "total_venta" 
ventas_dataframe["total_venta"] = ventas_dataframe["unidades_vendidas"] * ventas_dataframe["precio_unitario"]
print("\nDataFrame con columna 'total_venta' agregada:")
print(ventas_dataframe)

## 5 - Mostrar columnas especificas: "producto", "unidades_vendidas", "total_venta"
columnas_especificas = ventas_dataframe[["producto", "unidades_vendidas", "total_venta"]]
print("\nColumnas específicas (producto, unidades_vendidas, total_venta):")
print(columnas_especificas)

## 6 - Filtrar ventas donde "unidades_vendidas" > 50
ventas_filtro = ventas_dataframe[ventas_dataframe["unidades_vendidas"] > 50]
print("\nVentas con más de 50 unidades vendidas:")
print(ventas_filtro)

