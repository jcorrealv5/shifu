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

        imagen = Image.open("sprite2-removebg-preview.png")
        
        columnas = 9
        filas = 6
        
        ancho, alto = imagen.size
        ancho_celda = ancho // columnas
        alto_celda = alto // filas
        
        self.sprites = []
        for fila in range(filas):
            for columna in range(columnas):
                x1 = columna * ancho_celda
                y1 = fila * alto_celda
                x2 = x1 + ancho_celda
                y2 = y1 + alto_celda
                sprite = imagen.crop((x1, y1, x2, y2))
                sprite = sprite.resize((80,100))
                self.sprites.append(sprite)
                # sprite.save(f"sprite_{fila}_{columna}.png")
    
    def animar(self):
        self.texto = self.txtMensaje.text()
        self.posX = len(self.texto) * -50
        self.frame_actual = 0
        self.sprite_x = 50
        self.sprite_y = 200
        self.timer.start(250)
    
    def animarTexto(self):
        img = Image.new("RGBA", (self.ancho,self.alto), (0,0,0,0))
        grafico = ImageDraw.Draw(img)
        grafico.rectangle([0, 0, self.ancho, self.alto], fill="black", outline=None, width=1)
        fuente = ImageFont.truetype("arial.ttf", 100)
        grafico.text((self.posX, 100), self.texto, font = fuente, fill = "white")

        sprite = self.sprites[self.frame_actual].convert("RGBA")
        mascara = sprite.split()[3]
        img.paste(sprite, (self.sprite_x, self.sprite_y), mascara)

        qim = ImageQt(img)
        pix = QPixmap.fromImage(qim)
        self.lblGrafico.setPixmap(pix)
        if(self.posX<self.ancho):
            self.posX += 10
        else:
            self.posX = len(self.texto) * -50

        self.frame_actual = (self.frame_actual + 1) % len(self.sprites)
        if self.frame_actual == 1:
            self.sprite_x = 50
        else:
            self.sprite_x += self.ancho // len(self.sprites)

        

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())