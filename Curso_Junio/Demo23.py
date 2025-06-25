from sklearn.datasets import load_digits
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

print("Demo 23: Usando MLP-sklearn para Predecir Digitos con Division Manual Secuencial")

dst = load_digits()
print("Claves del DataSet: ", dst.keys())
X = dst["data"]
y = dst["target"]
print("Shape Datos de Entrada X:", X.shape)
print("Shape Datos de Salida y:", y.shape)

print("1. Creando un Modelo de Tipo MLP")
modelo = MLPClassifier()

print("2. Entrenar el Modelo con los 1600 primeros registros")
X_train = X[:1600]
y_train = y[:1600]
modelo.fit(X_train, y_train)

print("3. Predecir con los otros datos")
X_test = X[1600:]
y_test = y[1600:]
n_test = len(X_test)
y_pred = modelo.predict(X_test)

print("Cantidad de Pruebas: ", n_test)
print("Digitos Predecidos: ", y_pred)
score = modelo.score(X_test, y_test)
print("Score de Prediccion: ", score)
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.show()