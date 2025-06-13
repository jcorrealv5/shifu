print("Demo 13: Clases y Objetos Compartidos")

class Calculo():    
	def Suma(x,y):
		return x + y
	
	def Producto(x,y):
		return x * y

suma1 = Calculo.Suma(10,2)
prod1 = Calculo.Producto(10,2)
print("suma1:", suma1)
print("prod1:", prod1)

suma2 = Calculo.Suma(4,5)
prod2 = Calculo.Producto(4,5)
print("suma2:", suma2)
print("prod2:", prod2)
