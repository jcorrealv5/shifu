import torch
import torch.nn.functional as F
from torch import nn
from torchvision.transforms import ToTensor
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from datetime import datetime
import sys
sys.path.append("../../Modulos")
from ANN import CNN, ConvNetBin2C1P2FC

def transformarBinario(y):
    return 1 if y == 0 else 0

inicio = datetime.now()
print("Demo 59: Crear una CNN para Clasificacion Binaria MNIST 28x28")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("1. Crear el DataSet de MNIST y grabar a Disco")
dsTrain = datasets.MNIST(root="datasets",train=True,download=True,transform=ToTensor(),target_transform=transformarBinario)
print("DataSet Train: ", dsTrain)

batchSize = 32
print("2. Crear el DataLoader para manejar el DataSet MNIST")
dlTrain = DataLoader(dsTrain, batch_size=batchSize, shuffle=True)
print("DataLoader Train: ", dlTrain)

imagenes, etiquetas = next(iter(dlTrain))
print("Etiquetas: ", etiquetas)

print("3. Crear el Modelo desde la Red Neuronal")
modelo = ConvNetBin2C1P2FC().to(device)

print("4. Entrenando el Modelo en: " + device.type)
CNN.TrainBin(modelo, dlTrain, device, nEpocas=10, lr=0.001, batchSize=batchSize)

print("5. Midiendo el Rendimiento del Modelo")
presTrain = CNN.CheckAccuracyBin(modelo, dlTrain, device)
print(f"Presicion del Entrenamiento: {presTrain:.2f}")

print("6. Guardando el Modelo")
torch.save(modelo.state_dict(), '0.pt')

fin = datetime.now()
tiempo = fin - inicio
print(f"7. Tiempo de Proceso: {tiempo}")