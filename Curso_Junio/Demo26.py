from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
import joblib
from datetime import datetime

horaInicio = datetime.now()
print("Demo 26: Entrenar y Guardar un Modelo Entrenado MNIST-784")

print("1. Cargando el DataSet MNIST-784")
dst = fetch_openml("mnist_784", parser="auto", as_frame=False)

print("2. Dividiendo la Data en Entrenamiento y Pruebas")
X = dst["data"]
y = dst["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
print("Shape X: ", X.shape)
print("Shape y: ", y.shape)
print("Shape X_train: ", X_train.shape)
print("Shape y_train: ", y_train.shape)

print("3. Crear el Modelo usando MLP")
modelo = MLPClassifier()

print("4. Entrenar el Modelo MLP")
modelo.fit(X_train, y_train)

print("5. Guardar el Modelo en un Archivo en Disco")
joblib.dump(modelo, "MNIST784.pkl")

horaFin = datetime.now()
tiempo = horaFin - horaInicio
print(f"Proceso Completado en: {tiempo.total_seconds()} seg")