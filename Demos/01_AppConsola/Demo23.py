import os
#Demo 23: Lectura de un Archivo DBF usando solo Bytes
def convertBytesToString(lista):
    rpta = ""
    nLista = len(lista)
    for i in range(nLista):
        rpta += chr(lista[i])
    return rpta

print("Demo 23: Lectura de un Archivo DBF usando solo Bytes")
archivo = input("Ingresa la ruta y nombre del archivo DBF a leer: ")
if(os.path.isfile(archivo)):
    with open(archivo, "rb") as file:
        bytesTipo = file.read(1)
        if(len(bytesTipo)>0):
            if(bytesTipo[0]==48):
                bytesFecha = list(file.read(3))
                fecha = str(bytesFecha[0]) + "/" + str(bytesFecha[1]) + "/" + str(bytesFecha[2])
                print("Fecha de Creacion: ", fecha)
                bytesNumReg = list(file.read(4))
                numReg = int.from_bytes(bytesNumReg, byteorder='little', signed=False)
                print("Numero de Registros: ", numReg)
                bytesCab = list(file.read(2))
                numCab = int.from_bytes(bytesCab, byteorder='little', signed=False)
                nCampos = (numCab - 32) // 32
                print("Numero de Campos: ", nCampos)
                bytesNoUsados = file.read(22)
                for i in range(nCampos):
                    bytesNombreCampo = list(file.read(11))
                    bytesTipoCampo = list(file.read(1))
                    bytesNoUsados = file.read(4)
                    bytesSize = list(file.read(2))
                    bytesNoUsados = file.read(14)
                    print("Nombre del Campo: ", convertBytesToString(bytesNombreCampo))
                    print("Tipo del Campo: ", chr(bytesTipoCampo[0]))
                    print("Size del Campo: ", bytesSize[0])
                    print("Decimales del Campo: ", bytesSize[1])
            else:
              print("El archivo No es un DBF")  
        else:
          print("El archivo Esta Vacio")            
else:
    print("El archivo No existe")
