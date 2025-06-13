import sys, os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL
from PyQt5.QtGui import QPixmap, QImage

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo14.ui", self)
        #Obtener los controles a programar
        self.txtCodigo = self.findChild(QtWidgets.QLineEdit, "txtCodigo")        
        self.txtApellidos = self.findChild(QtWidgets.QLineEdit, "txtApellidos")
        self.txtNombres = self.findChild(QtWidgets.QLineEdit, "txtNombres")
        self.txtFechaNacimiento = self.findChild(QtWidgets.QLineEdit, "txtFechaNacimiento")
        self.txtDocumentoIdentidad = self.findChild(QtWidgets.QLineEdit, "txtDocumentoIdentidad")
        self.imgFoto = self.findChild(QtWidgets.QLabel, "imgFoto")
        btnPrimero = self.findChild(QtWidgets.QPushButton, "btnPrimero")
        btnAnterior = self.findChild(QtWidgets.QPushButton, "btnAnterior")
        btnSiguiente = self.findChild(QtWidgets.QPushButton, "btnSiguiente")
        btnUltimo = self.findChild(QtWidgets.QPushButton, "btnUltimo")
        self.txtPosicion  = self.findChild(QtWidgets.QLineEdit, "txtPosicion")
        #Programar los eventos de los controles
        btnPrimero.clicked.connect(lambda: self.consultarRegistro(btnPrimero.text()))
        btnAnterior.clicked.connect(lambda: self.consultarRegistro(btnAnterior.text()))
        btnSiguiente.clicked.connect(lambda: self.consultarRegistro(btnSiguiente.text()))
        btnUltimo.clicked.connect(lambda: self.consultarRegistro(btnUltimo.text()))
        #Conectar a Base de Datos y traer los Alumnos
        archivoConfig=r"C:\Users\jhonf\Documents\Shifu\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Users\jhonf\Documents\Shifu\Demos\Logs\LogPyQtDemo05.txt"
        self.Conexion = clienteSQL(archivoConfig,archivoLog)
        self.ListaAlumnos = None
        self.NroRegistros = 0
        self.IndiceRegistro=0
        data = self.Conexion.EjecutarComandoCadena("uspProfesorListarCsv")
        if(data is not None):
            if(data!=""):
                self.ListaProfesores = data.split("¬")
                self.NroRegistros = len(self.ListaProfesores)
                self.consultarRegistro("<<")
            else:
                print("No existen Profesores registrados") 
        else:
             print("Ocurrio un Error al traer los Profesores") 
    
    def consultarRegistro(self, opcion):
        if(self.ListaProfesores is not None):
            if(opcion=="<<"):
                self.IndiceRegistro=0
            elif(opcion=="<" and self.IndiceRegistro>0):
                self.IndiceRegistro-=1
            elif(opcion==">" and self.IndiceRegistro<self.NroRegistros-1):
                self.IndiceRegistro+=1
            elif(opcion==">>"):
                self.IndiceRegistro=self.NroRegistros-1
            self.txtPosicion.setText(f"{self.IndiceRegistro+1} de {self.NroRegistros}")
            fila = self.ListaProfesores[self.IndiceRegistro]
            campos = fila.split("|")
            self.txtCodigo.setText(campos[0])
            self.txtApellidos.setText(campos[1])
            self.txtNombres.setText(campos[2])
            self.txtFechaNacimiento.setText(campos[3])
            self.txtDocumentoIdentidad.setText(campos[4])
            rutaFotos = "C:/Users/jhonf/Documents/Shifu/Profesores/"
            archivo = os.path.join(rutaFotos, campos[0] + ".jpg")
            if(os.path.isfile(archivo)):
                with open(archivo, "rb") as file:
                    buffer = file.read()
                qImg = QImage()
                qImg.loadFromData(buffer)
            else:
                qImg = None
            pix = QPixmap(qImg)
            self.imgFoto.setPixmap(pix)
            
app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())