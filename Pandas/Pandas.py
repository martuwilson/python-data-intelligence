import pandas as pd

##Ej 1:

data = {
    "nombre": ["Ana", "Luis", "Carlos"],
    "edad": [30, 25, 40],
}

## crear DataFrame df_empleados

df_empleados = pd.DataFrame(data)   
print(df_empleados)

## SOLO columna 'edad' en una variable nueva llamada edades
edades = df_empleados['edad']
print(edades)
type(edades)

nombres = df_empleados['nombre']
print(nombres)
type(nombres)

########
## explorar sus atributos principales: shape, columns, y index.
## Utilizando las siguientes variables respectivamente: shape_df, columns_df, index_df 

shape_df = df_empleados.shape ## shape es una tupla (filas, columnas)
print("Shape del DataFrame")
print(shape_df)

columns_df = df_empleados.columns
print("\nColumnas del DataFrame")
print(columns_df)

index_df = df_empleados.index
print("\nIndices del DataFrame")
print(index_df)

# =============================================================================