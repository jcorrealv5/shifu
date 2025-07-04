import torch, sys
import numpy as np
from torchvision.io import decode_image
import matplotlib.pyplot as plt
sys.path.append("../../Modulos/")
from ANN import Convolucion, Grafico

print("Demo 41: Convolucion de una Imagen con Kernels de Desenfoque")
archivo = r"C:\Data\Python\2025_06_DADLCV\Imagenes\Varios\Lena.png"
imagenTensor = decode_image(archivo, mode="gray")
imagenTensor = imagenTensor.to(torch.float32)
imagenTensor = imagenTensor.squeeze(0)
print("Shape Imagen Tensor Entrada: ", imagenTensor.shape)

bias = torch.tensor([0], dtype=torch.float32)
imagenEntrada = imagenTensor.detach().numpy()

kernelBoxBlur = torch.tensor([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]],dtype=torch.float32)
print("Kernel Box Blur:\n", kernelBoxBlur)
conv = Convolucion()
imagenBoxBlur = conv.Filtrar(imagenTensor, kernelBoxBlur, bias)
Grafico.MostrarImagenes(imagenEntrada, imagenBoxBlur, "Box Blur")

kernelGaussianBlur = torch.tensor([[1/16,2/16,1/16],[2/16,4/16,2/16],[1/16,2/16,1/16]],dtype=torch.float32)
print("Kernel Gaussian Blur:\n", kernelGaussianBlur)
conv = Convolucion()
imagenGaussianBlur = conv.Filtrar(imagenTensor, kernelGaussianBlur, bias)
Grafico.MostrarImagenes(imagenEntrada, imagenGaussianBlur, "Gaussian Blur")