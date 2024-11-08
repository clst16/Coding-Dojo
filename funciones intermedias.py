#1. Actualizar valores en diccionarios y listas
matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
#1. resultado
matriz[1][0] = 6
print(matriz)

cantantes[0]["nombre"]= "Enrique Martin Morales"
print(cantantes)

ciudades ["México"][2]="Monterrey"
print(ciudades)

coordenadas[0]["latitud"]= 9.9355431
print(coordenadas)

#2. Iterar a través de una lista de diccionarios
cantantes1 = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

#2. resultado
def iterarDiccionario(cantantes1):
    for diccionario in cantantes1:
        for llave, valor in diccionario.items():
            print(f"{llave}-{valor}")
    print()

#3. Obtener valores de una lista de diccionarios
def iterarDiccionario2(llave,lista):
    for diccionario in lista:
        for llave in diccionario:
            print(diccionario[llave])
iterarDiccionario(cantantes1)

#4. Iterar a través de un diccionario con valores de lista
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}
def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{clave.upper()} ({len(lista)})")
        for valor in lista:
            print(f"- {valor}")
        print()
imprimirInformacion(costa_rica)