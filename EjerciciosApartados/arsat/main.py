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
                .str.replace("$", "", regex=False)  # Eliminar símbolo de peso
                .str.replace(" ", "", regex=False)  # Eliminar espacios
                .str.replace(".", "", regex=False)  # Eliminar separador de miles (punto)
                .str.replace(",", ".", regex=False) # Cambiar separador decimal (coma por punto)
                .astype(float)
            )

    dataframes[key] = df
    
# Variables de cada dataframe
administracion_df = dataframes["administracion"]
infra_servicios_df = dataframes["infra_servicios"]
informatica_df = dataframes["informatica"]
obras_df = dataframes["obras"]
operaciones_df = dataframes["operaciones"]


#for key, df in dataframes.items():
    #print(f"\n--- {key.upper()} ---")
    #print(df.dtypes)
    #print(df.head(2))
    

#Calcular aumentos absolutos y porcentuales entre octubre y noviembre de 2025
for key, df in dataframes.items():
    if 'oct_25' in df.columns and 'nov_25' in df.columns:
        df['aumento_absoluto'] = df['nov_25'] - df['oct_25']
        df['aumento_porcentual'] = np.where(
            df['oct_25'] != 0,
            (df['aumento_absoluto'] / df['oct_25']) * 100,
            np.nan
        )
        dataframes[key] = df
        #print(f"\n--- {key.upper()} AUMENTOS ---")
        #print(df[['cargo', 'oct_25', 'nov_25', 'aumento_absoluto', 'aumento_porcentual']].head(2))
        

#redondear los aumentos porcentuales a 2 decimales y tambien las columnas de oct_25 y nov_25 
for key, df in dataframes.items():
    if 'aumento_porcentual' in df.columns:
        df['aumento_porcentual'] = df['aumento_porcentual'].round(2)
    if 'oct_25' in df.columns:
        df['oct_25'] = df['oct_25'].round(2)
    if 'nov_25' in df.columns:
        df['nov_25'] = df['nov_25'].round(2)
    dataframes[key] = df
    
    #print(f"\n--- {key.upper()} REDONDEADO ---")
    #print(df[['cargo', 'oct_25', 'nov_25', 'aumento_absoluto', 'aumento_porcentual']].head(2))
    
#Resumen general por sector
    resumen = df[['aumento_absoluto', 'aumento_porcentual']].agg(['mean', 'min', 'max'])
    #print(f"\n--- {key.upper()} RESUMEN GENERAL ---")
    #print(resumen)

#Ranking de cargos con mayor aumento absoluto
    ranking = df[['cargo', 'aumento_absoluto']].sort_values('aumento_absoluto', ascending=False)
    #print(f"\n--- {key.upper()} RANKING ---")
    #print(ranking.head(5))
    
#Brecha salarial de cada sector: Te muestra qué tan desigual es cada área internamente:
    if 'nov_25' in df.columns:
        brecha = df['nov_25'].max() - df['nov_25'].min()
        print(f"\n--- {key.upper()} BRECHA SALARIAL ---")
        print(f"La brecha salarial en {key} es: ${brecha:,.2f}")