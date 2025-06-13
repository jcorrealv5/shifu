import os
#Demo15: Renombrar un Archivo
titulo = "Demo15: Renombrar un Archivo"
print(titulo)
print("_" * len(titulo))
archivoOrigen = input("Ingresa la Ruta completa del Archivo a Renombrar: ")
if(os.path.isfile(archivoOrigen)):
    nuevoNombre = input("Ingresa el Nuevo Nombre del Archivo: ")
    archivoDestino = os.path.join(os.path.dirname(archivoOrigen), nuevoNombre)
    try:
        os.rename(archivoOrigen, archivoDestino)
    except ValueError as errorValor:
        print("Error de Valor:", errorValor)
    except PermissionError as errorPermiso:
        print("Error de Permiso:", errorPermiso)
    except Exception as errorGeneral:
        print("Error General:", errorGeneral)
    print("Se renombro correctamente el archivo")
else:
    print("El archivo No existe")