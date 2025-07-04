import torch
import numpy as np
from torchvision.io import decode_image
import matplotlib.pyplot as plt

def ObtenerSize(imagen, kernel, padding, stride):
    h,w = imagen.shape[-2],imagen.shape[-1]
    k_h, k_w = kernel.shape[-2],kernel.shape[-1]

    h_out = (h-k_h-2*padding)//stride[0] +1
    w_out = (w-k_w-2*padding)//stride[1] +1
    return h_out,w_out

def Filtrar(imagen, kernel, bias, padding=0, stride=(1,1)):
    print("Filtrando...")
    imagenSalida = ObtenerSize(imagen, kernel, padding, stride)
    imagenFiltro = np.zeros(imagenSalida)
    for i in range(imagenSalida[0]):
        for j in range(imagenSalida[1]):
            imagenFiltro[i,j]=torch.tensordot(imagen[i:3+i,j:3+j],kernel).numpy() + bias.numpy()
    return imagenFiltro

def MostrarImagenes(imagenOriginal, imagenFiltro, tipoKernel):
    figura, ejes = plt.subplots(1,2)
    ejes[0].imshow(imagenOriginal, cmap="gray")
    ejes[0].set_title("Imagen Original")
    ejes[1].imshow(imagenFiltro, cmap="gray")
    ejes[1].set_title("Imagen Filtrada con Kernel " + tipoKernel)
    plt.show()

print("Demo 38: Convolucion de una Imagen")
archivo = r"C:\Data\Python\2025_06_DADLCV\Imagenes\Varios\Lena.png"
imagenTensor = decode_image(archivo, mode="gray")
imagenTensor = imagenTensor.squeeze(0)
print("Tipo Tensor Entrada: ", imagenTensor.dtype)
print("Shape Imagen Tensor Entrada: ", imagenTensor.shape)

kernel = torch.tensor([[0,-1,0],[-1,5,-1],[0,-1,0]],dtype=torch.uint8)
print("Tipo Kernel Entrada: ", kernel.dtype)
print("Shape Kernel Entrada: ", kernel.shape)

bias = torch.tensor([10], dtype=torch.float32)

imagenEntrada = imagenTensor.detach().numpy()
imagenSalida = Filtrar(imagenTensor, kernel, bias)

print("Shape Imagen Array Entrada: ", imagenEntrada.shape)
print("Shape Imagen Array Salida: ", imagenSalida.shape)

MostrarImagenes(imagenEntrada, imagenSalida, "Comun")