from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime

def autenticacion(nombreSesionLogin, urlVistaLogin):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            print("autenticacion")
            if(nombreSesionLogin in request.session):                
                login = request.session.get(nombreSesionLogin,"")
                print("login:",login)
                if(login!=""):
                    print("Si Autenticado")
                    return view_func(request, *args, **kwargs)
                else:
                    print("No Autenticado")
            else:
                print("No Autenticado")
                return render(request, urlVistaLogin)
        return wrap
    return decorator

def auditoria(archivoAuditoria, nombreSesionLogin):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):            
            fechaHora = datetime.now()
            strFechaHora = fechaHora.strftime("%Y-%m-%d %H:%M:%S")
            usuario = ""
            if(nombreSesionLogin in request.session):
                usuario = request.session.get(nombreSesionLogin,"")
            ip = ""
            ips = request.META.get('HTTP_X_FORWARDED_FOR')
            if ips:
                ip = ips.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
            file = open(archivoAuditoria, "a")
            file.write("Fecha y Hora: " + strFechaHora + "\n")
            file.write("Usuario: " + usuario + "\n")
            file.write("Ruta: " + request.path + "\n")
            file.write("IP Cliente: " + ip + "\n")
            file.write("Metodo Http: " + request.method + "\n")
            file.write("________________________________________\n")
            return view_func(request, *args, **kwargs)
        return wrap
    return decorator