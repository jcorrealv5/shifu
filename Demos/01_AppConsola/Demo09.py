import os

titulo = "Demo 09: Listar Solo Directorios de la Raiz de un Directorio"
print(titulo)
print("")
directorioRaiz = input("Ingresa el Directorio a Listar los Subdirectorios: ")
if(os.path.isdir(directorioRaiz)):
    directorios = os.listdir(directorioRaiz)
    c = 0
    for directorio in directorios:
        directorioCompleto = os.path.join(directorioRaiz, directorio)
        if(os.path.isdir(directorioCompleto)):
            c = c + 1
            print("Directorio", c, ":", directorio)
else:
    print("El directorio ingresado No existe")