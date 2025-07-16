from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
import base64, cv2
from io import BytesIO
import numpy as np
from PIL import Image
import torch
from torch import nn,load
import sys
sys.path.append("Modulos")
from ANN import ConvNet2C1P2FC

def ClasDigitos(request):
    return render(request, "Demo58/ClasDigitos.html")

@xframe_options_exempt
def ClasificarDigito(request):
    digitoBase64 = request.POST.get("Digito")
    imagen = convertirBase64ToNumPy(digitoBase64)
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    imagen = cv2.resize(imagen,(28,28))
    imagenTensor = torch.from_numpy(imagen).float()
    print("Tensor: ", imagenTensor)
    archivo = r"C:\Data\Python\2025_06_DADLCV\Demos\AppTorch\MNIST_ConvNet2C1P2FC.pt"
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    modelo = ConvNet2C1P2FC().to(device)
    with open(archivo, 'rb') as f: 
        modelo.load_state_dict(load(f, map_location=device, weights_only=True))
        modelo.eval()
    with torch.no_grad():
        imagenPlana = imagenTensor.view(1, 28, 28).to(device)
        print("imagenPlana: ", imagenPlana.shape)
        print("Shape Data Prueba Final: ", imagenPlana.shape)
        salida = modelo(imagenPlana)
        print("Salida: ", salida)
        _, predecido = torch.max(salida, 1)
        print("predecido: ", predecido)
        prediccion = predecido.item()    
        print("Prediccion: ", prediccion)
    return HttpResponse(prediccion)

def convertirBase64ToNumPy(imagenBase64):
    base64_bytes = imagenBase64.encode('ascii')
    buffer = base64.b64decode(base64_bytes)
    imagenPIL = Image.open(BytesIO(buffer))
    imagen = np.array(imagenPIL)
    return imagen