import os, shutil
titulo = "Demo 13: Copiar Solo Archivos de la Raiz (Shallow Copy)"
print(titulo)
directorioOrigen = input("Ingresa el directorio origen: ")
if(os.path.exists(directorioOrigen)):
    directorioDestino = input("Ingresa el directorio destino: ")
    if(os.path.exists(directorioDestino)):
        lista = os.listdir(directorioOrigen)
        c = 0
        for archivo in lista:
            archivoOrigen = os.path.join(directorioOrigen, archivo)
            if(os.path.isfile(archivoOrigen)):
                c=c+1
                archivoDestino = os.path.join(directorioDestino, archivo)
                print("Copiando archivo:", archivo)
                shutil.copy(archivoOrigen, archivoDestino)   
        print("Total de archivos copiados:", c)
    else:
        print("NO existe el directorio destino")
else:
    print("NO existe el directorio origen")