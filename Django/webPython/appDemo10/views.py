from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from Modulos.modAccesoDatos import clienteSQL
import os

def Consulta(request):    
    return render(request, "appDemo10/Consulta.html", {"Ver": "1.0001"})
    
def ListarCodigosSizeImg(request):
    rpta = ""
    rutaImagenes = "C:/Users/jhonf/Documents/Shifu/Alumnos"
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo03.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    data = con.EjecutarComandoCadena("uspAlumnoListarCodigosCsv") 
    if(data is not None and data!=""):
        listaCodigos = data.split("|")
        nCodigos = len(listaCodigos)
        for i in range(nCodigos):
            archivo = listaCodigos[i] + ".jpg"    
            archivoImg = os.path.join(rutaImagenes, archivo)
            if(not os.path.isfile(archivoImg)):
                archivoImg = os.path.join(rutaImagenes, "No.jpg")
            size = os.path.getsize(archivoImg)
            rpta += listaCodigos[i]
            rpta += "|"
            rpta += str(size)
            if(i<nCodigos-1):
                rpta += ";"
    return HttpResponse(rpta)

@xframe_options_exempt
def ObtenerDataConImagenes(request):
    rpta = ""
    rutaImagenes = "C:/Users/jhonf/Documents/Shifu/Alumnos"
    strCodigos = request.POST.get("Codigos")
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo03.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    data = con.EjecutarComandoCadena("uspAlumnosListarPorCodigosCsv","Codigos",strCodigos) 
    if(data is not None and data!=""):
        listaAlumnos = data.split(";")
        strSizes = ""
        imagenes = []
        campos = []
        texto = ""
        for i,alumno in enumerate(listaAlumnos):
            texto += alumno
            campos = alumno.split("|")
            codigo = campos[0]  
            archivo = codigo + ".jpg"     
            archivoImg = os.path.join(rutaImagenes, archivo)
            if(not os.path.isfile(archivoImg)):
                archivoImg = os.path.join(rutaImagenes, "No.jpg")
            size = os.path.getsize(archivoImg)
            with open(archivoImg, "rb") as file:
                buffer = file.read()
                imagenes.append(buffer)
            texto += "|"
            texto += str(size)
            if(i<len(listaAlumnos)-1):
                texto += ";"
        nTexto = len(texto)
        bytesRpta = []
        byte1 = int(nTexto / 255)
        byte2 = int(nTexto % 255)
        bytesTexto = texto.encode(encoding="utf-8")
        bytesRpta.append(byte1)
        bytesRpta.append(byte2)
        bytesRpta.extend(bytesTexto)
        for i in range(len(imagenes)):
            bytesRpta.extend(imagenes[i])
        rpta = bytes(bytesRpta)
    return HttpResponse(rpta, content_type="application/octet-stream")