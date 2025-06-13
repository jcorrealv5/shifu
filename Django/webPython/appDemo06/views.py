from django.shortcuts import render
from django.http import HttpResponse
from Modulos.modAccesoDatos import clienteSQL

def Consulta(request):    
    return render(request, "appDemo06/Consulta.html", {"Ver": "1.0001"})
    
def ConsultarAlumno(request):
    rpta = ""
    idAlumno = request.GET.get("id");
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo03.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    data = con.EjecutarComandoFila("uspAlumnoObtenerPorIdConFoto2","IdAlumno", idAlumno) 
    print("data", data)
    if(data is not None and data!=""):
        texto = data[0]
        bytesImagen = data[1]
        bytesRpta = []
        byte1 = int(len(texto))
        print("Size:", byte1)
        bytesTexto = texto.encode(encoding="utf-8")
        bytesRpta.append(byte1)
        bytesRpta.extend(bytesTexto)
        bytesRpta.extend(bytesImagen)
        rpta = bytes(bytesRpta)
    return HttpResponse(rpta, content_type="application/octet-stream")