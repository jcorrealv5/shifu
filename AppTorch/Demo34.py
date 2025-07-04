import torch

print("Demo34: Cambiar el Tipo de Datos y la Forma de un Tensor")

print("1. Cambiar el Tipo de Datos de un Tensor")
tensorEnteros = torch.tensor([1,2,3])
print("Type Tensor Enteros: ", tensorEnteros.dtype)
tensorFlotantes = tensorEnteros.to(torch.float32)
print("Type Tensor Flotantes: ", tensorFlotantes.dtype)
print(tensorFlotantes)

print("2. Transposicion de un Tensor")
tensor23 = torch.rand(2, 3)
print("Tensor 2x3:\n", tensor23)
tensor32 = torch.transpose(tensor23, 0, 1)
print("Tensor 3x2:\n", tensor32)

print("3. Cambiar la Forma de un Tensor")
tensor6 = torch.rand(6)
print("Tensor 6:\n", tensor6)
tensor32 = tensor6.reshape(3,2)
print("Tensor 3x2:\n", tensor32)

print("4. Aumentar una dimension a un Tensor")
tensor132 = torch.unsqueeze(tensor32, 0)
print("Tensor 1x3x2:\n", tensor132)

print("5. Eliminar una dimension a un Tensor")
tensor32 = torch.squeeze(tensor132, 0)
print("Tensor 3x2:\n", tensor32)
