import os, zlib

#Demo 24: Compresion de datos con Zlib
print("Demo 25: Descompresion de datos con Zlib")
archivoOrigen = input("Ingresa el archivo a descomprimir: ")
if(os.path.isfile(archivoOrigen)):
    if(archivoOrigen[-4:]==".cmp"):
        with open(archivoOrigen,"rb") as fileOrigen:
            dataOrigen = zlib.decompress(fileOrigen.read())
        rutaOrigen = os.path.dirname(archivoOrigen)
        nombreDestino = os.path.basename(archivoOrigen).replace(".cmp","")
        archivoDestino = os.path.join(rutaOrigen, nombreDestino)
        with open(archivoDestino,"wb") as fileDestino:
            fileDestino.write(dataOrigen)
        print("Se descomprimio el archivo en: ", nombreDestino + ".cmp")
    else:
        print("El Archivo No tiene la extension cmp")
else:
    print("Archivo No existe")