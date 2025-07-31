import torch
from torch import nn,load
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import sys
from PIL import Image
sys.path.append("../../Modulos")
from ANN import ConvNetBinCol643C2P3FC

data_transforms = transforms.Compose([
        transforms.Resize((64,64)),
        transforms.ToTensor(),
    ])

print("Demo 73: Predecir Sexo desde un Archivo con un Rostro")

print("1. Creando el Modelo CNN")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
modelo = ConvNetBinCol643C2P3FC().to(device)

print("2. Cargar el Modelo Pre Entrenado")
with open('UTK-Face.pt', 'rb') as f: 
     modelo.load_state_dict(load(f, map_location=device, weights_only=True))
     modelo.eval()

rutaImagenes = "C:/Data/Python/2025_06_DADLCV/Imagenes/Caras/"
archivo = rutaImagenes + "2.jpg"
imagen = Image.open(archivo).convert("RGB")
imagenTensor = data_transforms(imagen).unsqueeze(0)
print("Shape Tensor: ", imagenTensor.shape)
plt.imshow(imagen, cmap="gray")
plt.show()

def mostrarSexo(etiqueta):
    if round(etiqueta,2)<0.9:
        sexo="Femenino"
    else:
        sexo="Masculino"
    return sexo
    
with torch.no_grad():
    imagenPlana = imagenTensor.view(3, 64, 64).to(device).float()
    print("imagenPlana: ", imagenPlana)
    print("Shape Data Prueba Final: ", imagenPlana.shape)
    salida = modelo(imagenPlana)
    print("salida: ", salida)
    prediccion = salida.item()
    print("Prediccion: ", prediccion)
    sexo = mostrarSexo(prediccion)
    print("Sexo: ", sexo)