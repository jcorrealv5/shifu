from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from Modulos.modAccesoDatos import clienteSQL
import os

def Consulta(request):    
    return render(request, "appDemo08/Consulta.html", {"Ver": "1.0001"})
    
def ListarArchivos(request):
    rpta = ""
    rutaImagenes = "C:/Users/jhonf/Documents/Shifu/Django/webPython/static/AlumnosSmall"
    archivos = os.listdir(rutaImagenes)
    for i,archivo in enumerate(archivos):
        archivoImg = os.path.join(rutaImagenes, archivo)
        size = os.path.getsize(archivoImg)
        rpta += archivo
        rpta += "|"
        rpta += str(size)
        if(i<len(archivos)-1):
            rpta += ";"
    return HttpResponse(rpta)

@xframe_options_exempt
def ObtenerImagenes(request):
    rpta = ""
    rutaImagenes = "C:/Users/jhonf/Documents/Shifu/Django/webPython/static/AlumnosSmall"
    strArchivos = request.POST.get("Archivos")
    listaArchivos = strArchivos.split("|")
    strSizes = ""
    imagenes = []
    for i,archivo in enumerate(listaArchivos):
        archivoImg = os.path.join(rutaImagenes, archivo)
        if(os.path.isfile(archivoImg)):
            size = os.path.getsize(archivoImg)
            with open(archivoImg, "rb") as file:
                buffer = file.read()
                imagenes.append(buffer)
            strSizes += str(size)
            if(i<len(listaArchivos)-1):
                strSizes += "|"    
    bytesRpta = []
    byte1 = int(len(strSizes))
    bytesTexto = strSizes.encode(encoding="utf-8")
    bytesRpta.append(byte1)
    bytesRpta.extend(bytesTexto)
    for i in range(len(imagenes)):
        bytesRpta.extend(imagenes[i])
    rpta = bytes(bytesRpta)
    return HttpResponse(rpta, content_type="application/octet-stream")