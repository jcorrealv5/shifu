import numpy as np
import random
print("Demo 16: Red Neuronal Basica MCP Dinamica")

def RedMCP(arreglo):
    print("Size Arreglo:",arreglo.size)
    print("Arreglo: ", arreglo)
    pesos = np.random.randint(-10,10,arreglo.size)
    print("Pesos: ", pesos)
    prod = arreglo * pesos
    suma = np.sum(prod)
    print("Suma: ", suma)    
    return(suma>0)

nPruebas = int(input("Ingresa el Numero de Pruebas: "))
cSi = 0
for i in range(nPruebas):
    n = random.randint(3,10)
    arreglo = np.random.random_sample((1, n))
    rpta = RedMCP(arreglo)
    if(rpta):
        cSi=cSi+1
    print(f"Neurona Activada Prueba {i}: {rpta}")
    print("_" * 100)
print(f"Numero de Neuronas Activadas: {cSi}")
print(f"Numero de Neuronas No Activadas: {nPruebas - cSi}")
