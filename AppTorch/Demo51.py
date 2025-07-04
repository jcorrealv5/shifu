import matplotlib.pyplot as plt
from torchvision import datasets
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader

def MostrarImagenes(filas, cols, imagenesTensor, etiquetasTensor):
    figura, ejes = plt.subplots(filas,cols)
    for i in range(filas):
        for j in range(cols):
            n = (i * cols) + j
            #Mostrar la Imagen como Array de NumPy
            imagenTensor = imagenesTensor[n]
            imagenArray = imagenTensor.detach().numpy().squeeze(0)
            ejes[i,j].imshow(imagenArray, cmap="gray")
            #Mostrar la Etqueta como Elemento de un Array de NumPy
            etiquetaTensor = etiquetasTensor[n]
            etiqueta = etiquetaTensor.detach().numpy()
            ejes[i,j].set_title(etiqueta)
    plt.show()

print("Demo 51: Leer y Graficar Imagenes del DataSet MNIST con PyTorch")

print("1. Crear el DataSet de MNIST y grabar a Disco")
dsTrain = datasets.MNIST(root="datasets",train=True,download=True,transform=ToTensor())
print("DataSet Train: ", dsTrain)

print("2. Crear el DataLoader para manejar el DataSet MNIST")
dlTrain = DataLoader(dsTrain, batch_size=100, shuffle=True)
print("DataLoader Train: ", dlTrain)

print("3. Iterar a través del DataLoader")
X_train, y_train = next(iter(dlTrain))
print(f"Shape Data Entrada: {X_train.shape}")
print(f"Shape Data Salida: {y_train.shape}")

print("4. Graficar los 64 digitos del DataLoader")
MostrarImagenes(10,10,X_train,y_train)