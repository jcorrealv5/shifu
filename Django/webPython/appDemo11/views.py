from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from Modulos.modAccesoDatos import clienteSQL

def Mantenimiento(request):    
    return render(request, "appDemo11/Mantenimiento.html", {"Ver": "1.0001"})
    
def ObtenerListas(request):
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo03.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    data = con.EjecutarComandoCadena("uspProductoListasCboCsv") 
    return HttpResponse(data)

def ObtenerProductoPorId(request):
    id = request.GET.get("id")
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo03.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    data = con.EjecutarComandoCadena("uspProductoObtenerPorId2","ProductID",id) 
    return HttpResponse(data)

@xframe_options_exempt
def GrabarProducto(request):
    data = request.POST.get("Data")
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo03.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    data = con.EjecutarComandoCadena("uspProductoGrabar3Csv","Data",data,trx=True) 
    return HttpResponse(data)

def EliminarProductoPorId(request):
    id = request.GET.get("id")
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo03.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    data = con.EjecutarComandoCadena("uspProductoEliminar3Csv","ProductID",id,trx=True) 
    return HttpResponse(data)