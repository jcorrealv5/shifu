from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from Modulos.modAccesoDatos import clienteSQL
import os

def Mantenimiento(request):    
    return render(request, "appDemo13/Mantenimiento.html", {"Ver": "1.0001"})
    
def ObtenerListas(request):
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo11.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    data = con.EjecutarComandoCadena("uspProductoListasCboCsv") 
    return HttpResponse(data)    

def ObtenerProductoPorId(request):
    id = request.GET.get("id")
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo11.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    data = con.EjecutarComandoCadena("uspProductoObtenerPorId2","ProductID",id) 
    return HttpResponse(data)

@xframe_options_exempt
def GrabarProducto(request):
    data = request.POST.get("Data")
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo11.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    data = con.EjecutarComandoCadena("uspProductoGrabar3Csv","Data",data,trx=True)           
    return HttpResponse(data)

def EliminarProductoPorId(request):
    id = request.GET.get("id")
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo11.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    data = con.EjecutarComandoCadena("uspProductoEliminar3Csv","ProductID",id,trx=True) 
    return HttpResponse(data)

@xframe_options_exempt
def GrabarBloque(request):
    rpta = ""
    id = request.POST.get("Id")
    nombre = request.POST.get("Nombre")
    flag = request.POST.get("Flag")
    if(len(request.FILES)>0):
        rutaRepositorio = "C:/Users/jhonf/Documents/Shifu/Django/webPython/static/Repositorio/"
        rutaProducto = rutaRepositorio + "/" + id
        if(not os.path.isdir(rutaProducto)):
            os.mkdir(rutaProducto)
        archivo = os.path.join(rutaProducto, nombre)
        if(flag=="I" and os.path.isfile(archivo)):
            os.remove(archivo)
        fileOrigen = request.FILES["Blob"]
        fileOrigen.open()
        buffer = fileOrigen.read()
        fileOrigen.close()            
        with open(archivo, "ab") as file:
            file.write(buffer)
        rpta = "OK"
    else:
        rpta = "Error - No existe Archivo que grabar"
    return HttpResponse(rpta)
    
def ListarArchivos(request):
    rpta = ""
    id = request.GET.get("id")
    rutaRepositorio = "C:/Users/jhonf/Documents/Shifu/Django/webPython/static/Repositorio/"
    rutaProducto = rutaRepositorio + "/" + id
    if(os.path.isdir(rutaProducto)):
        archivos = os.listdir(rutaProducto)
        rpta = "Nombre del Archivo|Size;600|100;str|int;"
        for nombre in archivos:
            archivo = os.path.join(rutaProducto, nombre)
            rpta += nombre
            rpta += "|"
            rpta += str(os.path.getsize(archivo))
            rpta += ";"
        rpta = rpta[:-1]
    return HttpResponse(rpta)
    
def ObtenerArchivo(request):
    rpta = None
    id = request.GET.get("id")
    nombre = request.GET.get("nombre")
    rutaRepositorio = "C:/Users/jhonf/Documents/Shifu/Django/webPython/static/Repositorio/"
    rutaProducto = rutaRepositorio + "/" + id
    archivo = os.path.join(rutaProducto, nombre)
    if(os.path.isfile(archivo)):
        with open(archivo, "rb") as file:
            rpta = file.read()
    return HttpResponse(rpta, "application/octet-stream")