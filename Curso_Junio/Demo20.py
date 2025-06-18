import cv2, sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.append("../Modulos")
from ANN import Activacion

print("Demo 20: Usando una Funciones de Activacion")

archivo = r"C:\Users\jhonf\Documents\Shifu\shifu\Lena.png"
imagen = cv2.imread(archivo, 0).flatten()
X = (imagen / 128) - 1
print(X)
y = Activacion.TangenteHiperbolica(X)
print(y)
plt.plot(X, y, color="red")
plt.title("Funcion Sigmoide para Lena")
plt.show()
