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


