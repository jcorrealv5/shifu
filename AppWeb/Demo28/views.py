from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
import base64, cv2, os
from io import BytesIO
import numpy as np
from PIL import Image

def RegistroFirmas(request):
    return render(request, "Demo28/RegistroFirmas.html")

@xframe_options_exempt
def GrabarFirma(request):
    try:
        usuario = request.POST.get("Usuario")
        firmaBase64 = request.POST.get("Firma")
        imagen = convertirBase64ToNumPy(firmaBase64)
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        rutaFirmas = "C:/Data/Python/2025_06_DADLCV/DataSets/Firmas/"
        rutaUsuario = rutaFirmas + usuario
        if(not os.path.isdir(rutaUsuario)):
            os.mkdir(rutaUsuario)
        listaArchivos = os.listdir(rutaUsuario)
        nArchivos = len(listaArchivos)
        numArchivo = str(nArchivos + 1)
        archivo = os.path.join(rutaUsuario, numArchivo + ".png")
        cv2.imwrite(archivo, imagen)
        rpta = "Se grabo el archivo"
    except Exception as errorgeneral:
        rpta = "Error: " + str(errorgeneral)
    return HttpResponse(rpta)

def convertirBase64ToNumPy(imagenBase64):
    base64_bytes = imagenBase64.encode('ascii')
    buffer = base64.b64decode(base64_bytes)
    imagenPIL = Image.open(BytesIO(buffer))
    imagen = np.array(imagenPIL)
    return imagen