#Demo 02: Evaluar si un numero es Par o Impar
titulo = "Demo 02: Evaluar si un numero es Par o Impar"
print(titulo)
print("_" * len(titulo))
try:
    numero = int(input("Ingresa un Numero Entero: "))
    '''
    if(numero % 2 == 0):
        tipo="Par"
    else:
        tipo="Impar"
    '''
    tipo = ("Par" if numero % 2 == 0 else "Impar")
    print(f"El numero {numero} es {tipo}")
except ValueError as error:
    print("Error: ", error)
