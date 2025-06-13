import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PIL import Image, ImageDraw, ImageFont
from PIL.ImageQt import ImageQt

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo56.ui", self)
        self.txtMensaje = self.findChild(QtWidgets.QLineEdit, "txtMensaje")
        self.lblGrafico = self.findChild(QtWidgets.QLabel, "lblGrafico")
        btnAnimar = self.findChild(QtWidgets.QPushButton, "btnAnimar")
        self.ancho = self.lblGrafico.width()
        self.alto = self.lblGrafico.height()
        btnAnimar.clicked.connect(self.animar)        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animarTexto)
    
    def animar(self):
        self.texto = self.txtMensaje.text()
        self.posX = len(self.texto) * -50
        self.timer.start(50)
    
    def animarTexto(self):
        img = Image.new("RGBA", (self.ancho,self.alto), (0,0,0,0))
        grafico = ImageDraw.Draw(img)
        grafico.rectangle([0, 0, self.ancho, self.alto], fill="black", outline=None, width=1)
        fuente = ImageFont.truetype("arial.ttf", 100)
        grafico.text((self.posX, 100), self.texto, font = fuente, fill = "white")        
        qim = ImageQt(img)
        pix = QPixmap.fromImage(qim)
        self.lblGrafico.setPixmap(pix)
        if(self.posX<self.ancho):
            self.posX += 10
        else:
            self.posX = len(self.texto) * -50
        

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())