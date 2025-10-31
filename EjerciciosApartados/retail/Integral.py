## Ejercicios integral de Pandas y Numpy
import pandas as pd
import numpy as np

# cargar los 5 archivos CSV en DataFrames de Pandas // a futuro podria usar pathlib
paths = [
    r'C:\Users\004543613\Desktop\python_data_intelligence\EjerciciosApartados\retail\exchange_rates.csv',
    r'C:\Users\004543613\Desktop\python_data_intelligence\EjerciciosApartados\retail\retail_customers.csv',
    r'C:\Users\004543613\Desktop\python_data_intelligence\EjerciciosApartados\retail\retail_order_items.csv',
    r'C:\Users\004543613\Desktop\python_data_intelligence\EjerciciosApartados\retail\retail_orders.csv',
    r'C:\Users\004543613\Desktop\python_data_intelligence\EjerciciosApartados\retail\retail_products.csv'
]

dataframes = [pd.read_csv(path) for path in paths]
exchange_rates_df, customers_df, order_items_df, orders_df, products_df = dataframes

## Mostrar los shapes de los dataframes cargados, los types  y porcentaje de nulos por columna
for df, name in zip(dataframes, ['exchange_rates', 'customers', 'order_items', 'orders', 'products']):
    print(f"\nDataFrame: {name}")
    print("Shape:", df.shape)
    print("Types:\n", df.dtypes)
    print("Porcentaje de nulos por columna:")
    print((df.isnull().mean() * 100).round(2)) # porcentaje de nulos es * 100 para que sea % y redondeado a 2 decimales

## convertir en datetime la columna 'order_date' del dataframe orders_df y 'date' del dataframe exchange_rates_df y singup_date de customers_df
orders_df['order_date'] = pd.to_datetime(orders_df['order_date'])
exchange_rates_df['date'] = pd.to_datetime(exchange_rates_df['date'])
customers_df['signup_date']= pd.to_datetime(customers_df['signup_date'])

print("----------------------------------------------\n")
print("Parte 2: Limpieza básica y normalizacion de datos\n")

#Verificar duplicados y eliminarlos dataframe por dataframe
# Usar un diccionario para mantener las referencias correctas
dfs = {
    'exchange_rates_df': exchange_rates_df,
    'customers_df': customers_df,
    'order_items_df': order_items_df,
    'orders_df': orders_df,
    'products_df': products_df
}

for name, df in dfs.items():
    duplicados_antes = df.duplicated().sum()
    print(f"DataFrame: {name}")
    print(f"  - Filas totales: {len(df)}")
    print(f"  - Duplicados encontrados: {duplicados_antes}")
    
    if duplicados_antes > 0:
        # Eliminar duplicados y actualizar la variable original
        df_limpio = df.drop_duplicates()
        print(f"  - Duplicados eliminados: {duplicados_antes}")
        print(f"  - Filas después de limpiar: {len(df_limpio)}")
        
        # Actualizar las variables originales
        if name == 'exchange_rates_df':
            exchange_rates_df = df_limpio
        elif name == 'customers_df':
            customers_df = df_limpio
        elif name == 'order_items_df':
            order_items_df = df_limpio
        elif name == 'orders_df':
            orders_df = df_limpio
        elif name == 'products_df':
            products_df = df_limpio
    else:
        print(f"  - No se encontraron duplicados.")
    print()


""" Estandarizá strings (category, brand, city, channel, coupon_code).
(Aplicá df["col"] = df["col"].str.strip().str.title() o .str.lower() según convenga.) """

products_df['category'] = products_df['category'].str.strip().str.title()
products_df['brand'] = products_df['brand'].str.strip().str.title()
customers_df['city'] = customers_df['city'].str.strip().str.title()
orders_df['channel'] = orders_df['channel'].str.strip().str.lower()
orders_df['coupon_code'] = orders_df['coupon_code'].str.strip().str.upper()

# strip elimina espacios en blanco al inicio y final, title pone mayuscula la primera letra de cada palabra, lower pone todo en minuscula

#6 - Imputación en order_items.unit_price:
# Primero hacemos merge para traer el precio del producto
order_items_df = order_items_df.merge( #merge es similar a join, hace la combinacion de dataframes 
    products_df[['product_id', 'price']], 
    on='product_id', # 
    how='left' # left join para mantener todos los items de order_items_df
)

# Paso 1: Rellenamos los nulos de unit_price con el price del producto
print(f"\nNulos en unit_price ANTES: {order_items_df['unit_price'].isna().sum()}")

order_items_df["unit_price"] = np.where( # where es como un if-else vectorizado
    order_items_df['unit_price'].isna(), # 1- si hay nulo
    order_items_df['price'], # 2- reemplazar con price
    order_items_df['unit_price'] # 3- sino queda igual
)

print(f"Nulos en unit_price después del primer paso: {order_items_df['unit_price'].isna().sum()}")

# Paso 2: Si aún quedan NaN, reemplazar con la mediana por producto - MEDIANA (valor del "medio" con datos ordenados) NO ES MEDIA es promedio 
order_items_df["unit_price"] = order_items_df.groupby("product_id")["unit_price"].transform(
    lambda x: x.fillna(x.median()) ## funcion sin nombre , lambda x(argumento): x.fillna(x.median() es lo que retorna, si hay nulos -> rellena con la mediana de ese grupo
)

print(f"Nulos en unit_price después del segundo paso: {order_items_df['unit_price'].isna().sum()}")

# Eliminamos la columna price auxiliar que ya no necesitamos
order_items_df = order_items_df.drop(columns=['price'])
