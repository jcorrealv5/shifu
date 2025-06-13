import os
#Demo16: Leer un Archivo de Texto
titulo = "Demo16: Leer un Archivo de Texto"
print(titulo)
print("_" * len(titulo))
archivo = input("Ingresa la ruta del archivo de Texto a Leer: ")
if(os.path.isfile(archivo)):
    with open(archivo, "r", encoding="utf-8") as file:
        data = file.read()
    #file.close()
    print(data)
    print("Cerrado: ", file.closed)
else:
    print("No existe el archivo")