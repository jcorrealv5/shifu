import os, base64

#Demo 34: Convertir un Archivo de Imagen en Base64 y Comprimir
print("Demo 34: Convertir un Archivo de Imagen en Base64 y Cifrado XOR")

archivoJpg = input("Ingresa un Archivo de Imagen jpg: ")
if(os.path.isfile(archivoJpg)):
    campos = os.path.basename(archivoJpg).split(".")
    tipo = campos[-1].lower()
    if(tipo=="jpg"):
        cifrado = ""
        with open(archivoJpg, "rb") as file1:
            data = file1.read()
            if(data[0]==255 and data[1]==216):
                bytesBase64 = base64.b64encode(data)
                nSize = len(bytesBase64)
                clave = 10                
                for i in range(nSize):
                    cifrado += chr(bytesBase64[i] ^ clave)        
            else:
              print("El archivo No es un jpg")
        if(cifrado!=""):
            archivoCifrado = archivoJpg + ".cif"
            with open(archivoCifrado, "w") as file2:
                file2.write(cifrado)
            print("El archivo de imagen fue cifrado")
    else:
        print("El archivo No tiene extension jpg")
else:
    print("Archivo No existe")