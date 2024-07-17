#MADE BY TOMAS BERNI
import pandas as pd

# Cargar datos
Datos_Ventas_Tienda1 = r'C:\Users\TB\Downloads\Datos_Ventas_Tienda.csv' 
Datos_Ventas_Tienda2 = r'C:\Users\TB\Downloads\Datos_Ventas_Tienda2.csv'
Datos_Ventas_Tienda2 = Datos_Ventas_Tienda2.replace('\u202a', '')  # Había caracteres invisibles que no me dejaban visualizar tienda2 y tuve que cambiarlos.

df1 = pd.read_csv(Datos_Ventas_Tienda1)
df2 = pd.read_csv(Datos_Ventas_Tienda2)
df3 = pd.concat([df1, df2], ignore_index=True)

# Limpieza de datos
df3 = df3.dropna()  # Eliminar filas con valores nulos
df3 = df3.drop_duplicates()  # Eliminar duplicados
df3['Fecha'] = pd.to_datetime(df3['Fecha'])  # Cambiar fecha a datetime
df3['Producto'] = df3['Producto'].replace('Electrónic', 'Electrónica')  # Arreglando errores de ortografía

# Producto más vendido
producto_mas_vendido = df3.groupby("Producto")["Cantidad"].sum()
productos_mas_vendidos = producto_mas_vendido.sort_values(ascending=False)  # Lista de productos más vendidos
print("\nLista de productos mas vendidos:")
print(productos_mas_vendidos)
producto_mas_vendido = productos_mas_vendidos.head(1)  # Producto más vendido individual.
print("\nProducto más vendido:")
print(producto_mas_vendido)

# Mes con más ventas
meses = []

# Extraer los meses de la columna 'Fecha'
for f in df3["Fecha"]:
    meses.append(f.month)

df3["Meses"] = meses

# Agrupar por meses y calcular la suma de las cantidades vendidas
ventas_por_mes = df3.groupby("Meses")["Cantidad"].sum()
mes_mas_ventas = ventas_por_mes.idxmax()
cantidad_mas_ventas = ventas_por_mes.max()

print("\nMes con más ventas:")
print(f"Mes: {mes_mas_ventas}, Cantidad vendida: {cantidad_mas_ventas}")

#Exportar CSV

df3.to_csv("resumen_ventas_csv")

#MADE BY TOMAS BERNI


