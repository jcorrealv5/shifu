import numpy as np
from datetime import datetime
import torch

arrayX = np.random.random((1,30000))
arrayY = np.random.random((30000,10000))
print("Shape arrayX:", arrayX.shape)
print("Shape arrayY:", arrayY.shape)
inicio = datetime.now()
arrayZ = np.matmul(arrayX, arrayY)
fin = datetime.now()
tiempo = fin - inicio
print(f"Tiempo de NumPy: {tiempo}")

tensorX = torch.rand(1,30000)
tensorY = torch.rand(30000,10000)
print("Shape tensorX:", tensorX.shape)
print("Shape tensorY:", tensorY.shape)
inicio = datetime.now()
tensorZ = (tensorX@tensorY)
fin = datetime.now()
tiempo = fin - inicio
print(f"Tiempo de Torch CPU: {tiempo}")

tensorCudaX = torch.rand(1,30000).to("cuda")
tensorCudaY = torch.rand(30000,10000).to("cuda")
print("Shape tensorCudaX:", tensorCudaX.shape)
print("Shape tensorCudaY:", tensorCudaY.shape)
inicio = datetime.now()
tensorCudaZ = (tensorCudaX@tensorCudaY)
fin = datetime.now()
tiempo = fin - inicio
print(f"Tiempo de Torch GPU: {tiempo}")