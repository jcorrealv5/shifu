from django.shortcuts import render
from django.http import HttpResponse
from Modulos.modAccesoDatos import clienteSQL
import os

def Consulta(request):    
    return render(request, "appDemo07/Consulta.html", {"Ver": "1.0001"})
    
def ConsultarAlumno(request):
    rpta = ""
    idAlumno = request.GET.get("id");
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo03.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    data = con.EjecutarComandoCadena("uspAlumnoObtenerPorIdCsv","IdAlumno", idAlumno) 
    print("data", data)
    if(data is not None and data!=""):
        texto = data
        rutaImagen = "C:/Users/jhonf/Documents/Shifu/Alumnos"
        nombre = idAlumno + ".jpg"
        archivo = os.path.join(rutaImagen, nombre)
        bytesImagen = None
        if(os.path.isfile(archivo)):
            with open(archivo, "rb") as file:
                bytesImagen = file.read()
        bytesRpta = []
        byte1 = int(len(texto))
        bytesTexto = texto.encode(encoding="utf-8")
        bytesRpta.append(byte1)
        bytesRpta.extend(bytesTexto)
        if(bytesImagen is not None):
            bytesRpta.extend(bytesImagen)
        rpta = bytes(bytesRpta)
    return HttpResponse(rpta, content_type="application/octet-stream")