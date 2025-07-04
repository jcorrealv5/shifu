import torch, sys
import numpy as np
from torchvision.io import decode_image
import matplotlib.pyplot as plt
sys.path.append("../../Modulos/")
from ANN import Convolucion, Grafico

print("Demo 39: Convolucion de una Imagen con Kernel Bordes")
archivo = r"C:\Data\Python\2025_06_DADLCV\Imagenes\Varios\Lena.png"
imagenTensor = decode_image(archivo, mode="gray")
imagenTensor = imagenTensor.to(torch.float32)
imagenTensor = imagenTensor.squeeze(0)
print("Shape Imagen Tensor Entrada: ", imagenTensor.shape)

bias = torch.tensor([0], dtype=torch.float32)
imagenEntrada = imagenTensor.detach().numpy()

kernelBordesHorizontal = torch.tensor([[-1,-1,-1],[0,0,0],[1,1,1]],dtype=torch.float32)
print("Kernel Bordes Horizontal:\n", kernelBordesHorizontal)
conv = Convolucion()
imagenBordesHorizontal = conv.Filtrar(imagenTensor, kernelBordesHorizontal, bias)
Grafico.MostrarImagenes(imagenEntrada, imagenBordesHorizontal, "Bordes Horizontal")

kernelBordesVertical = torch.tensor([[-1,0,1],[-1,0,1],[-1,0,1]],dtype=torch.float32)
print("Kernel Bordes Vertical:\n", kernelBordesVertical)
conv = Convolucion()
imagenBordesVertical = conv.Filtrar(imagenTensor, kernelBordesVertical, bias)
Grafico.MostrarImagenes(imagenEntrada, imagenBordesVertical, "Bordes Vertical")