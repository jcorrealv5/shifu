from django.shortcuts import render
from django.http import HttpResponse
from Modulos.modAccesoDatos import clienteSQL
from Modulos.modUtilidades import JSON,XML

def ListarProductos(request):
    rpta = ""
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo28.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    tipo = request.GET.get("out")
    data = con.EjecutarComandoCadena("uspProductoListar3Csv") 
    if(data!=""):
        if(tipo=="" or tipo=="csv"):
            mime="text/plain"
            rpta = data
        if(tipo=="json"):
            rpta = JSON.SerializarCsv(data,'|','¬')
            mime="application/json"
        if(tipo=="xml"):
            rpta = XML.SerializarCsv(data,'|','¬',"Productos","Producto")
            mime="application/xml"
    return HttpResponse(rpta, mime)

def ConsultarProducto(request):
    rpta = ""
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo28.txt"
    id = request.GET.get("id")
    tipo = request.GET.get("out")
    con = clienteSQL(archivoConfig, archivoLog)
    data = con.EjecutarComandoCadena("uspProductoObtenerPorId3","ProductID",id) 
    if(data!=""):
        if(tipo=="" or tipo=="csv"):
            mime="text/plain"
            rpta = data
        if(tipo=="json"):
            rpta = JSON.SerializarCsv(data,'|','¬')
            mime="application/json"
        if(tipo=="xml"):
            rpta = XML.SerializarCsv(data,'|','¬',"Productos","Producto")
            mime="application/xml"
    return HttpResponse(rpta, mime)