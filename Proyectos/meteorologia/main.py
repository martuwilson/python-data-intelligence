import pandas as pd
import numpy as np

## 1- crear el dataframe con los datos meteorológicos
path = r"C:\Users\004543613\Desktop\python_data_intelligence\Proyectos\meteorologia\datos_meteorologicos.csv"
df = pd.read_csv(path)

## 2- explorar los datos
""" print('Head:', df.head())
print('\nInfo:')
print(df.info())
print('\nDescribe:')
print(df.describe()) """

## 3- convertir las columnas del dataframe en array de numpy
temperaturas = df['Temperatura'].to_numpy()
precipitaciones = df['Precipitación'].to_numpy()
humedades = df['Humedad'].to_numpy()

## Identificar los datos faltantes en los arrays y reemplazarlos con el promedio de los valores del respectivo array

# a - nulos de cada array
temperaturas_nulo = np.isnan(temperaturas)
precipitaciones_nulo = np.isnan(precipitaciones)
humedades_nulo = np.isnan(humedades)

#b - promedios de cada array (ignorando nulos)
promedio_temperaturas = np.nanmean(temperaturas)
promedio_precipitaciones = np.nanmean(precipitaciones)
promedio_humedades = np.nanmean(humedades)

# c - reemplazar nulos con promedios
temperaturas[temperaturas_nulo] = promedio_temperaturas ## de temperaturas , agarra los datos nulos y los reemplaza con el promedio
precipitaciones[precipitaciones_nulo] = promedio_precipitaciones
humedades[humedades_nulo] = promedio_humedades

## 5 - analisis estadisticos basicos
# a- temperatura promedio
temperaturas_promedio = np.mean(temperaturas)
print(f'Temperatura Promedio: {temperaturas_promedio:.2f} °C')

# b- precipitacion total
precipitaciones_totales = np.sum(precipitaciones)
print(f'Precipitación Total: {precipitaciones_totales:.2f} mm')

# c- humedad maxima y minima
humedad_maxima = np.max(humedades) 
humedad_minima = np.min(humedades) 
print(f'Humedad Máxima: {humedad_maxima:.2f} %')
print(f'Humedad Mínima: {humedad_minima:.2f} %')

# d - fecha mas calurosa
mas_calor = np.max(temperaturas)

#registro de la temperatura mas alta
indice_mas_calor = np.where(temperaturas == mas_calor)[0][0]

# fecha correspondiente mas calor
fecha_mas_calor = df.iloc[indice_mas_calor]['Fecha']
print(f'La fecha más calurosa fue: {fecha_mas_calor} con {mas_calor:.2f} °C')

## 6- fecha mas fria

mas_frio = np.min(temperaturas)
indice_mas_frio = np.where(temperaturas == mas_frio)[0][0]
fecha_mas_frio = df.iloc[indice_mas_frio]['Fecha']
print(f'La fecha más fría fue: {fecha_mas_frio} con {mas_frio:.2f} °C')

## 7 - exportar los datos limpios a un nuevo archivo CSV
df_limpio = pd.DataFrame({
    'Fecha': df['Fecha'],
    'Temperatura': temperaturas,
    'Precipitación': precipitaciones,
    'Humedad': humedades
})

output_path = r"C:\Users\004543613\Desktop\python_data_intelligence\Proyectos\meteorologia\datos_meteorologicos_limpios.csv"
df_limpio.to_csv(output_path, index=False)
print(f'Datos limpios exportados a: {output_path}')