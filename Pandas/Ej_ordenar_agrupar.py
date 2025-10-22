import pandas as pd 

datos = {
    'titulo': ['Pelicula A', 'Pelicula B', 'Pelicula C', 'Pelicula D', 'Pelicula E', 'Pelicula F' , 'Pelicula G'],
    'año': [2001, 2000, 2005, 2010, 2003, 2008, 2001],
    'rating': [7.2, 6.5, 8.1, 7.5, 6.8, 8.3, 7.0]
}

df = pd.DataFrame(datos)

##Ordenar año ascendente
df_ordenado = df.sort_values(by='año')
print("DataFrame ordenado por todas las columnas:")
print(df_ordenado)

## Rating descendente y año ascendente
df_ordenado_multiple = df.sort_values(by=['rating', 'año'], ascending=[False, True])
print("\nDataFrame ordenado por rating (desc) y año (asc):")
print(df_ordenado_multiple)

## agregar columna de genero y calcular promedio de 'rating' por genero
df['genero'] = ['Accion', 'Comedia', 'Accion', 'Drama', 'Comedia', 'Drama', 'Accion']

promedio_rating_genero = df.groupby('genero')['rating'].mean().reset_index()
print("\nPromedio de rating por género:")
print(promedio_rating_genero)

## Rating redondeado a 2 decimales
promedio_rating_genero['rating'] = promedio_rating_genero['rating'].round(2)
print("\nPromedio de rating por género (redondeado a 2 decimales):")
print(promedio_rating_genero)