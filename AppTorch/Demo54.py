import os
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torchvision.transforms import ToTensor
import torch.nn.functional as F
from datetime import datetime

inicio = datetime.now()
print("Demo 54: Crear una Red Neuronal MLP en PyTorch")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Dispositivo: {device.type}")

class MLP(nn.Module):
    def __init__(self, input_size,num_capas,num_clases):
        super(MLP, self).__init__()
        self.fc1 = nn.Linear(input_size, num_capas)
        self.fc2 = nn.Linear(num_capas, num_clases)
    def forward(self, x):
        x = x.view(-1, 28*28)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

def check_accuracy(loader, model):
    num_correct = 0
    num_samples = 0
    model.eval()
    with torch.no_grad():
        for x, y in loader:
            x = x.to(device).reshape(x.shape[0], -1)
            y = y.to(device)
            scores = model(x)
            _, predictions = scores.max(1)
            num_correct += (predictions == y).sum()
            num_samples += predictions.size(0)
    model.train()
    return num_correct / num_samples

print("1. Crear el DataSet de MNIST y grabar a Disco")
dsTrain = datasets.MNIST(root="datasets",train=True,download=True,transform=ToTensor())
print("DataSet Train: ", dsTrain)

print("2. Crear el DataLoader para manejar el DataSet MNIST")
dlTrain = DataLoader(dsTrain, batch_size=64, shuffle=True)
print("DataLoader Train: ", dlTrain)

print("3. Crear el Modelo desde la Red Neuronal")
modelo = MLP(784,50,10).to(device)

print("4. Entrenando el Modelo en: " + device.type)
criterio = nn.CrossEntropyLoss()
optimizador = torch.optim.Adam(modelo.parameters(), lr=0.001)
nEpocas = 3
for epoch in range(nEpocas):
    for batch_idx, (data, targets) in enumerate(dlTrain):
        X_train = data.to(device).reshape(data.shape[0], -1)
        y_train = targets.to(device)
        scores = modelo(X_train)
        loss = criterio(scores, y_train)        
        optimizador.zero_grad()
        loss.backward()
        optimizador.step()
    print(f"Epoca: {epoch}, Loss: {loss}, Batchs: {batch_idx}")

print("5. Midiendo el Rendimiento del Modelo")
presTrain = check_accuracy(dlTrain, modelo)
print(f"Presicion del Entrenamiento: {presTrain:.2f}")

print("6. Guardando el Modelo")
torch.save(modelo.state_dict(), 'MNIST.pt')

fin = datetime.now()
tiempo = fin - inicio
print(f"7. Tiempo de Proceso: {tiempo}")