import numpy as np
import matplotlib.pyplot as plt

print("Demo 19: Funciones de Activacion")

class Activacion():
    def Sigmoide(x):
        return (1/(1+np.exp(-x)))
	
    def TangenteHiperbolica(x):
        return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
    
    def ReLU(x):
        return np.maximum(0, x)
    
    def LeakyRelu(alpha,x):
        return(np.maximum(alpha*x,x))

X = np.arange(-10,10,0.1)
figura, ejes = plt.subplots(2,2)
ejes[0,0].plot(X, Activacion.Sigmoide(X), color="red")
ejes[0,0].set_title("F.A. Sigmoide")
ejes[0,1].plot(X, Activacion.TangenteHiperbolica(X), color="green")
ejes[0,1].set_title("F.A. Tangente Hiperbolica")
ejes[1,0].plot(X, Activacion.ReLU(X), color="blue")
ejes[1,0].set_title("F.A. ReLU")
ejes[1,1].plot(X, Activacion.LeakyRelu(3,X), color="brown")
ejes[1,1].set_title("F.A. Leaky Relu con Alpha 3")
plt.show()