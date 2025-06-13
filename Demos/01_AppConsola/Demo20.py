import os
#Demo20: Buscar un Archivo por Nombre en un Directorio y sus Subdirectorios y Mostrar su Contenido
titulo = "Demo20: Buscar un Archivo por Nombre en un Directorio y sus Subdirectorios y Mostrar su Contenido"
print(titulo)
directorio = input("Ingresa el Directorio donde se encuentra el Archivo: ")
if(os.path.isdir(directorio)):
    nombreArchivo = input("Nombre del Archivo a Buscar: ")
    lista = os.walk(directorio)
    c = 0
    for directorio, subdirectorios, archivos in lista:        
        if(nombreArchivo in archivos):
            c=c+1
            print("Encontrado en:", directorio)
            archivo = os.path.join(directorio, nombreArchivo)
            with open(archivo) as file:
                data = file.read()
            print(data)
    print("Numero de Arcnhivos encontrados:", c)
else:
    print("El directorio No existe")