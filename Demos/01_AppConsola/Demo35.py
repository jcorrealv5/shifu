import os, base64

#Demo 34: Convertir un Archivo de Imagen en Base64 y Comprimir
print("Demo 35: Convertir un Archivo Cifrado XOR en Base 64 a Imagen")

archivoCif = input("Ingresa un Archivo Cifrado (cif): ")
if(os.path.isfile(archivoCif)):
    campos = os.path.basename(archivoCif).split(".")
    tipo = campos[-1].lower()
    if(tipo=="cif"):
        bytesCifrado = None
        with open(archivoCif, "rb") as file1:
            bytesCifrado = file1.read()
        if(bytesCifrado is not None):
            nSize = len(bytesCifrado)
            buffer = []
            for i in range(nSize):
               buffer.append(bytesCifrado[i] ^ 10)
            archivoJpg = archivoCif.replace(".cif","")
            bytesBase64 = base64.b64decode(bytes(buffer))
            with open(archivoJpg, "wb") as file2:
                file2.write(bytesBase64)
            print("El archivo jpg fue creado")
    else:
        print("El archivo No tiene extension cif")
else:
    print("Archivo No existe")