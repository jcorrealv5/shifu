import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--directorio', help='Directorio a ver los archivos de un tipo', 
                    default="C:/",type=str)
parser.add_argument('--tipo', help='Tipo de archivoa listar', 
                    default="txt",type=str)
args = parser.parse_args()
directorio = args.directorio
tipo = args.tipo

titulo = "Demo 11: Listar Archivos de un cierto Tipo de la Raiz de un Directorio como Argumentos"
print(titulo)
print("")
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
        print(f"Total de archivos de extension {tipo}: {c} en el directorio: {directorio}")
else:
    print("El directorio ingresado No existe")