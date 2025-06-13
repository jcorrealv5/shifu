import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QMessageBox
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo07.ui", self)
        #Obtener los controles a programar
        self.txtCodigo = self.findChild(QtWidgets.QLineEdit, "txtCodigo")
        self.txtApellidos = self.findChild(QtWidgets.QLineEdit, "txtApellidos")
        self.txtNombres = self.findChild(QtWidgets.QLineEdit, "txtNombres")
        self.txtCorreo = self.findChild(QtWidgets.QLineEdit, "txtCorreo")
        btnPrimero = self.findChild(QtWidgets.QPushButton, "btnPrimero")
        btnAnterior = self.findChild(QtWidgets.QPushButton, "btnAnterior")
        btnSiguiente = self.findChild(QtWidgets.QPushButton, "btnSiguiente")
        btnUltimo = self.findChild(QtWidgets.QPushButton, "btnUltimo")
        self.txtPosicion = self.findChild(QtWidgets.QLineEdit, "txtPosicion")
        self.posicion = 0
        #Programar los eventos de los controles
        btnPrimero.clicked.connect(self.irPrimerRegistro)
        btnAnterior.clicked.connect(self.irRegistroAnterior)
        btnSiguiente.clicked.connect(self.irRegistroSiguiente)
        btnUltimo.clicked.connect(self.irUltimoRegistro)
        self.cargarRegistros()
    
    def cargarRegistros(self):
        archivoConfig=r"C:\Users\jhonf\Documents\Shifu\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Users\jhonf\Documents\Shifu\Demos\Logs\LogPyQtDemo05.txt"
        conexion = clienteSQL(archivoConfig,archivoLog)
        rpta = conexion.EjecutarComandoCadena("uspAlumnoListarCsv")
        msg = QMessageBox()
        if(rpta is not None):
            if(rpta!=""):
                self.ListaAlumnos = rpta.split("¬")
                self.NumReg = len(self.ListaAlumnos)
                self.mostrarRegistro()
            else:
                msg.setText("No existen Alumnos")
                msg.exec()
        else:
            msg.setText("Ocurrio un error al cargar los Alumnos")
            msg.exec()
    
    def mostrarRegistro(self):
        registro = self.ListaAlumnos[self.posicion]
        campos = registro.split("|")
        self.txtCodigo.setText(campos[0])
        self.txtApellidos.setText(campos[1])
        self.txtNombres.setText(campos[2])
        self.txtCorreo.setText(campos[3])
        self.txtPosicion.setText(f"{self.posicion + 1} de {self.NumReg}")
    
    def irPrimerRegistro(self):
        self.posicion = 0
        self.mostrarRegistro()
    
    def irRegistroAnterior(self):
        if(self.posicion>0):
            self.posicion -= 1
            self.mostrarRegistro()
    
    def irRegistroSiguiente(self):
        if(self.posicion<self.NumReg -1):
            self.posicion += 1
            self.mostrarRegistro()
    
    def irUltimoRegistro(self):
        self.posicion = self.NumReg - 1
        self.mostrarRegistro()
    
app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())