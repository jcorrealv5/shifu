import numpy as np
import torch
import matplotlib.pyplot as plt

class Activacion():
    def Sigmoide(x):
        return (1/(1+np.exp(-x)))
	
    def TangenteHiperbolica(x):
        return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
    
    def ReLU(x):
        return np.maximum(0, x)
    
    def LeakyRelu(alpha,x):
        return(np.maximum(alpha*x,x))

class Convolucion:
    def ObtenerSize(self,imagen, kernel, padding, stride):
        h,w = imagen.shape[-2],imagen.shape[-1]
        k_h, k_w = kernel.shape[-2],kernel.shape[-1]

        h_out = (h-k_h-2*padding)//stride[0] +1
        w_out = (w-k_w-2*padding)//stride[1] +1
        return h_out,w_out

    def Filtrar(self,imagen, kernel, bias, padding=0, stride=(1,1)):
        print("Filtrando...")
        imagenSalida = self.ObtenerSize(imagen, kernel, padding, stride)
        imagenFiltro = np.zeros(imagenSalida)
        for i in range(imagenSalida[0]):
            for j in range(imagenSalida[1]):
                imagenFiltro[i,j]=torch.tensordot(imagen[i:3+i,j:3+j],kernel).numpy() + bias.numpy()
        return imagenFiltro

class Grafico:
    def MostrarImagenes(imagenOriginal, imagenFiltro, tipoKernel):
        figura, ejes = plt.subplots(1,2)
        ejes[0].imshow(imagenOriginal, cmap="gray")
        ejes[0].set_title("Imagen Original")
        ejes[1].imshow(imagenFiltro, cmap="gray")
        ejes[1].set_title("Imagen Filtrada con Kernel " + tipoKernel)
        plt.show()