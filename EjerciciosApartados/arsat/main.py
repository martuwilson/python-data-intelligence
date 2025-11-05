import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carga de los csv como dataframes
diccionario_rutas = {
    "administracion": r"C:\Users\Martin\Desktop\Python\python-data-intelligence\EjerciciosApartados\arsat\grilla_admin_arsat - Hoja 1.csv",
    "infra_servicios": r"C:\Users\Martin\Desktop\Python\python-data-intelligence\EjerciciosApartados\arsat\infra_servicios_arsat - Hoja 1.csv",
    "informatica": r"C:\Users\Martin\Desktop\Python\python-data-intelligence\EjerciciosApartados\arsat\informatica_arsat - Hoja 1.csv",
    "obras": r"C:\Users\Martin\Desktop\Python\python-data-intelligence\EjerciciosApartados\arsat\obras_arsat - Hoja 1.csv",
    "operaciones": r"C:\Users\Martin\Desktop\Python\python-data-intelligence\EjerciciosApartados\arsat\operaciones_arsat - Hoja 1.csv"
}

dataframes = {}
for key, ruta in diccionario_rutas.items():
    dataframes[key] = pd.read_csv(ruta)

## Correción unnamed: 0
for key, df in dataframes.items():
    if 'Unnamed: 0' in df.columns:
        df = df.rename(columns={'Unnamed: 0': 'cargo'})
    dataframes[key] = df
    
#Limpieza de data
for key, df in dataframes.items():
    df.columns = df.columns.str.strip().str.lower()
    df.columns = df.columns.str.replace(" ", "_")
    df.columns = df.columns.str.replace("-", "_")
    
    for col in ["oct_25", "nov_25"]:
        if col in df.columns:
            df[col] = (
                df[col]
                .replace(r"[\$,]", "", regex=True)
                .str.replace(".", "", regex=False)  
                .str.replace(",", ".", regex=False)
                .astype(float)
            )

    dataframes[key] = df
    
# Variables de cada dataframe
administracion_df = dataframes["administracion"]
infra_servicios_df = dataframes["infra_servicios"]
informatica_df = dataframes["informatica"]
obras_df = dataframes["obras"]
operaciones_df = dataframes["operaciones"]


for key, df in dataframes.items():
    print(f"\n--- {key.upper()} ---")
    print(df.dtypes)
    print(df.head(2))
