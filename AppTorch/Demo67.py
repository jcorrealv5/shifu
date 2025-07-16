import matplotlib.pyplot as plt
from torchvision import datasets
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader

etiquetas = []
def MostrarImagenes(filas, cols, imagenesTensor, etiquetasTensor):
    figura, ejes = plt.subplots(filas,cols)
    for i in range(filas):
        for j in range(cols):
            n = (i * cols) + j
            #Mostrar la Imagen como Array de NumPy
            imagenTensor = imagenesTensor[n]
            #print("imagenTensor:", imagenTensor.shape)
            imagenArray = imagenTensor.permute(1, 2, 0).numpy()
            print("imagenArray:", imagenArray.shape)
            ejes[i,j].imshow(imagenArray, cmap="viridis")
            #Mostrar la Etiqueta como Elemento de un Array de NumPy
            etiquetaTensor = etiquetasTensor[n]
            indiceEtiqueta = etiquetaTensor.detach().numpy()
            etiqueta = etiquetas[indiceEtiqueta]
            ejes[i,j].set_title(etiqueta)
    plt.show()

print("Demo 67: Leer y Graficar Imagenes del DataSet CIFAR100 con PyTorch")

print("1. Crear el DataSet ImageNet y grabar a Disco")
dsTrain = datasets.CIFAR100(root="datasets",download=True,transform=ToTensor())
print("DataSet Train: ", dsTrain)
etiquetas = dsTrain.classes
print("Etiquetas de Salida: ", etiquetas)

print("2. Crear el DataLoader para manejar el DataSet CIFAR100")
dlTrain = DataLoader(dsTrain, batch_size=36, shuffle=True)
print("DataLoader Train: ", dlTrain)

print("3. Iterar a través del DataLoader")
X_train, y_train = next(iter(dlTrain))
print(f"Shape Data Entrada: {X_train.shape}")
print(f"Shape Data Salida: {y_train.shape}")

print("4. Graficar las 36 imagenes del DataLoader")
MostrarImagenes(6,6,X_train,y_train)