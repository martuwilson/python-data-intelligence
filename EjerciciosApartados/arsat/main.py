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
    
    #Brecha salarial de cada sector: Te muestra qué tan desigual es cada área internamente:
    if 'nov_25' in df.columns:
        brecha = df['nov_25'].max() - df['nov_25'].min()
        print(f"\n--- {key.upper()} BRECHA SALARIAL ---")
        print(f"La brecha salarial en {key} es: ${brecha:,.2f}")

# VISUALIZACIONES PARA LINKEDIN (layout 2x2 — eliminadas las gráficas de aumento porcentual promedio y boxplot)
plt.style.use('default')
sectores = list(dataframes.keys())
colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#7209B7']

fig, axes = plt.subplots(2, 2, figsize=(18, 12))
fig.patch.set_facecolor('white')

# --- 1) Brecha Salarial por Sector (axes[0,0])
brechas = []
for key, df in dataframes.items():
    if 'nov_25' in df.columns:
        brecha = df['nov_25'].max() - df['nov_25'].min()
        brechas.append(brecha)

ax = axes[0, 0]
ax.bar(range(len(sectores)), brechas, color=colors)
ax.set_title('Brecha Salarial por Sector\nARSAT - Noviembre 2025', fontsize=12, fontweight='bold')
ax.set_xlabel('Sectores', fontweight='bold')
ax.set_ylabel('Brecha Salarial ($)', fontweight='bold')
ax.set_xticks(range(len(sectores)))
ax.set_xticklabels([s.replace('_', ' ').title() for s in sectores], rotation=30, ha='right')
for i, v in enumerate(brechas):
    ax.text(i, v + max(brechas) * 0.01, f'${v:,.0f}', ha='center', fontweight='bold', fontsize=9)

    # --- 2) Top 10 Cargos Mejor Pagados (axes[0,1])
    todos_los_datos = pd.concat(dataframes.values(), ignore_index=True)
    top_salarios = todos_los_datos.nlargest(10, 'nov_25')[['cargo', 'nov_25']]
    ax = axes[0, 1]
    ax.barh(range(len(top_salarios)), top_salarios['nov_25'], color='#2E86AB')
    ax.set_title('Top 10 Cargos Mejor Pagados\nARSAT - Noviembre 2025', fontsize=12, fontweight='bold')
    ax.set_xlabel('Salario ($)', fontweight='bold')
    ax.set_yticks(range(len(top_salarios)))
    ax.set_yticklabels([c if len(c) <= 40 else c[:37] + '...' for c in top_salarios['cargo']], fontsize=9)
    for i, v in enumerate(top_salarios['nov_25']):
        ax.text(v + max(top_salarios['nov_25']) * 0.005, i, f'${v:,.0f}', va='center', fontweight='bold', fontsize=9)
    ax.invert_yaxis()

    # --- 3) Evolución Salarial Oct vs Nov (axes[1,0])
    muestra_cargos = todos_los_datos.sample(n=min(15, len(todos_los_datos)), random_state=42)[['cargo', 'oct_25', 'nov_25']]
    ax = axes[1, 0]
    x = np.arange(len(muestra_cargos))
    width = 0.35
    ax.bar(x - width/2, muestra_cargos['oct_25'], width, label='Octubre 2025', color='#A23B72', alpha=0.9)
    ax.bar(x + width/2, muestra_cargos['nov_25'], width, label='Noviembre 2025', color='#2E86AB', alpha=0.9)
    ax.set_title('Evolución Salarial Oct vs Nov\nMuestra de cargos', fontsize=12, fontweight='bold')
    ax.set_xlabel('Cargos', fontweight='bold')
    ax.set_ylabel('Salarios ($)', fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels([c if len(c) <= 15 else c[:12] + '...' for c in muestra_cargos['cargo']], rotation=45, ha='right', fontsize=8)
    ax.legend()

    # --- 4) Aumento Absoluto Promedio por Sector (axes[1,1])
    aumentos_absolutos = []
    for key, df in dataframes.items():
        if 'aumento_absoluto' in df.columns:
            aumentos_absolutos.append(df['aumento_absoluto'].mean())

    ax = axes[1, 1]
    ax.bar(range(len(sectores)), aumentos_absolutos, color=colors)
    ax.set_title('Aumento Absoluto Promedio\nPor Sector - 2025', fontsize=12, fontweight='bold')
    ax.set_xlabel('Sectores', fontweight='bold')
    ax.set_ylabel('Aumento Absoluto ($)', fontweight='bold')
    ax.set_xticks(range(len(sectores)))
    ax.set_xticklabels([s.replace('_', ' ').title() for s in sectores], rotation=30, ha='right')
    for i, v in enumerate(aumentos_absolutos):
        ax.text(i, v + max(aumentos_absolutos) * 0.01, f'${v:,.0f}', ha='center', fontweight='bold', fontsize=9)

    plt.tight_layout(pad=2.5)
    plt.savefig('analisis_salarial_arsat_2025.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()
plt.title('Evolución Salarial Oct vs Nov\nMuestra de 15 Cargos', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Cargos', fontweight='bold')
plt.ylabel('Salarios ($)', fontweight='bold')
plt.xticks(x, [cargo[:15] + '...' if len(cargo) > 15 else cargo for cargo in muestra_cargos['cargo']], rotation=45, ha='right', fontsize=8)
plt.legend()
plt.grid(axis='y', alpha=0.3)

# 6. Aumento Absoluto Promedio por Sector
aumentos_absolutos = []
for key, df in dataframes.items():
    if 'aumento_absoluto' in df.columns:
        aumento_abs = df['aumento_absoluto'].mean()
        aumentos_absolutos.append(aumento_abs)

plt.subplot(2, 3, 6)
bars = plt.bar(range(len(sectores)), aumentos_absolutos, color=colors)
plt.title('Aumento Absoluto Promedio\nPor Sector - 2025', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Sectores', fontweight='bold')
plt.ylabel('Aumento Absoluto ($)', fontweight='bold')
plt.xticks(range(len(sectores)), [s.replace('_', ' ').title() for s in sectores], rotation=45, ha='right')
for i, v in enumerate(aumentos_absolutos):
    plt.text(i, v + 200, f'${v:,.0f}', ha='center', fontweight='bold', fontsize=10)
plt.grid(axis='y', alpha=0.3)

plt.tight_layout(pad=3.0)
plt.savefig('analisis_salarial_arsat_2025.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()