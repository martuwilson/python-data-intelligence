import pandas as pd

datos_clima = pd.read_csv(r"C:\Users\004543613\Downloads\Precipitaciones.csv")
##print(datos_clima)

""" datos_clima.head()  ## primeras 5 filas
datos_clima.tail()  ## ultimas 5 filas
datos_clima.shape  ## (filas, columnas)
datos_clima.columns  ## nombres de las columnas """
datos_clima.describe()  ## estadisticas descriptivas de las columnas numericas
##print(datos_clima.describe())

################
## Extraer la primera fila de datos_clima y guardarla en una variable llamada head_df

head_df = datos_clima.head(1)
print("Primera fila del DataFrame:")
print(head_df)

## extraer ultima fila y guardarla en una variable llamada tail_df
tail_df = datos_clima.tail(1)
print("\nÚltima fila del DataFrame:")
print(tail_df)