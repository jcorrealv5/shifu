import os

titulo = "Demo 10: Listar Archivos de un cierto Tipo de la Raiz de un Directorio"
print(titulo)
print("")
directorio = input("Ingresa el Directorio a Listar los Archivos: ")
tipo = (input("Ingresa la Extension de los archivos que deseas ver: ")).lower()
if(os.path.isdir(directorio)):
    archivos = os.listdir(directorio)
    c = 0
    for archivo in archivos:
        archivoConRuta = os.path.join(directorio, archivo)
        extension = archivo.split(".")[-1].lower()
        if(os.path.isfile(archivoConRuta) and extension==tipo):
            c = c + 1
            print("Archivo", c, ":", archivo)
    if(c==0):
        print(f"No existen archivos de extension {tipo} en el directorio")
    else:
        print(f"Total de archivos de extension {tipo}: {c}")
else:
    print("El directorio ingresado No existe")