import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageDraw, ImageFont
from PIL.ImageQt import ImageQt

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo55.ui", self)
        lblGrafico = self.findChild(QtWidgets.QLabel, "lblGrafico")
        ancho = lblGrafico.width()
        alto = lblGrafico.height()
        mitadAncho = int(ancho / 2)
        mitadAlto = int(alto / 3)
        #Crear un Grafico usando PIL
        img = Image.new("RGBA", (ancho,alto), (0,0,0,0))
        grafico = ImageDraw.Draw(img)
        grafico.rectangle([0, 0, ancho, alto], fill="black", outline=None, width=1)
        fuente = ImageFont.truetype("arial.ttf", 50)
        grafico.text((150, 20), "Graficos en PyQT", font = fuente, fill = "white")
        grafico.line((0, 80, lblGrafico.width(), 80), fill="yellow", width=3)
        grafico.ellipse([mitadAncho-100, mitadAlto-50, mitadAncho+100, mitadAlto+50], fill="green", outline="yellow", width=3)
        archivoLogo = r"C:\Data\Python\2025_01_PythonMJ\Imagenes\Logos\LogoTDS.png"
        bmp = Image.open(archivoLogo)
        bmp2 = bmp.resize((300,150))
        img.paste(bmp2, (mitadAncho-150,mitadAlto+100))
        qim = ImageQt(img)
        pix = QPixmap.fromImage(qim)
        lblGrafico.setPixmap(pix)

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())