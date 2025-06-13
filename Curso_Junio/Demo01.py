import random

nombre = input("Cual es tu nombre: ")
print("Bienvenido: " + nombre)

n = random.randint(1,100)
c = 0
while True:
    cad = input("Ingresa un numero del 1 al 100: ")
    x = int(cad)
    c = c + 1
    if(x==n):
        print("Adivinaste el Numero")
        break
    elif(n>x):
        print("El numero es mayor")
    elif(n<x):
        print("El numero es menor")
print("Adivinaste en " + str(c) + " intentos")