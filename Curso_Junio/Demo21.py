import numpy as np

print("Demo 21: Perceptron MultiCapa (MLP) con Aprendizaje BackProp")

def sigmoide(x):
    return 1.0/(1.0+np.exp(-x))

def sigmoideDerivada(x):
    return sigmoide(x) * (1.0-sigmoide(x))

def tangente(x):
    return np.tanh(-x)

def tangenteDerivada(x):
    return 1.0 - x**2

class MLP():
    def __init__(self, capas, activacion="tangente"):
        if activacion=="sigmoide":
            self.activacion = sigmoide
            self.activacionDerivada = sigmoideDerivada
        elif activacion=="tangente":
            self.activacion = tangente
            self.activacionDerivada = tangenteDerivada
        self.pesos = []
        self.deltas = []
        #Asignar pesos aleatorios a capa de entrada y capa oculta
        for i in range(1,len(capas)-1):
            peso = 2 * np.random.random((capas[i-1]+1, capas[i]+1))-1
            self.pesos.append(peso)
        #Asignar peso aleatorio a capa de salida
        peso = 2 * np.random.random((capas[i]+1, capas[i+1]))-1
        self.pesos.append(peso)
        
    def Entrenar(self, X, y, tasa_aprendizaje=0.2, epocas=100000):
        sesgo = np.atleast_2d(np.ones(X.shape[0]))
        X = np.concatenate((sesgo.T, X), axis=1)
        for i in range(epocas):
            c = np.random.randint(X.shape[0])
            a = [X[c]]
            for j in range(len(self.pesos)):
                valor = np.dot(a[j], self.pesos[j])
                activacion = self.activacion(valor)
                a.append(activacion)
            #Calcular la diferencia en la capa de salida y el valor obtenido
            error = y[c] - a[-1]
            deltas = [error * self.activacionDerivada(a[-1])]            
            #Desde la segunda capa hasta el ultimo
            for j in range(len(a)-2,0,-1):
                deltas.append(deltas[-1].dot(self.pesos[j].T)*self.activacionDerivada(a[j]))
            self.deltas.append(deltas)
            deltas.reverse()
            #Backpropagation
            for j in range(len(self.pesos)):
                capa = np.atleast_2d(a[j])
                delta = np.atleast_2d(deltas[j])
                self.pesos[j] += tasa_aprendizaje * capa.T.dot(delta)
            #if i%100==0:
            #    print("Epoca", i)
	
    def Predecir(self, x):
        a = np.concatenate((np.ones(1).T, np.array(x)), axis=0)
        for i in range(0, len(self.pesos)):
            a = self.activacion(np.dot(a, self.pesos[i]))
        return a

#Prediccion del And
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[0],[0],[1]])
modelo = MLP([2,3,1], activacion="sigmoide")
print("Entrenando And")
modelo.Entrenar(X, y, tasa_aprendizaje=0.01, epocas=100000)
X_test = np.array([[1,1],[0,1],[0,0],[1,0]])
for i,x in enumerate(X):
    y_pred = np.round(modelo.Predecir(x))
    print(f"Prediccion And {x}: {y_pred}")

#Prediccion del Or
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[1]])
modelo = MLP([2,3,1], activacion="sigmoide")
print("Entrenando Or")
modelo.Entrenar(X, y, tasa_aprendizaje=0.01, epocas=100000)
X_test = np.array([[1,1],[0,1],[0,0],[1,0]])
for i,x in enumerate(X):
    y_pred = np.round(modelo.Predecir(x))
    print(f"Prediccion Or {x}: {y_pred}")

#Prediccion del XOR
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])
modelo = MLP([2,3,3,4,4,3,3,2,2,1], activacion="tangente")
print("Entrenando XOR")
modelo.Entrenar(X, y, tasa_aprendizaje=0.01, epocas=100000)
X_test = np.array([[1,1],[0,1],[0,0],[1,0]])
for i,x in enumerate(X):
    y_pred = np.round(modelo.Predecir(x))
    print(f"Prediccion XOR {x}: {y_pred}")