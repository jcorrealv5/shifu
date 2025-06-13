import os

titulo = "Demo 08: Listar Archivos de la Raiz de un Directorio"
print(titulo)
print("")
directorio = input("Ingresa el Directorio a Listar los Archivos: ")
if(os.path.isdir(directorio)):
    archivos = os.listdir(directorio)
    c = 0
    for archivo in archivos:
        archivoConRuta = os.path.join(directorio, archivo)
        if(os.path.isfile(archivoConRuta)):
            c = c + 1
            print("Archivo", c, ":", archivo)
else:
    print("El directorio ingresado No existe")