import torch
from torch import nn,load
import matplotlib.pyplot as plt
import sys, cv2
sys.path.append("../../Modulos")
from ANN import ConvNet6C3P3FC

print("Demo 66: Predecir Objetos-CIFAR10 desde un Archivo")

print("1. Creando el Modelo CNN")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
modelo = ConvNet6C3P3FC().to(device)

print("2. Cargar el Modelo Pre Entrenado")
with open('CIFAR10.pt', 'rb') as f: 
     modelo.load_state_dict(load(f, map_location=device, weights_only=True))
     modelo.eval()

rutaImagenes = "C:/Data/Python/2025_06_DADLCV/Imagenes/CIFAR10/"
archivo = rutaImagenes + "Gato.png"
imagen = cv2.imread(archivo)
imagenArray = cv2.resize(imagen, (32,32))
print("Shape Array Numpy: ", imagenArray.shape)
imagenTensor = torch.from_numpy(imagenArray)
print("Shape Tensor: ", imagenTensor.shape)

plt.imshow(imagenArray, cmap="gray")
plt.title("Gato")
plt.show()

clases = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
with torch.no_grad():
    imagenPlana = imagenTensor.view(3, 32, 32).to(device).float()
    print("imagenPlana: ", imagenPlana.shape)
    salida = modelo(imagenPlana)
    print("Salida: ", salida)
    _, predecido = torch.max(salida, 1)
    print("predecido: ", predecido)
    prediccion = predecido.item()    
    print("Prediccion: ", clases[prediccion])