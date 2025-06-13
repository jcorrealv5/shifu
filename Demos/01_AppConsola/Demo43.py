from datetime import datetime

class beLog:
    def __init__(self, modulo, clase):
        self.FechaHora = str(datetime.now())
        self.Modulo = modulo
        self.Clase = clase
    
    def setLog(self, metodo, error):
        self.Metodo = metodo
        self.Error = error
    
    def printLog(self):
        print("Fecha y Hora:", self.FechaHora)
        print("Modulo:", self.Modulo)
        print("Clase:", self.Clase)
        print("Metodo:", self.Metodo)
        print("Error:", self.Error)