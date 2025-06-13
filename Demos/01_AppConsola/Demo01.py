# Demo 01: Primer ejemplo de Python para ingresar y mostrar datos
titulo = "Demo 01: Primer ejemplo de Python para ingresar y mostrar datos"
print(titulo)
print("_" * len(titulo))
nombre = input("Ingresa tu Nombre: ")
pais = input("Ingresa tu Pais: ")
anioNac = int(input("Ingresa Anio Nacimiento: "))
edad = 2025 - anioNac
print(f"Hola {nombre} asi que eres de {pais} y tienes {edad} anios")
