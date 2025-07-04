import torch
import numpy as np
from torchvision.io import decode_image
import matplotlib.pyplot as plt

print("Demo 37: Creacion de un Tensor desde una Imagen y Ploteo")
archivo = r"C:\Data\Python\2025_06_DADLCV\Imagenes\Varios\Lena.png"

print("1. Leer una Imagen como un Tensor")
imagenTensor = decode_image(archivo, mode="gray")
print("Shape del Tensor: ", imagenTensor.shape)
print(imagenTensor)

print("2. Convertir el Tensor de Imagen a Array de NumPy")
imagenArray = imagenTensor.detach().numpy()
imagenGris = imagenArray.squeeze(0)
print("Shape del Array: ", imagenGris.shape)
print(imagenGris)

print("3. Mostrar un Array de Imagen como Grafico")
plt.imshow(imagenGris, cmap="gray")
plt.title("Imagen Original")
plt.show()