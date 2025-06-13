import os, zipfile
#Demo 26: Comprimir los archivos de un directorio en un archivo
print("Demo 26: Comprimir los archivos de un directorio en un archivo")
directorio = input("Ingresa el directorio donde estan los archivos a comprimir: ")
if(os.path.isdir(directorio)):
    archivos = os.listdir(directorio)
    nArchivos = len(archivos)
    c = 0
    if(nArchivos>0):
        archivoZip = directorio + ".zip"
        zip = zipfile.ZipFile(archivoZip, "w", zipfile.ZIP_DEFLATED)
        for archivo in archivos: 
            archivoCompleto = os.path.join(directorio, archivo)
            if(os.path.isfile(archivoCompleto)):
                c=c+1
                print(c,":",archivo)
                zip.write(archivoCompleto)
        zip.close()
        print(f"Total de archivos comprimidos={c} en {archivoZip}")
    else:
        print("El directorio esta Vacio")
else:
    print("La ruta ingresada No es un Directorio")