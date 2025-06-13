import os, math #Librerias Estandar de Python
import cv2 #Libreria Externa OpenCV
import matplotlib.pyplot as plt #Libreria Externa matplotlib

print("Demo 11: Funcion que Plotea Imagenes de un Directorio")

def crearArrayImagenes(directorio):
    imagenes = []
    if os.path.isdir(directorio):
        archivos = os.listdir(directorio)
        for archivo in archivos:
            print(archivo)
            imagen = cv2.imread(carpeta + archivo, 0)
            imagen = cv2.resize(imagen,(200,200))
            print(imagen.shape)
            imagenes.append(imagen)
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

carpeta = "C:/Data/Python/2025_01_PythonMJ/Imagenes/Producto/"
imagenes = crearArrayImagenes(carpeta)
graficarImagenes(imagenes, "Productos.png")