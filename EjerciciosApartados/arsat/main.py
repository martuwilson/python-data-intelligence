import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Conversion de tabla en pdf a dataframe de pandas
import tabula

# Especificar encoding para evitar errores
df = tabula.read_pdf("2025-10_grilla_salarial_arsat.pdf", pages="all", encoding='latin-1')[0]

## guardar el dataframe en un archivo CSV
df.to_csv("grilla_salarial_arsat.csv", index=False)
print("DataFrame guardado en grilla_salarial_arsat.csv")