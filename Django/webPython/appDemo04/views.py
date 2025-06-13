from django.shortcuts import render
from django.http import HttpResponse
from Modulos.modAccesoDatos import clienteSQL

def Consulta(request):
    titulo = "Demo 04: Pagina que usa CSS y JavaScript Generico"
    subtitulo = "Lista de Productos"
    pie = "ACME SA - Lima/Peru - 2025"
    obj = {"titulo": titulo, "subtitulo": subtitulo, "pie":pie}
    return render(request, "appDemo04/Consulta.html", context = obj)
    
def ListarProductos(request):
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo03.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    data = con.EjecutarComandoCadena("uspProductoListarCsv") 
    return HttpResponse(data)