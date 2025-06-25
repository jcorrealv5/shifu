import numpy as np

class Activacion():
    def Sigmoide(x):
        return (1/(1+np.exp(-x)))
	
    def TangenteHiperbolica(x):
        return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
    
    def ReLU(x):
        return np.maximum(0, x)
    
    def LeakyRelu(alpha,x):
        return(np.maximum(alpha*x,x))