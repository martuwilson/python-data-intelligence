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
#print("Fechas no convertidas:", gastos_df['fecha_reporte'].isna().sum())

## COMO QUEDARON NAT lo mejor es ahora rellenar por MODA por pais
gastos_df['fecha_reporte'] = gastos_df.groupby('pais')['fecha_reporte'].transform(
    lambda x: x.fillna(x.mode().iloc[0]  if not x.mode().empty else pd.Timestamp('2020-01-01')
)) ## se lee: para cada pais, en la columna fecha_reporte, rellena los NaT con la moda de esa columna para ese pais, si no hay moda (columna vacia) rellena con fecha fija 2020-01-01
#iloc es para tomar el primer valor de la serie resultante de mode()

##PARTE 3

# Crear una columna margen_operativo_usd = ingresos_usd - gastos_operativos_usd (con numpy)
gastos_df['margen_operativo_usd'] = np.where(
    (gastos_df['ingresos_usd'].notna()) & (gastos_df['gastos_operativos_usd'].notna()),
    gastos_df['ingresos_usd'] - gastos_df['gastos_operativos_usd'],
    np.nan
)

#print("\nDataFrame con margen operativo:\n", gastos_df.head())

# Crear una columna gasto_local = gastos_operativos_usd * tipo_cambio_local. ocn numpy
## FORMA FACIL: gastos_df['gastos_local'] = gastos_df['gastos_operativos_usd'] * gastos_df['tipo_cambio_local']

gastos_df['gastos_local'] = np.where(
    (gastos_df['gastos_operativos_usd'].notna()) & (gastos_df['tipo_cambio_local'].notna()),
    gastos_df['gastos_operativos_usd'] * gastos_df['tipo_cambio_local'],
    np.nan
)

# Redondear todas las cifras a 2 decimales donde sean columnas numericas
columnas_numericas = []

for columnas in gastos_df.select_dtypes(include=[np.number]).columns:
    columnas_numericas.append(columnas)
    gastos_df[columnas] = gastos_df[columnas].round(2)


""" 

Clasificar el nivel de rentabilidad según el margen:

< 0 → "Pérdida"

0 - 5000 → "Margen Bajo"

> 5000 → "Rentable"

"""

condiciones = [
    gastos_df['margen_operativo_usd'] < 0,
    (gastos_df['margen_operativo_usd'] >= 0) & (gastos_df['margen_operativo_usd'] <= 5000),
    gastos_df['margen_operativo_usd'] > 5000
]

categorias = ['Pérdida', 'Margen Bajo', 'Rentable']

gastos_df['nivel_rentabilidad'] = np.select(condiciones, categorias, default='Desconocido')


#PARTE 4
# Margen operativo promedio por pais
margen_promedio_pais = gastos_df.groupby('pais')['margen_operativo_usd'].mean().round(2)
#print("Margen operativo promedio por país:\n", margen_promedio_pais)

# clasificacion de margen promedio por pais 
clasificacion_margen = pd.DataFrame({
    'pais': margen_promedio_pais.index,
    'margen_promedio_usd': margen_promedio_pais.values
})

condiciones_clasificacion = [
    clasificacion_margen['margen_promedio_usd'] < 0,
    (clasificacion_margen['margen_promedio_usd'] >= 0) & (clasificacion_margen['margen_promedio_usd'] <= 5000),
    clasificacion_margen['margen_promedio_usd'] > 5000
]

categorias_clasificacion = ['Pérdida', 'Margen Bajo', 'Rentable']

clasificacion_margen['clasificacion'] = np.select(condiciones_clasificacion, categorias_clasificacion, default='Desconocido')

#print("\nClasificación de países según margen operativo promedio:\n", clasificacion_margen)

# Mostrar el gasto total por mes (ya normalizado).

gasto_total_mes = gastos_df.groupby('mes')['gastos_local'].sum().round(2)
#print("\nGasto total por mes (normalizado):\n", gasto_total_mes)

# Identificar el centro de costo con mayor margen total.
#1 - Calcular el margen total por centro de costo
margen_total_centro = gastos_df.groupby('centro_costo')['margen_operativo_usd'].sum()

#2 - Identificar el centro de costo con el mayor margen total
centro_mayor_margen = margen_total_centro.idxmax()

#3 - Obtener el valor del mayor margen total
valor_mayor_margen = margen_total_centro.max()

#4 saber de donde es el centro de costo
centro_info = gastos_df[gastos_df['centro_costo'] == centro_mayor_margen].iloc[0]
pais_centro = centro_info['pais']
#print(f"\nCentro de costo con mayor margen total: {centro_mayor_margen} en {pais_centro} con un margen de {valor_mayor_margen:.2f} USD")

# Calcular el porcentaje de gastos sobre ingresos (gastos/ingresos * 100) por país.

gastos_ingresos_pais = gastos_df.groupby('pais').apply(
    lambda x: (x['gastos_operativos_usd'].sum() / x['ingresos_usd'].sum()) * 100 if x['ingresos_usd'].sum() != 0 else np.nan
).round(2)

#print("\nPorcentaje de gastos sobre ingresos por país:\n", gastos_ingresos_pais)

# Mostrar los 3 países más rentables y los 3 menos rentables.

pais_rentabilidad = gastos_df.groupby('pais')['margen_operativo_usd'].sum().round(2)
pais_rentabilidad_ordenado = pais_rentabilidad.sort_values(ascending=False)
top_3_rentables = pais_rentabilidad_ordenado.head(3)
top_3_menos_rentables = pais_rentabilidad_ordenado.tail(3)

#print("\nTop 3 países más rentables:\n", top_3_rentables)
#print("\nTop 3 países menos rentables:\n", top_3_menos_rentables)


## PARTE 5 - Visualización de resultados
#Gráfico de barras: gastos_operativos_usd promedio por país.
gastos_promedio_pais = gastos_df.groupby('pais')['gastos_operativos_usd'].mean().round(2)
plt.figure(figsize=(10, 6))
gastos_promedio_pais.plot(kind='bar', color='skyblue')
plt.title('Gastos Operativos Promedio por País')
plt.xlabel('País')
plt.ylabel('Gastos Operativos Promedio (USD)')
plt.xticks(rotation=45)
plt.tight_layout()


# Gráfico de líneas: ingresos_usd promedio por mes.
ingresos_promedio_mes = gastos_df.groupby('mes')['ingresos_usd'].mean().round(2)
plt.figure(figsize=(10, 6))
ingresos_promedio_mes.plot(kind='line', marker='o', color='orange')
plt.title('Ingresos Promedio por Mes')
plt.xlabel('Mes')
plt.ylabel('Ingresos Promedio (USD)')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()

#Gráfico de dispersión: relación entre gastos e ingresos.
plt.figure(figsize=(10, 6))
plt.scatter(gastos_df['ingresos_usd'], gastos_df['gastos_operativos_usd'], alpha=0.6, color='green')
plt.title('Relación entre Ingresos y Gastos Operativos')
plt.xlabel('Ingresos (USD)')
plt.ylabel('Gastos Operativos (USD)')
plt.grid()
plt.tight_layout()

#Gráfico circular: distribución de niveles de rentabilidad.
nivel_rentabilidad_counts = gastos_df['nivel_rentabilidad'].value_counts()
plt.figure(figsize=(8, 8))
nivel_rentabilidad_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['red', 'yellow', 'green'])
plt.title('Distribución de Niveles de Rentabilidad')
plt.ylabel('')  # Ocultar la etiqueta del eje y
plt.tight_layout()

plt.show()