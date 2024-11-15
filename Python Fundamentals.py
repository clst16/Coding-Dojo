#1. Carga de Datos
ventas = [
    {
        "fecha": "2024-01-01",
        "producto": "Laptop",
        "cantidad": 1,
        "precio": 1200.00
    },
    {
        "fecha": "2024-01-02",
        "producto": "Mouse",
        "cantidad": 3,
        "precio": 25.50
    },
    {
        "fecha": "2024-01-03",
        "producto": "Teclado",
        "cantidad": 2,
        "precio": 45.00
    },
    {
        "fecha": "2024-01-04",
        "producto": "Monitor",
        "cantidad": 1,
        "precio": 300.00
    },
    {
        "fecha": "2024-01-05",
        "producto": "Impresora",
        "cantidad": 1,
        "precio": 150.00
    }
]

#2. Cálculo de Ingresos Totales
ingresos_totales= 0
for venta in ventas:
    ingresos_totales+= venta["cantidad"]*venta["precio"]
print(ingresos_totales)

#3. Análisis del Producto Más Vendido
ventas_por_producto = {}
for venta in ventas:
    nombre_producto= venta["producto"]
    cantidad= venta["cantidad"]
    if venta in ventas_por_producto:
        ventas_por_producto[venta] += cantidad
    else:
        ventas_por_producto[venta] = cantidad
producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]

print("Producto más vendido:", producto_mas_vendido)

#4. Promedio de Precio por Producto.
precio_por_producto={}
for producto in ventas:
    nombre_producto = producto['producto'] 
    suma_ventas_producto = producto['precio']*producto['cantidad']
    cantidad_producto = producto['cantidad']
precio_por_producto[nombre_producto] = (suma_ventas_producto,cantidad_producto)

#5. Ventas por Día - TERMINAR
ingresos_por_dia={}
for venta in ventas:
    fecha= venta["fecha"]
    cantidad= venta["cantidad"]
    precio= venta["precio"]
    ingresos= venta["cantidad"]*venta["precio"]
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingresos
    else:
        ingresos_por_dia[fecha] = ingresos

print("Ingresos por día:", ingresos_por_dia)

#6 Representación de Datos
resumen_ventas= {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]
if producto in resumen_ventas:
        resumen_ventas[producto]["cantidad"] += cantidad
        resumen_ventas[producto]["ingresos_totales"] += ingresos
else:
    resumen_ventas[producto]={
        "cantidad": cantidad,
        "ingresos_totales": ingresos,
        }
print("Resumen de ventas por producto:", resumen_ventas)