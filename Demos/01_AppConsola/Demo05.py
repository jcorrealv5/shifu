from urllib import request

#Demo 05: Leer la URL de una Pagina Web y Mostrar la Estadistica x Palabras
url = input("Ingresa la URL a mostrar la Estadistica: ")
rptaHttp = request.urlopen(url)
if(rptaHttp!=None):
    buffer = rptaHttp.read()
    dataTexto = buffer.decode("UTF-8")
    palabras = dataTexto.split(" ")    
    estadistica = {}
    for palabra in palabras:
        if(palabra in estadistica):
            estadistica[palabra] += 1
        else:
            estadistica[palabra] = 1    
    print("Cantidad de Palabras: ", len(palabras))
    claves = estadistica.keys()
    print("Palabras No repetidas: ", len(claves))
    for clave,valor in estadistica.items():
        print(clave, ":", valor)