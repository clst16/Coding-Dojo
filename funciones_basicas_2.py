#1
def multiplicacion_2(numero):
    lista_1 = []
    for i in range(numero+1):
        lista_1.append (numero*2)
    return lista_1
print(multiplicacion_2(1))
#2
def suma_y_resta(a,b):
    print(a+b)
    return a-b
print(suma_y_resta(1,1))
#3
def sumatoria_menos_longitud(lista):
    return sum(lista)-len(lista)
print(sumatoria_menos_longitud([2,1,1]))
#4
def valores_multiplicados_por_segundo(lista):
    if len(lista) >= 2:
        nueva_lista = [x * lista[1] for x in lista]
        print(len(nueva_lista))
        return nueva_lista
    else:
        return []
print (valores_multiplicados_por_segundo([1,2,3,4]))
#5
def valor_y_longitud(valor,longitud):
    lista_1=[]
    for i in range(longitud):
        valor_a_insertar=valor*longitud
        lista_1.append(valor_a_insertar)
    return lista_1
print (valor_y_longitud(2,2))