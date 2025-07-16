import torch, cv2
from torch import nn,load
from torch.utils.data import DataLoader
import torch.nn.functional as F
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import sys
sys.path.append("../../Modulos")
from ANN import ConvNet2C1P2FC

print("Demo 57: Predecir Digitos usando CNN")

print("1. Creando el Modelo CNN")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
modelo = ConvNet2C1P2FC().to(device)

print("2. Cargar el Modelo Pre Entrenado")
with open('MNIST_ConvNet2C1P2FC.pt', 'rb') as f: 
     modelo.load_state_dict(load(f, map_location=device, weights_only=True))
     modelo.eval()

print("3. Creando los DataSets y DataLoaders para Pruebas")
dsTest = datasets.MNIST(root='datasets/', train=False, transform=transforms.ToTensor(), download=True)
dlTest = DataLoader(dataset=dsTest, batch_size=32, shuffle=False)

print("4. Cargar y Mostrar la Imagen a Predecir")
imagenes, etiquetas = next(iter(dlTest))
imagenTensor, etiquetaTensor = imagenes[20], etiquetas[20]
print("Shape Tensor Prueba: ", imagenTensor.shape)
print("Shape Tensor Salida: ", etiquetaTensor.shape)
imagenArray = imagenTensor.detach().numpy().squeeze(0)
etiqueta = etiquetaTensor.detach().numpy()
print("Shape Array Prueba: ", imagenArray.shape)
plt.imshow(imagenArray, cmap="gray")
plt.title(etiqueta)
plt.show()

print("5. Usar el Modelo para Clasificar el Digito")
with torch.no_grad():
    imagenPlana = imagenTensor.view(1, 28, 28).to(device)
    print("Shape Data Prueba Final: ", imagenPlana.shape)
    salida = modelo(imagenPlana)
    print("Salida: ", salida)
    _, predecido = torch.max(salida, 1)
    print("predecido: ", predecido)
    prediccion = predecido.item()    
    print("Prediccion: ", prediccion)