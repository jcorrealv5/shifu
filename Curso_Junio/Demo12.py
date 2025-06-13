import os, math, hashlib #Librerias Estandar de Python
import cv2 #Libreria Externa OpenCV
import matplotlib.pyplot as plt #Libreria Externa matplotlib

print("Demo 12: Funcion que Plotea Imagenes de un Directorio sin Repetir Archivos")

def crearArrayImagenes(directorio):
    imagenes = []
    hashs = []
    if os.path.isdir(directorio):
        archivos = os.listdir(directorio)
        for nombre in archivos:
            print(nombre)
            archivo = carpeta + nombre
            with open(archivo,"rb") as file:
                buffer = file.read()
                objResumen = hashlib.sha256()
                objResumen.update(buffer)
                resumen = objResumen.digest()
                if not resumen in hashs:
                    hashs.append(resumen)
                    imagen = cv2.imread(archivo, 0)
                    imagen = cv2.resize(imagen,(200,200))
                    print(imagen.shape)
                    imagenes.append(imagen)
                else:
                    print("Ya existe el archivo")
    return imagenes

def graficarImagenes(imagenes, archivo):
    nImagenes = len(imagenes)
    nSize = math.ceil(math.sqrt(nImagenes))
    figura, ejes = plt.subplots(nSize,nSize)
    for i in range(nSize):
        for j in range(nSize):
            n = i * nSize + j
            if(n<nImagenes):
                ejes[i,j].imshow(imagenes[n], cmap="gray")
            else:
                break
    plt.savefig(archivo)
    plt.show()

carpeta = "C:/Data/Python/2025_06_DADLCV/Imagenes/"
imagenes = crearArrayImagenes(carpeta)
graficarImagenes(imagenes, "Productos.png")