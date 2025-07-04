import torch, cv2
from torch import nn,load
from torch.utils.data import DataLoader
import torch.nn.functional as F
from torchvision import datasets, transforms
import matplotlib.pyplot as plt

class MLP(nn.Module):
    def __init__(self, input_size,num_capas,num_clases):
        super(MLP, self).__init__()
        self.fc1 = nn.Linear(input_size, num_capas)
        self.fc2 = nn.Linear(num_capas, num_clases)
    def forward(self, x):
        x = x.view(-1, 28*28)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
        
print("1. Creando el Modelo de Red Neuronal")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
modelo = MLP(784,50,10).to(device)

print("2. Cargar el Modelo Pre Entrenado")
with open('MNIST.pt', 'rb') as f: 
     modelo.load_state_dict(load(f, map_location=device, weights_only=True))
     modelo.eval()

print("3. Creando los DataSets y DataLoaders para Pruebas")
dsTest = datasets.MNIST(root='datasets/', train=False, transform=transforms.ToTensor(), download=True)
dlTest = DataLoader(dataset=dsTest, batch_size=64, shuffle=False)

print("4. Cargar y Mostrar la Imagen a Predecir")
imagenes, etiquetas = next(iter(dlTest))
imagenTensor, etiquetaTensor = imagenes[63], etiquetas[63]
print("Shape Tensor Prueba: ", imagenTensor.shape)
print("Shape Tensor Salida: ", etiquetaTensor.shape)
imagenArray = imagenTensor.detach().numpy().squeeze(0)
etiqueta = etiquetaTensor.detach().numpy()
print("Shape Array Prueba: ", imagenArray.shape)
plt.imshow(imagenArray, cmap="gray")
plt.title(etiqueta)
plt.show()

print("5. Usar el Modelo para Clasificar el Digito")
with torch.no_grad():
    imagenPlana = imagenTensor.view(1, 784).to(device)
    print("Shape Data Prueba Final: ", imagenPlana.shape)
    salida = modelo(imagenPlana)
    print("Salida: ", salida)
    _, predecido = torch.max(salida, 1)
    print("predecido: ", predecido)
    prediccion = predecido.item()    
    print("Prediccion: ", prediccion)