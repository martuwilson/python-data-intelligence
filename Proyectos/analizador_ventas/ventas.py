import pandas as pd

df = pd.read_csv(r"C:\Users\004543613\Desktop\python_data_intelligence\Proyectos\analizador_ventas\Datos_Ventas_Tienda.csv")
df2 = pd.read_csv(r"C:\Users\004543613\Desktop\python_data_intelligence\Proyectos\analizador_ventas\Datos_Ventas_Tienda2.csv")


## crear df combinado
df_combinado = pd.concat([df, df2], ignore_index=True)


##Minupular para limpiar datos
##Fechas a formato fecha
df_combinado['Fecha'] = pd.to_datetime(df_combinado['Fecha'])

## df info -- devolvio que no hay nulos , entonces no hace falta limpiar
##print(df_combinado.info())

## Producto mas vendido
producto_mas_vendido = df_combinado.groupby('Producto')['Cantidad'].sum()
producto_mas_vendido = producto_mas_vendido.sort_values(ascending=False)
producto_mas_vendido.head(1)
##print(f"Producto más vendido:\n{producto_mas_vendido.head(1)}")


## Mes de mas ventas
#1
meses = []
for fecha in df_combinado['Fecha']:
    meses.append(fecha.month)

df_combinado['Meses'] = meses

#2 ver el mes con mas ventas
ventas_por_mes = df_combinado.groupby('Meses')['Total Venta'].sum().sort_values(ascending=False)
#print(f"\nMes con más ventas:\n{ventas_por_mes.head(1)}")

## Datos agrupados por categoria de producto y analizar ventas x categoria

ventas_por_categoria = df_combinado.groupby('Producto')['Total Venta'].sum().sort_values(ascending=False)
#print(f"\nVentas por categoría de producto:\n{ventas_por_categoria}")

## guardar df con meses agregada como csv en el mismo path
df_combinado.to_csv(r"C:\Users\004543613\Desktop\python_data_intelligence\Proyectos\analizador_ventas\Datos_Ventas_Tienda_Combinado.csv", index=False)
print('CSV guardado con éxito.')