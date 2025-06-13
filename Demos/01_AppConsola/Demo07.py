import random

#Demo 07: Uso del bucle while
titulo = "Demo 07: Uso del bucle while"
print(titulo)
print("_" * len(titulo))
c = 0
azar = random.randint(1,100)
while True:    
    num = int(input("Ingresa un Numero entre 1 y 100: "))
    c = c + 1
    if(azar>num):
        print("El numero al azar es mayor")
    else:
        if(azar<num):
            print("El numero al azar es menor")
        else:
            break
print(f"Acertastes el numero {azar} en {c} Intentos: ")