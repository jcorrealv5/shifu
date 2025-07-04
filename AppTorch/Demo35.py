import torch

print("Demo 35: Operaciones Matematicas con Tensores")
tensor1 = torch.tensor([[2,3],[0,1],[4,1]])
print("Shape tensor1: ", tensor1.shape)
print(tensor1)
tensor2 = torch.tensor([[3,0],[1,2],[5,1]])
print("Shape tensor2: ", tensor2.shape)
print(tensor2)

print("1. Multiplicacion de Tensores (Elementos)")
tensorMultiElem = torch.multiply(tensor1, tensor2)
print("Shape tensor Multi Elem: ", tensorMultiElem.shape)
print(tensorMultiElem)

tensor3 = torch.tensor([[3,0,5],[1,2,1]])
print("Shape tensor3: ", tensor3.shape)

print("2. Multiplicacion de Tensores (Matricial)")
tensorMultiMatriz = torch.matmul(tensor1,tensor3)
print("Shape tensor Multi Matriz: ", tensorMultiMatriz.shape)
print(tensorMultiMatriz)
