import torch, sys
import numpy as np
from torchvision.io import decode_image
import matplotlib.pyplot as plt
sys.path.append("../../Modulos/")
from ANN import Convolucion, Grafico

print("Demo 42: Convolucion de una Imagen con Kernels de Sobel")
archivo = r"C:\Data\Python\2025_06_DADLCV\Imagenes\Varios\Lena.png"
imagenTensor = decode_image(archivo, mode="gray")
imagenTensor = imagenTensor.to(torch.float32)
imagenTensor = imagenTensor.squeeze(0)
print("Shape Imagen Tensor Entrada: ", imagenTensor.shape)

bias = torch.tensor([0], dtype=torch.float32)
imagenEntrada = imagenTensor.detach().numpy()

kernelSobelHorizontal = torch.tensor([[-1,0,1],[-2,0,2],[-1,0,1]],dtype=torch.float32)
print("Kernel Sobel Horizontal:\n", kernelSobelHorizontal)
conv = Convolucion()
imagenSobelHorizontal = conv.Filtrar(imagenTensor, kernelSobelHorizontal, bias)
Grafico.MostrarImagenes(imagenEntrada, imagenSobelHorizontal, "Sobel Horizontal")

kernelSobelVertical = torch.tensor([[-1,-2,-1],[0,0,0],[1,2,1]],dtype=torch.float32)
print("Kernel Sobel Vertical:\n", kernelSobelVertical)
conv = Convolucion()
imagenSobelVertical = conv.Filtrar(imagenTensor, kernelSobelVertical, bias)
Grafico.MostrarImagenes(imagenEntrada, imagenSobelVertical, "Sobel Vertical")