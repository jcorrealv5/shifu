import torch, sys
import numpy as np
from torchvision.io import decode_image
import matplotlib.pyplot as plt
sys.path.append("../../Modulos/")
from ANN import Convolucion, Grafico

print("Demo 43: Convolucion de una Imagen con Kernels Prewitt")
archivo = r"C:\Data\Python\2025_06_DADLCV\Imagenes\Varios\Lena.png"
imagenTensor = decode_image(archivo, mode="gray")
imagenTensor = imagenTensor.to(torch.float32)
imagenTensor = imagenTensor.squeeze(0)
print("Shape Imagen Tensor Entrada: ", imagenTensor.shape)

bias = torch.tensor([0], dtype=torch.float32)
imagenEntrada = imagenTensor.detach().numpy()

kernelPrewittHorizontal = torch.tensor([[-1,0,1],[-1,0,1],[-1,0,1]],dtype=torch.float32)
print("Kernel Prewitt Horizontal:\n", kernelPrewittHorizontal)
conv = Convolucion()
imagenPrewittHorizontal = conv.Filtrar(imagenTensor, kernelPrewittHorizontal, bias)
Grafico.MostrarImagenes(imagenEntrada, imagenPrewittHorizontal, "Prewitt Horizontal")

kernelPrewittVertical = torch.tensor([[-1,-1,-1],[0,0,0],[1,1,1]],dtype=torch.float32)
print("Kernel Prewitt Vertical:\n", kernelPrewittVertical)
conv = Convolucion()
imagenPrewittVertical = conv.Filtrar(imagenTensor, kernelPrewittVertical, bias)
Grafico.MostrarImagenes(imagenEntrada, imagenPrewittVertical, "Prewitt Vertical")