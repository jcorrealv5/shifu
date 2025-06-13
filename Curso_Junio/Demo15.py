import numpy as np
import random
print("Demo 15: Red Neuronal Basica MCP")

def RedMCP(arreglo):
    print("Size Arreglo:",arreglo.size)
    print("Arreglo: ", arreglo)
    pesos = np.random.randint(-10,10,arreglo.size)
    print("Pesos: ", pesos)
    prod = arreglo * pesos
    suma = np.sum(prod)
    print("Suma: ", suma)    
    return(suma>0)

for i in range(10):
    n = random.randint(3,10)
    arreglo = np.random.random_sample((1, n))
    rpta = RedMCP(arreglo)
    print(f"Neurona Activada Prueba {i}: {rpta}")
    print("_" * 100)
