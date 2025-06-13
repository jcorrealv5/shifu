import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QMessageBox
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo06.ui", self)
        #Obtener los controles a programar
        self.txtCodigo = self.findChild(QtWidgets.QSpinBox, "txtCodigo")
        btnConsultar = self.findChild(QtWidgets.QPushButton, "btnConsultar")        
        self.txtNombre = self.findChild(QtWidgets.QLineEdit, "txtNombre")
        self.txtCreditos = self.findChild(QtWidgets.QLineEdit, "txtCreditos")
        self.txtHoras = self.findChild(QtWidgets.QLineEdit, "txtHoras")
        #Programar los eventos de los controles
        btnConsultar.clicked.connect(self.consultarRegistro)
    
    def consultarRegistro(self):
        idCurso = self.txtCodigo.value()
        msg = QMessageBox()
        archivoConfig=r"C:\Users\jhonf\Documents\Shifu\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Users\jhonf\Documents\Shifu\Demos\Logs\LogPyQtDemo05.txt"
        conexion = clienteSQL(archivoConfig,archivoLog)
        rpta = conexion.EjecutarComandoCadena("uspCursoObtenerPorIdCsv", "IdCurso", idCurso)            
        if(rpta is not None):
            if(rpta!=""):
                campos = rpta.split("|")
                self.txtNombre.setText(campos[0])
                self.txtCreditos.setText(campos[1])
                self.txtHoras.setText(campos[2])
            else:
                self.txtNombre.setText("")
                self.txtCreditos.setText("")
                self.txtHoras.setText("")
                msg.setText("No existe el Curso con ese Codigo")
                msg.exec()
        else:
            msg.setText("Ocurrio un Error al Consultar el Curso")
            msg.exec()

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())