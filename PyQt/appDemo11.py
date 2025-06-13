import sys, base64, os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QMessageBox
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL
from PyQt5.QtGui import QPixmap, QImage

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo11.ui", self)
        #Obtener los controles a programar
        self.txtCodigo = self.findChild(QtWidgets.QSpinBox, "txtCodigo")
        btnConsultar = self.findChild(QtWidgets.QPushButton, "btnConsultar")
        self.txtApellidos = self.findChild(QtWidgets.QLineEdit, "txtApellidos")
        self.txtNombres = self.findChild(QtWidgets.QLineEdit, "txtNombres")
        self.txtCorreo = self.findChild(QtWidgets.QLineEdit, "txtCorreo")
        self.imgFoto = self.findChild(QtWidgets.QLabel, "imgFoto")
        #Programar los eventos de los controles
        btnConsultar.clicked.connect(self.consultarRegistro)
    
    def consultarRegistro(self):
        idAlumno = self.txtCodigo.value()
        msg = QMessageBox()
        archivoConfig=r"C:\Users\jhonf\Documents\Shifu\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Users\jhonf\Documents\Shifu\Demos\Logs\LogPyQtDemo05.txt"
        rutaFotos = r"C:\Users\jhonf\Documents\Shifu\Alumnos"
        conexion = clienteSQL(archivoConfig,archivoLog)
        rpta = conexion.EjecutarComandoCadena("uspAlumnoObtenerPorIdCsv", "IdAlumno", idAlumno)            
        if(rpta is not None):
            qImg = QImage()
            if(rpta!=""):
                campos = rpta.split("|")
                self.txtApellidos.setText(campos[0])
                self.txtNombres.setText(campos[1])
                self.txtCorreo.setText(campos[2])
                archivoFoto = os.path.join(rutaFotos, str(idAlumno) + ".jpg")
                if(os.path.isfile(archivoFoto)):
                    with open(archivoFoto, "rb") as file:
                        buffer = file.read()
                    qImg.loadFromData(buffer)
                    pix = QPixmap(qImg)
                    self.imgFoto.setPixmap(pix)
            else:
                self.txtApellidos.setText("")
                self.txtNombres.setText("")
                self.txtCorreo.setText("")
                pix = QPixmap(None)
                self.imgFoto.setPixmap(pix)
                msg.setText("No existe el Alumno con ese Codigo")
                msg.exec()
        else:
            msg.setText("Ocurrio un Error al Consultar el Alumno")
            msg.exec()

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())