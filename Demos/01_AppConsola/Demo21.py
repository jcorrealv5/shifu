import os
#Demo21: Buscar un Archivo por un Texto en un Directorio y sus Subdirectorios y Mostrar su Contenido
titulo = "Demo21: Buscar un Archivo por un Texto en un Directorio y sus Subdirectorios y Mostrar su Contenido"
print(titulo)
directorio = input("Ingresa el Directorio donde se realizara la Busqueda: ")
if(os.path.isdir(directorio)):
    textoBuscado = input("Texto a Buscar: ")
    lista = os.walk(directorio)
    cArchivos = 0
    tipos = ["txt", "xml", "json", "ini", "config", "py", "csv"]
    for directorio, subdirectorios, archivos in lista:
        for itemFile in archivos:
            campos = itemFile.split(".")
            extension = campos[-1]
            if(extension in tipos):                
                archivo = os.path.join(directorio, itemFile)
                with open(archivo, "r", encoding="utf-8") as file:
                    lineas = file.read().split("\n")
                    encontro = False
                    for cLinea,linea in enumerate(lineas):
                        if(linea.find(textoBuscado)>-1):
                            encontro=True
                            print("Directorio: ", directorio)
                            print("Archivo: ", itemFile)
                            print("Nro linea: ", cLinea + 1)
                            print("linea: ", linea)
                    if(encontro):
                        cArchivos=cArchivos+1
    print(f"Numero de Archivos donde se encontro el texto {textoBuscado}: {cArchivos}")
else:
    print("El directorio No existe")