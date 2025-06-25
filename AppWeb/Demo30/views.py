from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
import base64, cv2, os
from io import BytesIO
import numpy as np
from PIL import Image
from joblib import load

def PrediccionFirmas(request):
    return render(request, "Demo30/PrediccionFirmas.html")

@xframe_options_exempt
def PredecirFirma(request):
    rpta = ""
    try:
        firmaBase64 = request.POST.get("Firma")
        imagen = convertirBase64ToNumPy(firmaBase64)
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        imagen = cv2.resize(imagen,(80,40)).flatten()
        archivo = r"C:\Users\jhonf\Documents\Shifu\shifu\Curso_Junio\Firmas.pkl"
        modelo = load(archivo)
        y_pred = modelo.predict([imagen])
        indice = y_pred[0]
        print("Prediccion: ", indice)
        rutaFirmas = "C:/Users/jhonf/Documents/Shifu/DataSets/Firmas"
        clases = os.listdir(rutaFirmas)
        rpta = clases[indice]
        print("Pertenece a: ", rpta)
    except Exception as errorgeneral:
        rpta = "Error: " + str(errorgeneral)
    return HttpResponse(rpta)

def convertirBase64ToNumPy(imagenBase64):
    base64_bytes = imagenBase64.encode('ascii')
    buffer = base64.b64decode(base64_bytes)
    imagenPIL = Image.open(BytesIO(buffer))
    imagen = np.array(imagenPIL)
    return imagen