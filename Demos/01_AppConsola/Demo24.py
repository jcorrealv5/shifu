import os, zlib

#Demo 24: Compresion de datos con Zlib
print("Demo 24: Compresion de datos con Zlib")
archivoOrigen = input("Ingresa el archivo a comprimir: ")
if(os.path.isfile(archivoOrigen)):
    with open(archivoOrigen,"rb") as fileOrigen:
        dataOrigen = fileOrigen.read()
    rutaOrigen = os.path.dirname(archivoOrigen)
    nombreOrigen = os.path.basename(archivoOrigen)
    archivoDestino = archivoOrigen + ".cmp"
    with open(archivoDestino,"wb") as fileDestino:
        fileDestino.write(zlib.compress(dataOrigen))
    print("Se comprimio el archivo en: ", nombreOrigen + ".cmp")
else:
    print("Archivo No existe")