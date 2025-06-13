import sys, cv2
import numpy as np
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QThread

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo70.ui", self)
        
        self.btnIniciarVideo = self.findChild(QtWidgets.QPushButton, "btnIniciarVideo")
        self.lblVideo = self.findChild(QtWidgets.QLabel, "lblVideo")
        
        self.btnIniciarVideo.clicked.connect(self.procesarVideo)
        self.hiloVideo = None
        
    def procesarVideo(self):
        if(self.hiloVideo is None and self.btnIniciarVideo.text()=="Iniciar Video"):
            self.btnIniciarVideo.setText("Finalizar Video")
            self.hiloVideo = WorkerVideo(self)
            self.hiloVideo.enviarFrame.connect(self.mostrarRptaEnviarFrame)
            self.hiloVideo.start()
        else: 
            self.btnIniciarVideo.setText("Iniciar Video")
            self.hiloVideo.terminate()
            self.hiloVideo = None
            pix = QPixmap(None)
            self.lblVideo.setPixmap(pix)

    def mostrarRptaEnviarFrame(self, img):
        (alto, ancho) = img.shape[:2]
        qImg = QImage(img, ancho, alto, 3 * ancho, QImage.Format_BGR888)
        pix = QPixmap(qImg)
        self.lblVideo.setPixmap(pix)

class WorkerVideo(QThread):
    enviarFrame = QtCore.pyqtSignal(np.ndarray)
    
    def __init__(self, parent):
        super(WorkerVideo, self).__init__(parent) 
    
    def run(self):
        video = cv2.VideoCapture(0)
        if(video.isOpened()):
            while True:
                rpta, img = video.read()
                if(rpta):
                    self.enviarFrame.emit(img)
                else:
                    break
            video.release()
            cv2.destroyAllWindows()
        else:
            print("No esta activa la Camara Web")
        

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())