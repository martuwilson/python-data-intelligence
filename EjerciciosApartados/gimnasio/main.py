# Ejercicio Integrador - Gimnasio
# Objetivo: limpiar, transformar y analizar datos de un gimnasio

# 1 - Importar librerías necesarias
import pandas as pd
import numpy as np

# 2 - Cargar el CSV en un dataframe
path= r"C:\Users\004543613\Desktop\python_data_intelligence\EjerciciosApartados\gimnasio\socios_gimnasio.csv"
df = pd.read_csv(path);

# 3 - Mostrar info general:
#print("\nInformación general del DataFrame:")
# Primeras 5 filas
#print('Primeras 5 filas:\n', df.head())
#Tipos de datos
#print('\nTipos de datos:\n', df.dtypes)
# Cantidad de filas y columnas
#print('\nShape (filas, columnas):', df.shape)
# Descripcion estadistica
#print('\nDescripción estadística:\n', df.describe())
# Cantidad de valores nulos
#print('\nValores nulos por columna:\n', df.isnull().sum())

# PARTE 2: Limpieza de datos
# 1 - Verificar y rellenar los valores nulos
#En asistencias_mes los nulos pasan a ser mediana general
df['asistencias_mes'] = df['asistencias_mes'].fillna(df['asistencias_mes'].median())  # Sin inplace, reasignamos
#En peso_kg y altura_m: reemplazá por el promedio del grupo según sexo.
df['peso_kg'] = df.groupby('sexo')['peso_kg'].transform(lambda x: x.fillna(x.mean()))
df['altura_m'] = df.groupby('sexo')['altura_m'].transform(lambda x: x.fillna(x.mean()))

# 2 - Fecha de inscripción: convertir a formato datetime
df['fecha_registro'] = pd.to_datetime(df['fecha_registro'])

# 3 - agregado por mi, pasar a strings los datos que requieren
df['sexo'] = df['sexo'].astype('string') #antes aparecia como object pero es mejor string para usar metodos de string
df['nombre'] = df['nombre'].astype('string')
df['plan'] = df['plan'].astype('string')

# re imprimir info para verificar cambios
#print("\nInformación del DataFrame después de la limpieza:")
# Ver si hay nulos
#print('\nValores nulos por columna:\n', df.isnull().sum())
# Ver tipos de datos
#print('\nTipos de datos:\n', df.dtypes)

# PARTE 3 : Columnas derivadas
# 1 - calcular imc y agregar como nueva columna
df['imc'] = df['peso_kg'] / (df['altura_m'] ** 2)
df['imc'] = df['imc'].round(2)  # Redondear a 2 decimales

# clasificar IMC segun rangos:
""" 
<18.5: “Bajo peso”
18.5–24.9: “Normal”
25–29.9: “Sobrepeso”
>=30: “Obesidad”
"""

condiciones = [
    df['imc'] < 18.5,
    (df['imc'] >= 18.5) & (df['imc'] <= 24.9),
    (df['imc'] >= 25) & (df['imc'] <= 29.9),
    df['imc'] >= 30
]

categorias = ['Bajo peso', 'Normal', 'Sobrepeso', 'Obesidad']

# Agregamos default='Desconocido' para que sea del mismo tipo (string) que las categorías
df['categoria_imc'] = np.select(condiciones, categorias, default='Desconocido')

# 3 - Calculá una columna antiguedad_meses con cuántos meses lleva cada socio activo:
df['antiguedad_meses'] = ((pd.Timestamp.now() - df['fecha_registro']).dt.days / 30).astype(int)

# PARTE 4 - Agrupaciones y estadísticas
""" 1 Mostrá el promedio de asistencias mensuales por plan.

2 Mostrá el IMC promedio por sexo.

3 Identificá:

 a- El socio con mayor cantidad de asistencias.

 b- El socio con mayor IMC.

4 - Calculá la correlación entre edad, asistencias_mes, imc y antiguedad_meses. """

# 1 - Promedio de asistencias mensuales por plan
promedios_asistencia_plan = df.groupby('plan')['asistencias_mes'].mean().round(2)
print("Promedio de asistencias mensuales por plan:")
print(promedios_asistencia_plan)

# 2 - IMC promedio por sexo
imc_promedio_sexo = df.groupby('sexo')['imc'].mean().round(2)
print("\nIMC promedio por sexo:")
print(imc_promedio_sexo)

# 3a - Socio con mayor cantidad de asistencias
socio_mas_asistencias = df.loc[df['asistencias_mes'].idxmax()]
print("\nSocio con mayor cantidad de asistencias mensuales:")
print(socio_mas_asistencias[['nombre', 'asistencias_mes']])
# 3b - Socio con mayor IMC
socio_mayor_imc = df.loc[df['imc'].idxmax()]
print("\nSocio con mayor IMC:")
print(socio_mayor_imc[['nombre', 'imc']])
# 4 - Correlación entre edad, asistencias_mes, imc y antiguedad_meses
correlacion = df[['edad', 'asistencias_mes', 'imc', 'antiguedad_meses']].corr() # corr -> calcula la correlacion entre columnas numericas
print("\nCorrelación entre edad, asistencias_mes, imc y antiguedad_meses:")
print(correlacion)

