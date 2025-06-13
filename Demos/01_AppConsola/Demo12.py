import os
titulo = "Listar todos los Subdirectorios y Archivos de un Directorio"
print(titulo)
directorioRaiz = input("Ingresa un directorio a ver todo: ")
if(directorioRaiz==""):
    directorioRaiz="C:/Data/Python/2025_01_PythonMJ/"
if(os.path.exists(directorioRaiz)):
    lista = os.walk(directorioRaiz)
    for directorio, subdirectorios, archivos in lista:
        print("directorio",directorio)
        #print("subdirectorios",subdirectorios)
        if(len(archivos)>0):
            print("\n".join(archivos))
else:
    print("No existe el directorio ingresado")