from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
import base64, cv2
from io import BytesIO
import numpy as np
from PIL import Image
from joblib import load

def ClasDigitos(request):
    return render(request, "Demo27/ClasDigitos.html")

@xframe_options_exempt
def ClasificarDigito(request):
    digitoBase64 = request.POST.get("Digito")
    imagen = convertirBase64ToNumPy(digitoBase64)
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    imagen = cv2.resize(imagen,(28,28)).flatten()
    archivo = r"C:\Data\Python\2025_06_DADLCV\Demos\AppConsola\MNIST784.pkl"
    modelo = load(archivo)
    y_pred = modelo.predict([imagen])
    print("Prediccion: ", y_pred[0])
    return HttpResponse(str(y_pred[0]))

def convertirBase64ToNumPy(imagenBase64):
    base64_bytes = imagenBase64.encode('ascii')
    buffer = base64.b64decode(base64_bytes)
    imagenPIL = Image.open(BytesIO(buffer))
    imagen = np.array(imagenPIL)
    return imagen