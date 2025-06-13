from django.shortcuts import render

def Menu(request):       
    return render(request, "appDemo02/Menu.html")

def Acerca(request):
    return render(request, "appDemo02/Acerca.html")

def Productos(request):
    return render(request, "appDemo02/Productos.html")

def Servicios(request):
    return render(request, "appDemo02/Servicios.html")