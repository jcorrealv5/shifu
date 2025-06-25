import os, cv2
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
import joblib
from datetime import datetime
import numpy as np

horaInicio = datetime.now()
print("Demo 29: Crear un DataSet, Entrenar y Guardar un Modelo Entrenado de Firmas")

print("1. Crear el DataSet de Firmas")
rutaDataSet = "C:/Users/jhonf/Documents/Shifu/DataSets/Firmas"
directorios = os.listdir(rutaDataSet)
listaX = []
listaY = []
for c,directorio in enumerate(directorios):
    print(directorio)
    carpeta = os.path.join(rutaDataSet,directorio)
    archivos = os.listdir(carpeta)    
    for nombre in archivos:        
        print(nombre)
        archivo = os.path.join(carpeta,nombre)
        imagen = cv2.imread(archivo, 0)
        imagen = cv2.resize(imagen, (80,40))
        imagen = imagen.reshape(3200)
        listaX.append(imagen)
        listaY.append(c)
X = np.array(listaX)
y = np.array(listaY)

print("2. Dividiendo la Data en Entrenamiento y Pruebas")
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
joblib.dump(modelo, "Firmas.pkl")

horaFin = datetime.now()
tiempo = horaFin - horaInicio
print(f"Proceso Completado en: {tiempo.total_seconds()} seg")