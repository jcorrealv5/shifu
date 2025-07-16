import torch
import torch.nn.functional as F
from torch import nn
from torchvision.transforms import ToTensor
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from datetime import datetime
import sys
sys.path.append("../../Modulos")
from ANN import CNN, ConvNet2C1P2FC

inicio = datetime.now()
print("Demo 56: Crear una CNN para Digitos MNIST 28x28")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("1. Crear el DataSet de MNIST y grabar a Disco")
dsTrain = datasets.MNIST(root="datasets",train=True,download=True,transform=ToTensor())
print("DataSet Train: ", dsTrain)

print("2. Crear el DataLoader para manejar el DataSet MNIST")
dlTrain = DataLoader(dsTrain, batch_size=32, shuffle=True)
print("DataLoader Train: ", dlTrain)

print("3. Crear el Modelo desde la Red Neuronal")
modelo = ConvNet2C1P2FC().to(device)

print("4. Entrenando el Modelo en: " + device.type)
CNN.Train(modelo, dlTrain, device, nEpocas=10, lr=0.001)

print("5. Midiendo el Rendimiento del Modelo")
presTrain = CNN.CheckAccuracy(modelo, dlTrain, device)
print(f"Presicion del Entrenamiento: {presTrain:.2f}")

print("6. Guardando el Modelo")
torch.save(modelo.state_dict(), 'MNIST_ConvNet2C1P2FC.pt')

fin = datetime.now()
tiempo = fin - inicio
print(f"7. Tiempo de Proceso: {tiempo}")