from django.shortcuts import render
from django.http import HttpResponse
from Modulos.modAccesoDatos import clienteSQL
from Modulos.modUtilidades import XML

def ListarProductos(request):
    rpta = ""
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo28.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    data = con.EjecutarComandoCadena("uspProductoListar3Csv") 
    if(data!=""):
        rpta = XML.SerializarCsv(data,'|','¬',"Productos","Producto")
    return HttpResponse(rpta, "application/xml")

def ConsultarProducto(request):
    rpta = ""
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo28.txt"
    id = request.GET.get("id")
    con = clienteSQL(archivoConfig, archivoLog)
    data = con.EjecutarComandoCadena("uspProductoObtenerPorId3","ProductID",id) 
    if(data!=""):
        rpta = XML.SerializarCsv(data,'|','¬',"Productos","Producto")
    return HttpResponse(rpta, "application/xml")