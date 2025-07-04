import torch, sys
import numpy as np
from torchvision.io import decode_image
import matplotlib.pyplot as plt
sys.path.append("../Modulos/")
from ANN import Convolucion
from datetime import datetime
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


inicio = datetime.now()
print("Demo 46: Crear Varias Convoluciones de una Imagen con Diferentes Kernels")
archivo = r"C:\Users\jhonf\Documents\Shifu\shifu\Lena.png"
imagenTensor = decode_image(archivo, mode="gray")
imagenTensor = imagenTensor.to(torch.float32)
imagenTensor = imagenTensor.squeeze(0)
print("Shape Imagen Tensor Entrada: ", imagenTensor.shape)

bias = torch.tensor([0], dtype=torch.float32)
imagenEntrada = imagenTensor.detach().numpy()
imagenes = []
etiquetas = []

def MostrarImagenes():
    figura, ejes = plt.subplots(3,4)
    for i in range(3):
        for j in range(4):
            n = (i * 4) + j
            ejes[i,j].imshow(imagenes[n], cmap="gray")
            ejes[i,j].set_title(etiquetas[n])
    plt.show()

kernelBordesHorizontal = torch.tensor([[-1,-1,-1],[0,0,0],[1,1,1]],dtype=torch.float32)
print("Kernel Bordes Horizontal:\n", kernelBordesHorizontal)
conv = Convolucion()
imagenBordesHorizontal = conv.Filtrar(imagenTensor, kernelBordesHorizontal, bias)
imagenes.append(imagenBordesHorizontal)
etiquetas.append("Bordes Horizontal")

kernelBordesVertical = torch.tensor([[-1,0,1],[-1,0,1],[-1,0,1]],dtype=torch.float32)
print("Kernel Bordes Vertical:\n", kernelBordesVertical)
conv = Convolucion()
imagenBordesVertical = conv.Filtrar(imagenTensor, kernelBordesVertical, bias)
imagenes.append(imagenBordesVertical)
etiquetas.append("Bordes Vertical")

kernelNitidez = torch.tensor([[0,-1,0],[-1,5,-1],[0,-1,0]],dtype=torch.float32)
print("Kernel Nitidez:\n", kernelNitidez)
conv = Convolucion()
imagenNitidez = conv.Filtrar(imagenTensor, kernelNitidez, bias)
imagenes.append(imagenNitidez)
etiquetas.append("Nitidez")

kernelBoxBlur = torch.tensor([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]],dtype=torch.float32)
print("Kernel Box Blur:\n", kernelBoxBlur)
conv = Convolucion()
imagenBoxBlur = conv.Filtrar(imagenTensor, kernelBoxBlur, bias)
imagenes.append(imagenBoxBlur)
etiquetas.append("Box Blur")

kernelGaussianBlur = torch.tensor([[1/16,2/16,1/16],[2/16,4/16,2/16],[1/16,2/16,1/16]],dtype=torch.float32)
print("Kernel Gaussian Blur:\n", kernelGaussianBlur)
conv = Convolucion()
imagenGaussianBlur = conv.Filtrar(imagenTensor, kernelGaussianBlur, bias)
imagenes.append(imagenGaussianBlur)
etiquetas.append("Gaussian Blur")

kernelSobelHorizontal = torch.tensor([[-1,0,1],[-2,0,2],[-1,0,1]],dtype=torch.float32)
print("Kernel Sobel Horizontal:\n", kernelSobelHorizontal)
conv = Convolucion()
imagenSobelHorizontal = conv.Filtrar(imagenTensor, kernelSobelHorizontal, bias)
imagenes.append(imagenSobelHorizontal)
etiquetas.append("Sobel Horizontal")

kernelSobelVertical = torch.tensor([[-1,-2,-1],[0,0,0],[1,2,1]],dtype=torch.float32)
print("Kernel Sobel Vertical:\n", kernelSobelVertical)
conv = Convolucion()
imagenSobelVertical = conv.Filtrar(imagenTensor, kernelSobelVertical, bias)
imagenes.append(imagenSobelVertical)
etiquetas.append("Sobel Vertical")

kernelPrewittHorizontal = torch.tensor([[-1,0,1],[-1,0,1],[-1,0,1]],dtype=torch.float32)
print("Kernel Prewitt Horizontal:\n", kernelPrewittHorizontal)
conv = Convolucion()
imagenPrewittHorizontal = conv.Filtrar(imagenTensor, kernelPrewittHorizontal, bias)
imagenes.append(imagenPrewittHorizontal)
etiquetas.append("Prewitt Horizontal")

kernelPrewittVertical = torch.tensor([[-1,-1,-1],[0,0,0],[1,1,1]],dtype=torch.float32)
print("Kernel Prewitt Vertical:\n", kernelPrewittVertical)
conv = Convolucion()
imagenPrewittVertical = conv.Filtrar(imagenTensor, kernelPrewittVertical, bias)
imagenes.append(imagenPrewittVertical)
etiquetas.append("Prewitt Vertical")

kernelLaplaciano = torch.tensor([[0,-1,0],[-1,4,-1],[0,-1,0]],dtype=torch.float32)
print("Kernel Laplaciano:\n", kernelLaplaciano)
conv = Convolucion()
imagenLaplaciano = conv.Filtrar(imagenTensor, kernelLaplaciano, bias)
imagenes.append(imagenLaplaciano)
etiquetas.append("Laplaciano")

kernelScharrHorizontal = torch.tensor([[3,0,-3],[10,0,-10],[3,0,-3]],dtype=torch.float32)
print("Kernel Scharr Horizontal:\n", kernelScharrHorizontal)
conv = Convolucion()
imagenScharrHorizontal = conv.Filtrar(imagenTensor, kernelScharrHorizontal, bias)
imagenes.append(imagenScharrHorizontal)
etiquetas.append("Scharr Horizontal")

kernelScharrVertical = torch.tensor([[3,10,3],[0,0,0],[-3,-10,-3]],dtype=torch.float32)
print("Kernel Scharr Vertical:\n", kernelScharrVertical)
conv = Convolucion()
imagenScharrVertical = conv.Filtrar(imagenTensor, kernelScharrVertical, bias)
imagenes.append(imagenScharrVertical)
etiquetas.append("Scharr Vertical")

fin = datetime.now()
tiempo = fin - inicio
print(f"Tiempo de 12 Convoluciones Sin PyTorch: {tiempo}")
MostrarImagenes()