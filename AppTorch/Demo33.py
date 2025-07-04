import torch
import numpy as np
from torchvision.io import decode_image

print("Demo 33: Creacion de Tensores")

print("1.1. Desde una Lista de Python")
lista = [1,2,3]
tensorLista = torch.tensor(lista)
print("Shape Tensor Lista Python: ", tensorLista.shape)

print("1.2. Desde un Array de NumPy")
arreglo = np.array([1,2,3], dtype=np.int32)
tensorArreglo = torch.from_numpy(arreglo)
print("Shape Tensor Arreglo NumPy: ", tensorArreglo.shape)

print("1.3. Desde un Archivo de Imagen en Disco")
archivo = r"C:\Data\Python\2025_06_DADLCV\Imagenes\Varios\Lena.png"
tensorImagenColor = decode_image(archivo, mode="RGB")
print("Shape Tensor Archivo Imagen Color: ", tensorImagenColor.shape)
tensorImagenGris = decode_image(archivo, mode="Gray")
print("Shape Tensor Archivo Imagen Gris: ", tensorImagenGris.shape)

print("1.4. Relleno de Ceros")
tensorCeros = torch.zeros(4, 3)
print("Shape Tensor Ceros: ", tensorCeros.shape)
print(tensorCeros)

print("1.5. Relleno de Unos")
tensorUnos = torch.ones(3, 4)
print("Shape Tensor Unos: ", tensorUnos.shape)
print(tensorUnos)

print("1.6. Relleno de Numeros al Azar")
tensorAzar = torch.rand(5, 8)
print("Shape Tensor Azar: ", tensorAzar.shape)
print(tensorAzar)
