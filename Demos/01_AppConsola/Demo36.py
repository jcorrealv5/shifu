from urllib import request

#Demo 36: Cliente HTTP que obtiene el HTML de una Pagina Web
print("Demo 36: Cliente HTTP que obtiene el HTML de una Pagina Web Fija")
url = "https://docs.python.org/3/library/index.html"
rptaHttp = request.urlopen(url)
if(rptaHttp is not None):
    rptaBytes = rptaHttp.read()
    #print(rptaBytes)
    with open("LibreriasPython.html", "wb") as file:
        file.write(rptaBytes)
    print("Se creo el archivo HTML con la Info de las Librerias de Python")