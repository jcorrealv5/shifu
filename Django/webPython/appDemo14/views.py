from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from Modulos.modGraficos import Captcha
from Modulos.modAccesoDatos import clienteSQL
from Modulos.modSeguridadWeb import autenticacion, auditoria
import os

@auditoria("C:/Users/jhonf/Documents/Shifu/Django/Carrito.txt", "Usuario")
def Login(request):    
    return render(request, "appDemo14/Login.html", {"Ver": "1.0001"})

def CrearCaptcha(request):
    rpta = Captcha.Crear(5, 220, 80, 40, "aqua", 10)
    buffer = rpta["Imagen"]
    codigo = rpta["Codigo"]
    request.session["Codigo"] = codigo
    return HttpResponse(buffer, "application/octet-stream")

@xframe_options_exempt
def ValidarLogin(request):
    rpta = ""
    codigoGenerado = request.session["Codigo"]
    usuario = request.POST.get("Usuario")
    claveCifrada = request.POST.get("Clave")
    codigoEnviado = request.POST.get("Codigo")
    if(codigoGenerado==codigoEnviado):    
        login = usuario + "|" + claveCifrada
        archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
        archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo14.txt"
        con = clienteSQL(archivoConfig, archivoLog)
        rpta = con.EjecutarComandoCadena("uspUsuarioValidarLoginCsv","Login",login)
        if(rpta==""):
            rpta = "Error - Login invalido"
        else:
            request.session["Usuario"] = usuario
    else:
        rpta = "Error - Codigo de captcha incorrecto"
    return HttpResponse(rpta)

@autenticacion("Usuario", "appDemo14/Login.html")
@auditoria("C:/Users/jhonf/Documents/Shifu/Django/Carrito.txt", "Usuario")
def Categorias(request):    
    return render(request, "appDemo14/Categorias.html", {"Ver": "1.0001"})

def ListarCodigos(request):
    rpta = ""
    carpeta = request.GET.get("Carpeta")
    print("carpeta", carpeta)
    if(carpeta=="Producto"):
        idCategoria = request.GET.get("IdCategoria")
        print("idCategoria", idCategoria)
    rutaImagenes = "C:/Data/Python/2025_01_PythonMJ/Imagenes/" + carpeta
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo14.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    if(carpeta=="Producto"):
        data = con.EjecutarComandoCadena("uspProductoListarCodigosPorCategoriaCsv", "CategoryID", idCategoria) 
    else:
        data = con.EjecutarComandoCadena("usp" + carpeta + "ListarCodigosCsv") 
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
        print("rpta", rpta)
    return HttpResponse(rpta)

@xframe_options_exempt
def ObtenerImagenes(request):
    rpta = ""
    carpeta = request.POST.get("Carpeta")
    strCodigos = request.POST.get("Codigos")
    print("ObtenerImagenes")
    print("carpeta", carpeta)
    print("strCodigos", strCodigos)
    rutaImagenes = "C:/Data/Python/2025_01_PythonMJ/Imagenes/" + carpeta
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo03.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    data = con.EjecutarComandoCadena("usp" + carpeta + "ListarPorCodigosCsv","Codigos",strCodigos) 
    if(data is not None and data!=""):
        lista = data.split(";")
        strSizes = ""
        imagenes = []
        campos = []
        texto = ""
        for i,fila in enumerate(lista):
            texto += fila
            campos = fila.split("|")
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
            if(i<len(lista)-1):
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

@autenticacion("Usuario", "appDemo14/Login.html")  
@auditoria("C:/Data/Python/2025_01_PythonMJ/Demos/Logs/Carrito.txt", "Usuario")
def Productos(request):
    return render(request, "appDemo14/Productos.html", {"Ver": "1.0001"})

@autenticacion("Usuario", "appDemo14/Login.html") 
@auditoria("C:/Data/Python/2025_01_PythonMJ/Demos/Logs/Carrito.txt", "Usuario")
def Detalles(request):    
    return render(request, "appDemo14/Detalles.html", {"Ver": "1.0001"})

@auditoria("C:/Data/Python/2025_01_PythonMJ/Demos/Logs/Carrito.txt", "Usuario")
def ObtenerStockProductoPorId(request):
    id = request.GET.get("id")
    archivoConfig = r"C:\Data\Python\2025_01_PythonMJ\Demos\03_Django\WebPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Data\Python\2025_01_PythonMJ\Demos\Logs\LogDjango_Demo11.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    data = con.EjecutarComandoCadena("uspProductoObtenerStockPorId","ProductID",id) 
    return HttpResponse(data)

@xframe_options_exempt   
@auditoria("C:/Data/Python/2025_01_PythonMJ/Demos/Logs/Carrito.txt", "Usuario")
def GrabarOrden(request):
    rpta = ""
    data = request.POST.get("Data")
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo03.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    rpta = con.EjecutarComandoCadena("uspOrdenGrabarPyCsv","Data",data,trx=True) 
    return HttpResponse(rpta)