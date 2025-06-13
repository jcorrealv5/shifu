import os, shutil
titulo = "Demo 14: Copiar Todo, Carpetas y Archivos de un Directorio (Deep Copy)"
print(titulo)
directorioOrigenRaiz = input("Ingresa el directorio origen: ")
if(os.path.exists(directorioOrigenRaiz)):
    directorioDestinoRaiz = input("Ingresa el directorio destino: ")
    if(os.path.exists(directorioDestinoRaiz)):
        lista = os.walk(directorioOrigenRaiz)
        cDirs = 0
        cFiles = 0
        for directorio, subdirectorios, archivos in lista:
            print("directorio",directorio)
            if(len(subdirectorios)>0):
                for itemDir in subdirectorios:
                    directorioDestino = os.path.join(directorio.replace(directorioOrigenRaiz,directorioDestinoRaiz), itemDir)
                    print("directorioDestino",directorioDestino)
                    if(not os.path.exists(directorioDestino)):
                        os.mkdir(directorioDestino)
                        cDirs = cDirs + 1
            if(len(archivos)>0):                
                for itemFile in archivos:
                    archivoOrigen = os.path.join(directorio, itemFile)
                    archivoDestino = archivoOrigen.replace(directorioOrigenRaiz,directorioDestinoRaiz)
                    #print("archivoOrigen:", archivoOrigen)
                    #print("archivoDestino:", archivoDestino)
                    print("Copiando archivo:", itemFile)
                    shutil.copy(archivoOrigen, archivoDestino)  
                    cFiles = cFiles + 1
        print("Total de directorios creados:", cDirs)
        print("Total de archivos copiados:", cFiles)
    else:
        print("NO existe el directorio destino")
else:
    print("NO existe el directorio origen")