#1 Importacion de librerias a usar

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#2 Cargar los datos desde un archivo CSV
ruta = r"C:\Users\Martin\Desktop\Python\python-data-intelligence\EjerciciosApartados\gimnasio2\socios_gimnasio.csv"
gimnasio_df = pd.read_csv(ruta)

# 3 Verificar la carga de datos
# print(gimnasio_df.head()) -> check, carga el csv

# ver duplicados y eliminarlos
duplicados = gimnasio_df.duplicated() # Devuelve una serie booleana indicando filas duplicadas
num_duplicados = duplicados.sum() # Cuenta cuántos duplicados hay
#print(f"Número de filas duplicadas: {num_duplicados}")
gimnasio_df = gimnasio_df.drop_duplicates() # Elimina filas duplicadas

# 4 chequear si hay valores faltantes
gimnasio_df.fillna(gimnasio_df.mean(numeric_only=True), inplace=True)
""" if gimnasio_df.isnull().sum().sum() == 0:
    print("No hay valores faltantes en el DataFrame después de la imputación.")
else:
    print("Todavía hay valores faltantes en el DataFrame después de la imputación.") """
    
# PANORAMA GENERAL DEL DATAFRAME
""" print("\nInformación general del DataFrame después de la limpieza:")
print(gimnasio_df.describe()) """


## PARTE 2 - Calculos y nuevas columnas

# 1 - Calcular el IMC y agregarlo como nueva columna --- IMC = peso_kg / (altura_m)^2 usando numpy
gimnasio_df['IMC'] = gimnasio_df['peso'] / np.square(gimnasio_df['altura_m']) # Calculo del IMC
gimnasio_df['IMC'] = gimnasio_df['IMC'].round(2)  # Redondear a 2 decimales

# Diagnóstico rápido de IMC
print(f"IMC promedio general: {gimnasio_df['IMC'].mean():.2f}")
print(f"IMC mínimo: {gimnasio_df['IMC'].min():.2f} | máximo: {gimnasio_df['IMC'].max():.2f}")


#print(gimnasio_df[['peso', 'altura_m', 'IMC']].head()) 

# 2 - agregar columna de nivel de asistencia con categorias: Baja si es menor a 5, Media si es entre 5 y 10, Alta si es mayor a 10
#en el dataframe original la columna se llama asistencias_mes usando np.where
gimnasio_df['nivel_asistencia'] = np.where(gimnasio_df['asistencias_mes'] < 5, 'Baja',
                                          np.where(gimnasio_df['asistencias_mes'] <= 10, 'Media', 'Alta'))
#print(gimnasio_df[['asistencias_mes', 'nivel_asistencia']].head())

# Asegurar que las categorías tengan orden lógico
gimnasio_df['nivel_asistencia'] = pd.Categorical(
    gimnasio_df['nivel_asistencia'],
    categories=['Baja', 'Media', 'Alta'],
    ordered=True
)

# 3 - Mostrar los primeros 10 socios ordenados por IMC descendente
socios_imc_desc = gimnasio_df.sort_values(by='IMC', ascending=False).head(10)
print("Top 10 socios con mayor IMC:")
print(socios_imc_desc[['socio_id', 'IMC']])

# Vista previa de la distribución de niveles de asistencia
gimnasio_df['nivel_asistencia'].value_counts().plot(kind='bar', color='orange')
plt.title("Distribución de niveles de asistencia")
plt.xlabel("Nivel de asistencia")
plt.ylabel("Cantidad de socios")
plt.show()
