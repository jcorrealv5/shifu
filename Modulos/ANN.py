import numpy as np
import torch
from torch import nn
import torch.nn.functional as F
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

class CNN:
    def CheckAccuracy(modelo, dataLoader, device):
        num_correct = 0
        num_samples = 0
        modelo.eval()
        with torch.no_grad():
            for x, y in dataLoader:
                x = x.to(device)
                y = y.to(device)
                scores = modelo(x)
                _, predictions = scores.max(1)
                num_correct += (predictions == y).sum()
                num_samples += predictions.size(0)
        modelo.train()
        return num_correct / num_samples
    
    def CheckAccuracyBin(modelo, dataLoader, device):
        num_correct = 0
        num_samples = 0
        modelo.eval()
        with torch.no_grad():
            for x, y in dataLoader:
                x = x.to(device)
                y = y.to(device)
                scores = modelo(x)
                predictions = (torch.sigmoid(scores) > 0.5).squeeze().long()
                num_correct += (predictions == y).sum()
                num_samples += predictions.size(0)
        modelo.train()
        return num_correct / num_samples

    def Train(modelo, dataLoader, device, nEpocas=3, lr=0.001):
        criterio = nn.CrossEntropyLoss()
        optimizador = torch.optim.Adam(modelo.parameters(), lr=0.001)
        for epoch in range(nEpocas):
            for batch_idx, (data, targets) in enumerate(dataLoader):
                X_train = data.to(device)
                y_train = targets.to(device)
                scores = modelo(X_train)
                loss = criterio(scores, y_train)        
                optimizador.zero_grad()
                loss.backward()
                optimizador.step()
            print(f"Epoca: {epoch}, Loss: {loss}, Batchs: {batch_idx}")

    def TrainBin(modelo, dataLoader, device, nEpocas=3, lr=0.001, batchSize=32):
        criterio = nn.BCEWithLogitsLoss()
        optimizador = torch.optim.Adam(modelo.parameters(), lr=0.001)
        for epoch in range(nEpocas):
            for batch_idx, (data, targets) in enumerate(dataLoader):
                X_train = data.to(device)
                y_train = targets.to(device).reshape(32,1).float()
                scores = modelo(X_train)
                loss = criterio(scores, y_train)        
                optimizador.zero_grad()
                loss.backward()
                optimizador.step()
            print(f"Epoca: {epoch}, Loss: {loss}, Batchs: {batch_idx}")

class ConvNet2C1P2FC(nn.Module):
    def __init__(self):
        super(ConvNet2C1P2FC, self).__init__()
        self.Conv1 = nn.Conv2d(1, 32, kernel_size=3)
        self.Conv2 = nn.Conv2d(32, 64, kernel_size=3)
        self.Pool = nn.MaxPool2d(2, 2)
        self.FC1 = nn.Linear(64*12*12, 128)
        self.FC2 = nn.Linear(128, 10)
        self.Dropout1 = nn.Dropout(0.25)
        self.Dropout2 = nn.Dropout(0.5)
    def forward(self,x):
        x = F.relu(self.Conv1(x))
        x = F.relu(self.Conv2(x))
        x = self.Pool(x)
        x = self.Dropout1(x)
        x = torch.flatten(x, 1)
        x = x.view(-1, 64*12*12)
        x = F.relu(self.FC1(x))
        x = self.Dropout2(x)
        x = F.relu(self.FC2(x))
        x = F.log_softmax(x, dim=1)
        return x

class ConvNetBin2C1P2FC(nn.Module):
    def __init__(self):
        super(ConvNetBin2C1P2FC, self).__init__()
        self.Conv1 = nn.Conv2d(1, 32, kernel_size=3)
        self.Conv2 = nn.Conv2d(32, 64, kernel_size=3)
        self.Pool = nn.MaxPool2d(2, 2)
        self.FC1 = nn.Linear(64*12*12, 128)
        self.FC2 = nn.Linear(128, 1)
        self.Dropout1 = nn.Dropout(0.25)
        self.Dropout2 = nn.Dropout(0.5)
    def forward(self,x):
        x = F.relu(self.Conv1(x))
        x = F.relu(self.Conv2(x))
        x = self.Pool(x)
        x = self.Dropout1(x)
        x = torch.flatten(x, 1)
        x = x.view(-1, 64*12*12)
        x = F.relu(self.FC1(x))
        x = self.Dropout2(x)
        x = self.FC2(x)
        return x

class ConvNet6C3P3FC(nn.Module):
    def __init__(self, nClases):
        super(ConvNet6C3P3FC, self).__init__()
        self.Conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.Conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.Conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.Conv4 = nn.Conv2d(128, 128, kernel_size=3, padding=1)
        self.Conv5 = nn.Conv2d(128, 256, kernel_size=3, padding=1)
        self.Conv6 = nn.Conv2d(256, 256, kernel_size=3, padding=1)
        self.Pool = nn.MaxPool2d(2, 2)
        self.FC1 = nn.Linear(256 * 4 * 4, 1024)
        self.FC2 = nn.Linear(1024, 512)
        self.FC3 = nn.Linear(512, nClases)
        self.Dropout1 = nn.Dropout(0.25)
        self.Dropout2 = nn.Dropout(0.5)
    def forward(self,x):
        x = F.relu(self.Conv1(x))
        x = F.relu(self.Conv2(x))
        x = self.Pool(x)
        x = F.relu(self.Conv3(x))
        x = F.relu(self.Conv4(x))
        x = self.Pool(x)
        x = F.relu(self.Conv5(x))
        x = F.relu(self.Conv6(x))
        x = self.Pool(x)
        x = self.Dropout1(x)
        x = torch.flatten(x, 1)
        x = x.view(-1, 256 * 4 * 4)
        x = F.relu(self.FC1(x))
        x = F.relu(self.FC2(x))
        x = self.Dropout2(x)
        x = self.FC3(x)
        return x