print("Demo 18: Red Neuronal Perceptron Simple con Clases")

class Perceptron():
    def __init__(self):
        self.peso = 0.1
        self.sesgo = 1

    def Entrenar(self, X, y, peso, sesgo, epocas, ratioAprendizaje):
        self.X = X
        self.y = y
        self.peso = peso
        self.sesgo = sesgo
        self.epocas = epocas
        self.ratioAprendizaje = ratioAprendizaje
        for i in range(epocas):
            y_preds = [self.Predecir(i) for i in X]
            print("y_preds: ", y_preds)
            costos = [r-p for p,r in zip(y_preds,y)]
            print("costos: ", costos)
            costo_promedio = sum(costos)/len(y)
            self.peso += ratioAprendizaje*costo_promedio
            self.sesgo += ratioAprendizaje*costo_promedio
            print(f"Epoca: {i+1}, Peso: {self.peso}, Sesgo: {self.sesgo}, Costo Prom: {costo_promedio}")
            if(costo_promedio==0):
                break

    def Predecir(self, x):
        return ((self.peso * x)+self.sesgo)

X=[1,2,3,4,5]
y=[3,6,9,12,15]
modelo = Perceptron()
modelo.Entrenar(X=X, y=y, peso=0.8, sesgo=5, epocas=1000, ratioAprendizaje=0.05)

X_test = [2,4,6,8]
y_preds = [modelo.Predecir(i) for i in X_test]
print("Prediccion Final: ",y_preds) 