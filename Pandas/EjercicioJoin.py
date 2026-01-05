import pandas as pd

# Creación del DataFrame df_a
df_a = pd.DataFrame({
    'id': [1, 2, 3],
    'Nombre': ['Ana', 'Beto', 'Carla']
})
df_a.set_index('id', inplace=True)

# Creación del DataFrame df_b
df_b = pd.DataFrame({
    'id': [1, 2, 3],
    'Edad': [25, 30, 35]
})
df_b.set_index('id', inplace=True)

df_combinado = df_a.join(df_b) ## how por defecto es 'left'
print("DataFrame combinado (join izquierdo por defecto):")
print(df_combinado)


## Ejercicio 2 : 

productos_df = pd.DataFrame({
    'ProductoID': [1, 2, 3, 4],
    'Nombre': ['Producto 1', 'Producto 2', 'Producto 3', 'Producto 4'],
    'Precio': [100, 150, 200, 250]
}).set_index('ProductoID')

categorias_df = pd.DataFrame({
    'CategoriaID': [1, 2],
    'NombreCategoria': ['Categoría 1', 'Categoría 2']
}).set_index('CategoriaID')

## todos los productos se muestren, independientemente de si tienen una categoría asignada o no.
""" Utiliza el método adecuado  para asegurar que todos los registros del DataFrame de la izquierda (productos_df en este caso) se incluyan en el DataFrame resultante df_combinado, independientemente de si tienen una correspondencia en el DataFrame de la derecha (categorias_df). """
productos_categorias = productos_df.join(categorias_df, how='left')
print("\nDataFrame de productos con categorías (join izquierdo):")
print(productos_categorias)


""" combinar estos DataFrames en un DataFrame llamado df_combinado de tal manera que se conserven todos los registros del DataFrame de productos_df, incluso si no tienen una categoría correspondiente en categorias_df. Para esto, debes utilizar el parámetro how="right" en el método join(). """

# NOTA: Para que funcione correctamente, productos_df necesita tener una columna CategoriaID
# que relacione cada producto con su categoría
productos_df = pd.DataFrame({
    'ProductoID': [1, 2, 3, 4],
    'Nombre': ['Producto 1', 'Producto 2', 'Producto 3', 'Producto 4'],
    'Precio': [100, 150, 200, 250],
    'CategoriaID': [1, 2, 3, None]  # Producto 4 no tiene categoría asignada
})

productos_df = productos_df.set_index('ProductoID')

categorias_df = pd.DataFrame({
    'CategoriaID': [1, 2, 3],
    'NombreCategoria': ['Categoría 1', 'Categoría 2', 'Categoría 3']
}).set_index('CategoriaID')

# Right join: conserva TODAS las categorías (DataFrame de la derecha)
# Si un producto no tiene esa categoría, aparecerá NaN en sus columnas
productos_categorias = categorias_df.join(productos_df.set_index('CategoriaID'), how='right')
print("\nDataFrame de productos con categorías (join derecho):")
print(productos_categorias)