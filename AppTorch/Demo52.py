import matplotlib.pyplot as plt
from torchvision import datasets
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader

etiquetas = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]
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
            ejes[i,j].set_title(etiquetas[etiqueta])
    plt.show()

print("Demo 52: Leer y Graficar Imagenes del DataSet Fashion-MNIST con PyTorch")

print("1. Crear el DataSet de Fashion-MNIST y grabar a Disco")
dsTrain = datasets.FashionMNIST(root="datasets",train=True,download=True,transform=ToTensor())
print("DataSet Train: ", dsTrain)

print("2. Crear el DataLoader para manejar el DataSet MNIST")
dlTrain = DataLoader(dsTrain, batch_size=100, shuffle=True)
print("DataLoader Train: ", dlTrain)

print("3. Iterar a través del DataLoader")
X_train, y_train = next(iter(dlTrain))
print(f"Shape Data Entrada: {X_train.shape}")
print(f"Shape Data Salida: {y_train.shape}")

print("4. Graficar las 100 ropas del DataLoader")
MostrarImagenes(10,10,X_train,y_train)