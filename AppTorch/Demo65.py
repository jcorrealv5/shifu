import torch
from torch import nn,load
from torch.utils.data import DataLoader
import torch.nn.functional as F
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import sys
sys.path.append("../../Modulos")
from ANN import ConvNet6C3P3FC

print("Demo 65: Predecir Objetos-CIFAR10 usando CNN")

print("1. Creando el Modelo CNN")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
modelo = ConvNet6C3P3FC().to(device)

print("2. Cargar el Modelo Pre Entrenado")
with open('CIFAR10.pt', 'rb') as f: 
     modelo.load_state_dict(load(f, map_location=device, weights_only=True))
     modelo.eval()

print("3. Creando los DataSets y DataLoaders para Pruebas")
dsTest = datasets.CIFAR10(root='datasets/', train=False, transform=transforms.ToTensor(), download=True)
dlTest = DataLoader(dataset=dsTest, batch_size=32, shuffle=True)
clases = dsTest.classes

print("4. Cargar y Mostrar la Imagen a Predecir")
imagenes, etiquetas = next(iter(dlTest))
imagenTensor, etiquetaTensor = imagenes[0], etiquetas[0]
print("Shape Tensor Prueba: ", imagenTensor.shape)
print("Shape Tensor Salida: ", etiquetaTensor.shape)

imagenArray = imagenTensor.permute(1, 2, 0).numpy()
etiqueta = etiquetaTensor.detach().numpy()
print("Shape Array Prueba: ", imagenArray.shape)
plt.imshow(imagenArray, cmap="gray")
plt.title(clases[etiqueta])
plt.show()

print("5. Usar el Modelo para Clasificar el Digito")
with torch.no_grad():
    imagenPlana = imagenTensor.view(3, 32, 32).to(device)
    print("imagenPlana: ", imagenPlana)
    print("Shape Data Prueba Final: ", imagenPlana.shape)
    salida = modelo(imagenPlana)
    print("Salida: ", salida)
    _, predecido = torch.max(salida, 1)
    print("predecido: ", predecido)
    prediccion = predecido.item()    
    print("Prediccion: ", clases[prediccion])