import pandas as pd

""" data = {
    "mes": ["Ene", "Ene", "Ene", "Feb", "Feb", "Feb", "Mar", "Mar", "Mar"],
    "producto": ["Notebook", "Mouse", "Zapatillas"] * 3,
    "categoria": ["Electrónica", "Electrónica", "Indumentaria"] * 3,
    "unidades_vendidas": [15, 120, 40, 10, 135, 60, 20, 100, 55],
    "precio_unitario": [350000, 4500, 75000, 345000, 4800, 73000, 340000, 5000, 76000],
    "ciudad": ["Buenos Aires", "Córdoba", "Rosario", "Córdoba", "Rosario", "Buenos Aires", "Rosario", "Buenos Aires", "Córdoba"],
    "vendedor": ["Juan", "Ana", "Pedro", "Juan", "Ana", "Pedro", "Juan", "Ana", "Pedro"]
} """
##ventas_dataframe = pd.DataFrame(data)
""" print("DataFrame de Ventas:")
print(ventas_dataframe) """
##ventas_dataframe.to_csv(r"C:\Users\004543613\Desktop\python_data_intelligence\EjerciciosApartados\ventas.csv", index=False) ## Guardar DataFrame como archivo CSV

## 1 - Cargar CSV generado previamente arriba.
path = r"C:\Users\004543613\Desktop\python_data_intelligence\EjerciciosApartados\ventas.csv"
ventas_dataframe = pd.read_csv(path)

## 2 - Mostrar las primeras 5 filas del DataFrame
print("Primeras 5 filas del DataFrame de Ventas:")
print(ventas_dataframe.head())

## 3 - ver columnas y tipo de datos
print("\nColumnas y tipos de datos:")
print(ventas_dataframe.info())

## 4 - obtener estadisticas generales
print("\nEstadísticas generales del DataFrame:")
print(ventas_dataframe.describe()) ## describe() retorna estadisticas descriptivas de columnas numericas