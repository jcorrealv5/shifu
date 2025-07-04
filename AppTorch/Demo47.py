import torch, sys
import numpy as np
from torchvision.io import decode_image
import matplotlib.pyplot as plt
sys.path.append("../Modulos/")
from torch.nn import Conv2d
from ANN import Grafico

print("Demo 44: Convolucion de una Imagen con Kernel x Defecto")
archivo = r"C:\Users\jhonf\Documents\Shifu\shifu\Lena.png"
imagenTensor = decode_image(archivo, mode="gray")
imagenTensor = imagenTensor.to(torch.float32)
print("Shape Imagen Tensor Entrada: ", imagenTensor.shape)

bias = torch.tensor([0], dtype=torch.float32)
imagenEntrada = imagenTensor.detach().numpy().squeeze(0)

conv = Conv2d(in_channels=1, out_channels=1, kernel_size=3, bias=False)
imagenSalidaTensor = conv(imagenTensor)
imagenSalidaArray = imagenSalidaTensor.detach().numpy().squeeze(0)
print(imagenSalidaTensor.shape)
print(imagenSalidaArray.shape)
Grafico.MostrarImagenes(imagenEntrada, imagenSalidaArray, "Kernel x Defecto")