#1
for i in range (1,101):
    print(i)
#2
for i in range (2,501,2):
    print(i)
#3
def contar_vanilla_ice():
    for num in range (1,101):
        if num % 5 == 0:
            print("ice ice")
        if num % 10 == 0:
            print("baby")
contar_vanilla_ice()
#4
suma_total= 0
for i in range (0,500001,2):
    suma_total=suma_total+i
print(suma_total)
#5
for i in range(2024,3,-3):
    print(i)
#6
def imprimir_multiplos(numInicial, numFinal, multiplo):
    for i in range(3,10,2):
        if i % 2 == 0:
            print(i)