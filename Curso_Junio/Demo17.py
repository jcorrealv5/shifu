print("Demo 17: Red Neuronal Perceptron Simple")

peso = 0.1
epocas = 100000
sesgo = 5
ratioAprendizaje = 0.01
X=[10,20,5,4,1]
y=[25,45,15,13,7]
print("Entrada:", X)
print("Salida:", y)

def predecir(x):
    return ((peso * x)+sesgo)

for i in range(epocas):
    y_preds = [predecir(i) for i in X]
    print("y_preds: ", y_preds)
    costos = [r-p for p,r in zip(y_preds,y)]
    print("costos: ", costos)
    costo_promedio = sum(costos)/len(y)
    peso += ratioAprendizaje*costo_promedio
    sesgo += ratioAprendizaje*costo_promedio
    print(f"Epoca: {i+1}, Peso: {peso}, Sesgo: {sesgo}, Costo Prom: {costo_promedio}")
    if(costo_promedio==0):
        break

X_test = [100,2,33,4,7,8]
y_preds = [predecir(i) for i in X_test]
print("Prediccion Final: ",y_preds) 