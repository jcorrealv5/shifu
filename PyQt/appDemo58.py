import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL
from modWindowsPyQt import CustomTableViewModel, MessageBox
from PIL import Image, ImageDraw, ImageFont
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmap

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo58.ui", self)
        
        tblCategoria = self.findChild(QtWidgets.QTableView, "tblCategoria")
        lblGrafico = self.findChild(QtWidgets.QLabel, "lblGrafico")
        btnGrabarGrafico = self.findChild(QtWidgets.QPushButton, "btnGrabarGrafico")
        btnGrabarGrafico.clicked.connect(self.grabarGrafico)
        
        ancho = lblGrafico.width()
        alto = lblGrafico.height()
        
        archivoConfig = r"C:\Data\Python\2025_01_PythonMJ\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog = r"C:\Data\Python\2025_01_PythonMJ\Demos\Logs\PyQtDemo46.txt"
        con = clienteSQL(archivoConfig, archivoLog)
        data = con.EjecutarComandoCadena("uspCategoriaProductosStock2Csv")
        if(data is not None):
            if(data!=""):
                listaCategorias = data.split("¬")
                nRegistros = len(listaCategorias)
                modelo = CustomTableViewModel(listaCategorias)
                tblCategoria.setModel(modelo)
                maxStock = 0
                categorias = []
                stocks = []
                for i in range(3, nRegistros):
                    campos=listaCategorias[i].split("|")
                    categorias.append(campos[0][:4])                    
                    stock = int(campos[1])
                    stocks.append(stock)
                    if(stock>maxStock):
                        maxStock=stock
                escalaV = (alto - 100) / maxStock
                #Graficar usando PIL
                self.img = Image.new("RGBA", (ancho, alto), (0,0,0,0))
                grafico = ImageDraw.Draw(self.img)
                grafico.rectangle([0, 0, ancho, alto], fill="black", outline=None, width=1)
                fuente = ImageFont.truetype("arial.ttf", 20)
                posX = 30
                grafico.text((200, 20), "Grafico de Stocks", font = fuente, fill = "white") 
                for i in range(len(categorias)):
                    valor = stocks[i] * escalaV
                    grafico.text((posX, alto - 40), categorias[i], font = fuente, fill = "white") 
                    grafico.rectangle([posX, alto - (valor + 50), posX + 40, alto - 50], fill="yellow", outline=None, width=1)
                    grafico.text((posX, alto - (valor + 80)), str(stocks[i]), font = fuente, fill = "white")                     
                    posX += 70
                qim = ImageQt(self.img)
                pix = QPixmap.fromImage(qim)
                lblGrafico.setPixmap(pix)
                
    def grabarGrafico(self):
        self.img.save("Grafico_Stock_Columnas.png")
        MessageBox.Show("Se grabo el Grafico")

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())