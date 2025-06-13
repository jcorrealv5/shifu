import  os

print("Demo15: App de Consola par Cifrar las Fotos de Alumnos")
rutaOrigen = "C:/Users/jhonf/Documents/Shifu/Alumnos/"
rutaDestino = "C:/Users/jhonf/Documents/Shifu/Alumnos1sec/"
archivos = os.listdir(rutaOrigen)
for archivo in archivos:
    print("Cifrando: ", archivo)
    archivoOrigen = os.path.join(rutaOrigen, archivo)
    with open(archivoOrigen, "rb") as fileOrigen:
        bufferOrigen = fileOrigen.read()
    nSize = len(bufferOrigen)
    clave = 10
    bufferDestino = []
    for i in range(nSize):
        x = bufferOrigen[i] ^ clave
        bufferDestino.append(x)
    buffer = bytes(bufferDestino)
    archivoDestino = os.path.join(rutaDestino, archivo)
    with open(archivoDestino, "wb") as fileDestino:
        fileDestino.write(buffer)
print(f"Se cifraron: {len(archivos)} archivos")
