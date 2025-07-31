import cv2, sys, os, shutil
from PIL import Image
import torch
from torch import nn, load
import torchvision.transforms as transforms

sys.path.append("../Modulos")
from ANN import ConvNetBinCol643C2P3FC

print("Demo 76: Programa que clasifica archivos en 2 carpetas: Hombres y Mujeres")

rutaOrigen = "C:/Users/jhonf/Documents/Shifu/DataSets/RENIEC"
rutaDestino = "C:/Users/jhonf/Documents/Shifu/DataSets/Imagenes"

# Crear carpetas de destino si no existen
os.makedirs(os.path.join(rutaDestino, "Hombres"), exist_ok=True)
os.makedirs(os.path.join(rutaDestino, "Mujeres"), exist_ok=True)

print("1. Crear un Clasificador para Reconocer Rostros usando Haar Cascade")
archivoHaar = "haarcascade_frontalface_default.xml"
clasificador = cv2.CascadeClassifier(archivoHaar)

print("2. Crear el Modelo CNN para Clasificar Sexo")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
modelo = ConvNetBinCol643C2P3FC().to(device)

print("3. Cargar los Pesos del Modelo Pre Entrenado")
with open('UTK-Face.pt', 'rb') as f: 
    modelo.load_state_dict(load(f, map_location=device, weights_only=True))
    modelo.eval()

data_transforms = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.ToTensor()
])

archivos = os.listdir(rutaOrigen)
c = 0

print("4. Clasificando Archivos")
for i, nombreArchivo in enumerate(archivos):
    archivoOrigen = os.path.join(rutaOrigen, nombreArchivo)
    imagen = cv2.imread(archivoOrigen)

    if imagen is None:
        print(f"❌ No se pudo leer la imagen: {archivoOrigen}")
        continue

    caras = clasificador.detectMultiScale(imagen, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50), flags=cv2.CASCADE_SCALE_IMAGE)
    if len(caras) > 0:
        for (x, y, w, h) in caras:
            cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cara = imagen[y:y + h, x:x + w]
            imagenPIL = Image.fromarray(cara).convert("RGB")
            imagenTensor = data_transforms(imagenPIL).unsqueeze(0)

            with torch.no_grad():
                imagenPlana = imagenTensor.view(3, 64, 64).to(device).float()
                salida = modelo(imagenPlana)
                carpeta = "Mujeres" if round(salida.item(), 2) < 0.9 else "Hombres"

                print(f"Item: {i}, Archivo: {nombreArchivo}, Categoria: {carpeta}")
                archivoDestino = os.path.join(rutaDestino, carpeta, nombreArchivo)
                shutil.copyfile(archivoOrigen, archivoDestino)
                c += 1

print(f"✅ Se clasificaron {c} archivos.")
