import pandas as pd

## Cargar data
df = pd.read_csv(r"C:\Users\004543613\Downloads\medallas.csv")
##print(df.head())

## 2: exploracion inicial:
""" print("Shape: ", df.shape) ## shape retorna una tupla con (filas, columnas)
print("Info: ", df.info()) ## informacion general del dataframe
print("Describe: ", df.describe()) ## estadisticas descriptivas de columnas numericas
print("Nulls: ", df.isnull().sum()) ## conteo de valores nulos por columna

 """

## 3: LIMPIEZA DE DATOS

## Reemplazar valores no validos
df.fillna(0, inplace=True) ## rellena valores nulos con 0
##print(df_relleno.isnull().sum())

## corregir tipos de datos:
df["Oro"] = df["Oro"].astype(int)
df["Plata"] = df["Plata"].astype(int)
df["Bronce"] = df["Bronce"].astype(int)
print(df)

##Medallas de oro por pais
top_3_oro = df.sort_values('Oro', ascending=False).head(3)
print("\nTop 3 países con más medallas de oro:")
print(top_3_oro)

## Medallas totales por pais

filtro = df["Total"] > 10
mas_10_medallas = df[filtro].sort_values('Total', ascending=False)
print("\nPaíses con más de 10 medallas en total:")
print(mas_10_medallas)

##Cuál es la desviación standard (std) de la columna "Total"?
std_total = df["Total"].std()
print(f"\nDesviación estándar de medallas totales: {std_total:.2f}")