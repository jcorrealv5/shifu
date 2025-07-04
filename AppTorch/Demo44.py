import torch, sys
import numpy as np
from torchvision.io import decode_image
import matplotlib.pyplot as plt
sys.path.append("../../Modulos/")
from ANN import Convolucion, Grafico

print("Demo 43: Convolucion de una Imagen con Kernel Laplaciano")
archivo = r"C:\Data\Python\2025_06_DADLCV\Imagenes\Varios\Lena.png"
imagenTensor = decode_image(archivo, mode="gray")
imagenTensor = imagenTensor.to(torch.float32)
imagenTensor = imagenTensor.squeeze(0)
print("Shape Imagen Tensor Entrada: ", imagenTensor.shape)

bias = torch.tensor([0], dtype=torch.float32)
imagenEntrada = imagenTensor.detach().numpy()

kernelLaplaciano = torch.tensor([[0,-1,0],[-1,4,-1],[0,-1,0]],dtype=torch.float32)
print("Kernel Laplaciano:\n", kernelLaplaciano)
conv = Convolucion()
imagenLaplaciano = conv.Filtrar(imagenTensor, kernelLaplaciano, bias)
Grafico.MostrarImagenes(imagenEntrada, imagenLaplaciano, "Laplaciano")