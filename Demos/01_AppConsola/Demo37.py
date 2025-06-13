import os
from urllib import request, error

#Demo 36: Cliente HTTP que obtiene el HTML de una Pagina Web
print("Demo 37: Cliente HTTP que obtiene el HTML de una Pagina Web Dinamica")
url = input("Ingresa la direccion url de la pagina a grabar: ")
try:
    rptaHttp = request.urlopen(url)
    if(rptaHttp is not None and rptaHttp.status==200):
        rptaBytes = rptaHttp.read()
        archivo = os.path.basename(url) + ".html"
        with open(archivo, "wb") as file:
            file.write(rptaBytes)
        print("Se creo el archivo: ", archivo)
    else:
        print("No existe conexion al sitio")
except error.HTTPError as errorHttp:
    print("Error HTTP: ", errorHttp)
except ValueError as errorValor:
    print("Error Valor: ", errorValor)
except Exception as errorGeneral:
    print("Error Generico: ", errorGeneral)