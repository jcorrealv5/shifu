import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QModelIndex
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL
from modWindowsPyQt import CustomTableViewModel, MessageBox
from PyQt5.QtGui import QPixmap, QPainter, QImage, QFont, QColor, QPainterPath, QBrush

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo63.ui", self)
        
        tblCategoria = self.findChild(QtWidgets.QTableView, "tblCategoria")
        self.lblGrafico = self.findChild(QtWidgets.QLabel, "lblGrafico")
        btnGrabarGrafico = self.findChild(QtWidgets.QPushButton, "btnGrabarGrafico")
        btnGrabarGrafico.clicked.connect(self.grabarGrafico)
        
        self.ancho = self.lblGrafico.width()
        self.alto = self.lblGrafico.height()
        
        archivoConfig=r"C:\Users\jhonf\Documents\Shifu\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Users\jhonf\Documents\Shifu\Demos\Logs\LogPyQtDemo05.txt"
        con = clienteSQL(archivoConfig, archivoLog)
        data = con.EjecutarComandoCadena("uspCategoriaProductosStock2Csv")
        if(data is not None):
            if(data!=""):
                listaCategorias = data.split("¬")
                nRegistros = len(listaCategorias)
                modelo = CustomTableViewModel(listaCategorias)
                tblCategoria.setModel(modelo)
                maxStock = 0
                self.categorias = []
                self.stocks = []
                for i in range(3, nRegistros):
                    campos=listaCategorias[i].split("|")
                    self.categorias.append(campos[0][:5])                    
                    stock = int(campos[1])
                    self.stocks.append(stock)
                    if(stock>maxStock):
                        maxStock=stock
                self.escalaV = (self.alto - 120) / maxStock
                self.indice = 0
                tblCategoria.selectionModel().currentRowChanged.connect(self.seleccionarFila)
                self.graficarBarras()
    
    def seleccionarFila(self, pos:QModelIndex, previo:QModelIndex):
        self.indice = pos.row()
        self.graficarBarras()

    def graficarBarras(self):
        #Graficar usando QPainter
        img = QImage(self.ancho,self.alto,QImage.Format_RGB32)
        self.pix = QPixmap.fromImage(img)
        qp = QPainter()
        qp.begin(self.pix)              
        qp.setFont(QFont("Arial", 20, QFont.Bold)) 
        qp.setPen(QColor("white"))
        qp.drawText(150, 50, "Grafico de Stocks")                
        qp.setFont(QFont("Arial", 10))
        posX = 30
        for i in range(len(self.categorias)):
            valor = int(self.stocks[i] * self.escalaV)
            qp.drawText(posX, self.alto - 30, self.categorias[i])
            if(self.indice==i):
                colorBarra = QColor("red")
            else:
                colorBarra = QColor("yellow")
            qp.fillRect(posX, self.alto - (valor + 50), 40, valor, colorBarra)
            qp.fillRect(posX + 10, self.alto - (valor + 60), 40, valor, colorBarra)
            self.dibujarTrianguloSuperior(qp, colorBarra, posX, self.alto - (valor + 50))
            self.dibujarTrianguloInferior(qp, colorBarra, posX, self.alto - 50)
            qp.drawText(posX, self.alto - (valor + 70), str(self.stocks[i]))
            posX += 70
        qp.end()
        self.lblGrafico.setPixmap(self.pix)
        self.lblGrafico.resize(self.ancho,self.alto)
    
    def dibujarTrianguloSuperior(self, qp, color, x, y):
        path = QPainterPath()
        path.moveTo(x,y)
        path.lineTo(x,y)
        path.lineTo(x+10,y-10)
        path.lineTo(x+10,y)
        qp.fillPath(path, color)
    
    def dibujarTrianguloInferior(self, qp, color, x, y):
        path = QPainterPath()
        path.moveTo(x+40,y-10)
        path.lineTo(x+40,y-10)
        path.lineTo(x+50,y-10)
        path.lineTo(x+40,y)
        qp.fillPath(path, color)
                
    def grabarGrafico(self):
        pos = self.indice
        self.indice=-1
        self.graficarBarras()
        self.pix.save("Grafico_Stock_Columnas_2D_QPainter.png")
        self.indice=pos
        self.graficarBarras()
        MessageBox.Show("Se grabo el Grafico")

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())