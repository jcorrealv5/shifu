#Demo 03: Bucle For en Python
titulo = "Demo 03: Bucle For en Python"
print(titulo)
print("_" * len(titulo))
rango = range(32,256,1)
for i in rango:
    print(i, "=", chr(i))
