from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt

print("Demo 25: Trabajando con MNIST-784")

print("1. Cargando el DataSet MNIST-784")
dst = fetch_openml("mnist_784", parser="auto", as_frame=False)

print("2. Mostrando las Claves del DataSet")
print(dst.keys())

X = dst["data"]
y = dst["target"]

print("3. Mostrando las Dimensiones de los Datos")
print("Shape de Datos de Entrada X: ", X.shape)
print("Shape de Datos de Entrada y: ", y.shape)

print("4. Dibujar los 25 Primeros Datos de Entrada y su Salida")
nSize = 5
figura, ejes = plt.subplots(nSize,nSize)
for i in range(nSize):
    for j in range(nSize):
        n = (i * nSize) + j
        imagen = X[n].reshape(28,28)
        ejes[i,j].imshow(imagen, cmap="gray")
        ejes[i,j].set_title(str(y[n]))
        ejes[i,j].set_axis_off()
plt.show()
