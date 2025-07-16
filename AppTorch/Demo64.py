import torch
import torch.nn.functional as F
from torch import nn
from torchvision.transforms import ToTensor
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from datetime import datetime
import sys
sys.path.append("../Modulos")
from ANN import CNN, ConvNet6C3P3FC

inicio = datetime.now()
print("Demo 64: Crear una CNN para Clasificacion Multiclase CIFAR-10 32x32")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("1. Crear el DataSet de CIFAR10")
dsTrain = datasets.CIFAR10(root="datasets",train=True,download=True,transform=ToTensor())
print("DataSet Train: ", dsTrain)

batchSize = 32
print("2. Crear el DataLoader para manejar el DataSet CIFAR-10")
dlTrain = DataLoader(dsTrain, batch_size=batchSize, shuffle=True)
print("DataLoader Train: ", dlTrain)

imagenes, etiquetas = next(iter(dlTrain))
print("Etiquetas: ", etiquetas)
print("Shape Imagen: ", imagenes[0].shape)

print("3. Crear el Modelo desde la Red Neuronal")
modelo = ConvNet6C3P3FC().to(device)

print("4. Entrenando el Modelo en: " + device.type)
CNN.Train(modelo, dlTrain, device, nEpocas=10, lr=0.001)

print("5. Guardando el Modelo")
torch.save(modelo.state_dict(), 'CIFAR10.pt')

fin = datetime.now()
tiempo = fin - inicio
print(f"7. Tiempo de Proceso: {tiempo}")