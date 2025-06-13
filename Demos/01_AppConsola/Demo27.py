import os, zipfile
#Demo 27: Descomprimir archivos de un directorio
print("Demo 27: Descomprimir archivos de un directorio")
archivoComprimido = input("Ingresa el archivo donde estan los archivos a comprimidos: ")
if(os.path.isfile(archivoComprimido)):
    if(archivoComprimido[-4:]==".zip"):
        rutaSalida = os.path.dirname(archivoComprimido)
        zip = zipfile.ZipFile(archivoComprimido, "r", zipfile.ZIP_DEFLATED)
        zip.extractall(rutaSalida)
        archivos = zip.namelist()
        zip.close()
        for i,archivo in enumerate(archivos):
            print(i+1, ":", archivo)
        print("Total de archivos descomprimidos: ", len(archivos))
    else:
        print("El Archivo a descomprimir No es zip")
else:
    print("El dato ingresado No es un archivo")