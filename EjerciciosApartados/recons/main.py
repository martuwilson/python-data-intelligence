##Ejercicio Integrado: “Presupuesto vs Real – Contaduría Global”

## Parte 1 - Carga y exploracion
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Leer CSV
df = pd.read_csv('presupuesto_vs_real_EMPRESA.csv')

#Primeras 5 filas
#print(df.head())

#Dimensiones
#print(f"Dimensiones del DataFrame: {df.shape}") #(180,13) -> 180 filas, 13 columnas

#Info de columnas y nulos
#print(df.info()) # Información general del DataFrame
#print(df.isna().sum()) # Recuento de valores nulos por columna
#print((df.isna().mean() * 100).round(2)) # Porcentaje de valores nulos por columna

## Estadisticas de numericas
#print(df.describe().round(2)) # Estadísticas descriptivas de columnas numéricas
## Comentario: count da 171,172 y 180 respectivamente, por lo que hay nulos en esas columnas.

#Valores únicos en categóricas clave
#print("Valores únicos: ", df[['pais', 'unidad_negocio', 'rubro', 'moneda']].nunique())
#print("Valores únicos pais:", df['pais'].unique())


#Parte 2 - Limpieza y normalización
#Normalizacion básica de textos (no tengan espacios adelante/atras,todo en minusculas, no tengas tildes)
def normalize_text(text):
    if isinstance(text, str):
        text = text.strip().lower()
        text = text.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
        text = text.replace('ñ', 'n')
    return text
for col in ['pais', 'unidad_negocio', 'rubro', 'moneda', 'proveedor', 'aprobador']:
    df[col] = df[col].apply(normalize_text)
    
#Arreglar paises inconsistentes
df['pais'] = df['pais'].replace({
    'Brasil': 'brasil',
    'BRASIL': 'brasil',
    'México': 'mexico',
    'Argentina': 'argentina',
    'Colombia': 'colombia',
    'Chile': 'chile',
    'Perú': 'peru'
}) 

#Convertir fecha_reporte a datetime
df['fecha_reporte'] = pd.to_datetime(df['fecha_reporte'], errors='coerce', dayfirst=True, format='mixed')

#Crear columna periodo_dt (rear una columna nueva con la fecha representativa del mes (por ejemplo, primer día del mes).)
df['periodo_dt'] = pd.to_datetime(df['periodo'] + '-01', format='%Y-%m-%d', errors='coerce')

#Imputar tipo_cambio_local faltante (con el promedio del pais correspondiente)
df['tipo_cambio_local'] = df.groupby('pais')['tipo_cambio_local'].transform(
    lambda x: x.fillna(x.mean())
)

#Verificar limpieza
""" print(df.info())
print(df.isna().sum())
print(df.head())
print(df.dtypes) """

## PARTE 3
#Crear columna margen_usd
df['margen_usd'] = df['real_usd'] - df['presupuesto_usd']

#crear var_pct (cuidado con los 0 o NaN)
df['var_pct'] = np.where(
    df['presupuesto_usd'] > 0,
    (df['margen_usd'] / df['presupuesto_usd']) * 100,
    np.nan
)

#crear columna real_local
df['real_local'] = df['real_usd'] * df['tipo_cambio_local']

#clasificar la ejecucion en tramos -> crear coluna tramo_var segun la variacion %
def classificar_variacion(var_pct):
    if pd.isna(var_pct):
        return 'sin_dato'
    elif var_pct < -20:
        return 'sub-ejecucion fuerte'
    elif -20 <= var_pct < 20:
        return 'ejecucion normal'
    elif var_pct >= 20:
        return 'sobre-ejecucion'
    
df['tramo_var'] = df['var_pct'].apply(classificar_variacion)

#Detectar outliers en real_usd usando Z-score por país
df['z_real_usd'] = df.groupby('pais')['real_usd'].transform(
    lambda x: (x - x.mean()) / x.std()
)
outliers = df[df['z_real_usd'].abs() > 3]
#print("Outliers detectados:\n", outliers[['pais', 'real_usd', 'z_real_usd']])

""" 3.6 — Mini chequeo final

Tarea:
Mostrar las primeras filas con las nuevas columnas:

margen_usd

var_pct

real_local

tramo_var

z_real_usd """

df[['presupuesto_usd','real_usd','margen_usd','var_pct','tramo_var','z_real_usd']].head()
print(df[['pais','presupuesto_usd','real_usd','margen_usd','var_pct','tramo_var','z_real_usd']].head())