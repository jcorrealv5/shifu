import numpy as np

print("Demo 10: Funciones en Python")

def mostrarInfoArray(arreglo, tipo):
    print("Tipo de Array: ", tipo)
    print("Shape Array: ", arreglo.shape)
    print("Dim Array: ", arreglo.ndim)
    print("Elementos Array: ", arreglo.size)
    print("_" * 30)

vector=np.array([10,20,30,40,50])
matriz=np.array([[1,2,3],[4,5,6],[7,8,9]])
tensor=np.array([[[1,1,1],[2,2,1]],[[3,3,1],[4,4,1]]])

mostrarInfoArray(vector, "Vector")
mostrarInfoArray(matriz, "Matriz")
mostrarInfoArray(tensor, "Tensor")