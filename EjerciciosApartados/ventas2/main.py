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

#estandarizar fechas
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce', dayfirst=True)  # Convertir a datetime, forzando errores a NaT
# Verificar que el tipo cambió
print(df['order_date'].dtype)        # Debería decir: datetime64[ns]

# Ver si quedó algún NaT (fecha que no pudo parsearse)
print(df['order_date'].isnull().sum())  # Debería ser 0

# Preview de las fechas convertidas
print(df[['order_id', 'order_date']].head(10))

#Limpiar columna status
# Convertir a minúsculas y eliminar espacios
df['status'] = df['status'].str.lower().str.strip()
# Ver valores únicos después de la limpieza
print("\nValores únicos en 'status' después de limpieza:")
print(df['status'].value_counts())


#Tratar valores nulos y placeholders
#customer_name tiene celdas vacias y valor literal como "N/A". Reemplazar por Unknown
df['customer_name'] = df['customer_name'].replace(['', 'N/A'], 'Unknown')
# Verificar cambios
print("\nValores únicos en 'customer_name' después de limpieza:")
print(df['customer_name'].value_counts())

#quantity tiene NaNs → imputalos con la mediana
df['quantity'] = df['quantity'].fillna(df['quantity'].median())

#customer_email tiene emails inválidos (sin @ completo) → marcalos con un flag booleano email_valido
df['email_valido'] = df['customer_email'].str.contains(r'^[^@]+@[^@]+\.[^@]+$', na=False)

