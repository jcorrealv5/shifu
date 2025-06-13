print("Demo 14: Clases y Objetos Instanciables")

class Calculo():
    def __init__(self, z=1):
        self.z = z

    def Suma(self,x,y):
        return x + y + self.z
	
    def Producto(self,x,y):
        return x * y * self.z

obj1 = Calculo(3)
obj2 = Calculo(5)

suma1 = obj1.Suma(10,2)
prod1 = obj1.Producto(10,2)
print("suma1:", suma1)
print("prod1:", prod1)

suma2 = obj2.Suma(4,5)
prod2 = obj2.Producto(4,5)
print("suma2:", suma2)
print("prod2:", prod2)
