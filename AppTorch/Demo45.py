import torch, sys
import numpy as np
from torchvision.io import decode_image
import matplotlib.pyplot as plt
sys.path.append("../../Modulos/")
from ANN import Convolucion, Grafico

print("Demo 45: Convolucion de una Imagen con Kernels Scharr")
archivo = r"C:\Data\Python\2025_06_DADLCV\Imagenes\Varios\Lena.png"
imagenTensor = decode_image(archivo, mode="gray")
imagenTensor = imagenTensor.to(torch.float32)
imagenTensor = imagenTensor.squeeze(0)
print("Shape Imagen Tensor Entrada: ", imagenTensor.shape)

bias = torch.tensor([0], dtype=torch.float32)
imagenEntrada = imagenTensor.detach().numpy()

kernelScharrHorizontal = torch.tensor([[3,0,-3],[10,0,-10],[3,0,-3]],dtype=torch.float32)
print("Kernel Scharr Horizontal:\n", kernelScharrHorizontal)
conv = Convolucion()
imagenScharrHorizontal = conv.Filtrar(imagenTensor, kernelScharrHorizontal, bias)
Grafico.MostrarImagenes(imagenEntrada, imagenScharrHorizontal, "Scharr Horizontal")

kernelScharrVertical = torch.tensor([[3,10,3],[0,0,0],[-3,-10,-3]],dtype=torch.float32)
print("Kernel Scharr Vertical:\n", kernelScharrVertical)
conv = Convolucion()
imagenScharrVertical = conv.Filtrar(imagenTensor, kernelScharrVertical, bias)
Grafico.MostrarImagenes(imagenEntrada, imagenScharrVertical, "Scharr Vertical")