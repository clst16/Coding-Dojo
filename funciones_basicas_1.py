#7
def concatenar(a, b):
    return str(b) + str(a)
print(concatenar(7, 15))

#8
def paises_latinoamerica_o_lenguas_indigenas():
    a = 560
    print(a)
    if a < 180:
        return 33
    else:
        return 46
    return 21
print(paises_latinoamerica_o_lenguas_indigenas())

#9
def cantidad_de_dias_o_meses_o_semanas_en_anio(a, b):
    if a < b:
        return 365
    else:
        return 12
    return 52
print(cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3))
print(cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4))
print(cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4) + cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3))

#10
def sumatoria(a, b):
    return a + b
    return 157
print(sumatoria(3, 4))

#11
a = 150
print(a)
def funcion():
    a = 350
    print(a)
print(a)
funcion()
print(a)

#12
a = 150
print(a)
def funcion():
    a = 350
    print(a)
    return a
print(a)
funcion()
print(a)

#13
a = 150
print(a)
def funcion():
    a = 350
    print(a)
    return a
print(a)
a = funcion()
print(a)

#14
def funcion1():
    print(3)
    funcion2()
    print(2)
def funcion2():
    print(1)
funcion1()

#15
def funcion1():
    print(3)
    a = funcion2()
    print(a)
    return 4
def funcion2():
    print(1)
    return 0
b = funcion1()
print(b)