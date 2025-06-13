from django.shortcuts import render
from django.http import HttpResponse
from urllib import request as req

def Consulta(request):    
    return render(request, "appDemo32/Consulta.html", {"Ver": "1.0001"})   

def ConsultarProductos(request):
    rpta =""
    id = request.GET.get("id")
    tipo = request.GET.get("tipo")
    if(tipo=="csv"):
        mime="text/plain"
    else:
        mime="application/" + tipo
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo28.txt"
    if(id==""):
        url = "http://190.43.83.241:8000/servicio04/ListarProductos?out=" + tipo
    else:
        url = "http://190.43.83.241:8000/servicio04/ConsultarProducto?id=" + id + "&out=" + tipo
    try:
        rptaHttp = req.urlopen(url)
        if(rptaHttp is not None and rptaHttp.status==200):
            rpta = rptaHttp.read()
    except Exception as errorGeneral:
        print("Error: ", errorGeneral)
        rpta = "Error: " + str(errorGeneral)
    return HttpResponse(rpta, mime)