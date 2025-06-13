import os

#Demo 06: Leer Archivo de Texto y Mostrar la Estadistica x Palabras
archivo = input("Ingresa la ruta del archivo a sacar la estadistica: ")
if(os.path.exists(archivo)):
    file = open(archivo, "rb")
    dataBytes = file.read()
    dataTexto = dataBytes.decode("UTF-8")
    palabras = dataTexto.split(" ")    
    estadistica = {}
    for palabra in palabras:
        if(palabra in estadistica):
            estadistica[palabra] += 1
        else:
            estadistica[palabra] = 1    
    print("Cantidad de Palabras: ", len(palabras))
    claves = estadistica.keys()
    print("Palabras No repetidas: ", len(claves))
    for clave,valor in estadistica.items():
        print(clave, ":", valor)
else:
    print("No existe el archivo ingresado")