import torch, sys
import numpy as np
from torchvision.io import decode_image
import matplotlib.pyplot as plt
sys.path.append("../Modulos/")
from torch.nn import Conv2d
from ANN import Grafico

print("Demo 49: Convolucion de una Imagen con Kernel Especifico Box Blur 7x7")
archivo = r"C:\Users\jhonf\Documents\Shifu\shifu\Lena.png"
imagenTensor = decode_image(archivo, mode="gray")
imagenTensor = imagenTensor.to(torch.float32)
print("Shape Imagen Tensor Entrada: ", imagenTensor.shape)

kernel = torch.tensor([
[1/49,1/49,1/49,1/49,1/49,1/49,1/49],
[1/49,1/49,1/49,1/49,1/49,1/49,1/49],
[1/49,1/49,1/49,1/49,1/49,1/49,1/49],
[1/49,1/49,1/49,1/49,1/49,1/49,1/49],
[1/49,1/49,1/49,1/49,1/49,1/49,1/49],
[1/49,1/49,1/49,1/49,1/49,1/49,1/49],
[1/49,1/49,1/49,1/49,1/49,1/49,1/49]
],dtype=torch.float32)
kernel = kernel.reshape(1,1,7,7)
print("Kernel Laplaciano:\n", kernel)

bias = torch.tensor([5], dtype=torch.float32)
imagenEntrada = imagenTensor.detach().numpy().squeeze(0)

conv = Conv2d(in_channels=1, out_channels=1, kernel_size=7, bias=True)
conv.weight = torch.nn.Parameter(kernel)
conv.bias = torch.nn.Parameter(bias)
imagenSalidaTensor = conv(imagenTensor)

imagenSalidaArray = imagenSalidaTensor.detach().numpy().squeeze(0)
print(imagenSalidaTensor.shape)
print(imagenSalidaArray.shape)
Grafico.MostrarImagenes(imagenEntrada, imagenSalidaArray, "Box Blur 7x7")