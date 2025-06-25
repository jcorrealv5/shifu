from sklearn.neural_network import MLPClassifier

print("Demo 22: Usando MLP-sklearn para Predecir And, Or, Xor")
print("Creando un Modelo MLP")

modelo = MLPClassifier(solver='lbfgs')
X = [(0,0),(0,1),(1,0),(1,1)]
y_And = [0,0,0,1]
y_Or = [0,1,1,1]
y_Xor = [0,1,1,0]
X_test = [(1,1),(1,0),(0,1),(0,0)]
print("Datos a Predecir:\n", X_test)

print("Entrenar el Modelo para el And")
modelo.fit(X, y_And)
y_Pred_And = modelo.predict(X_test)
print("Datos Predecidos con And:\n", y_Pred_And)

print("Entrenar el Modelo para el Or")
modelo.fit(X, y_Or)
y_Pred_Or = modelo.predict(X_test)
print("Datos Predecidos con Or:\n", y_Pred_Or)

print("Entrenar el Modelo para el Xor")
modelo.fit(X, y_Xor)
y_Pred_Xor = modelo.predict(X_test)
print("Datos Predecidos con Xor:\n", y_Pred_Xor)