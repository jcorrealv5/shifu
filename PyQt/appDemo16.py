import sys, os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL
from PyQt5.QtGui import QPixmap, QImage

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo16.ui", self)
        #Obtener los controles a programar
        self.txtCodigo = self.findChild(QtWidgets.QLineEdit, "txtCodigo")        
        self.txtApellidos = self.findChild(QtWidgets.QLineEdit, "txtApellidos")
        self.txtNombres = self.findChild(QtWidgets.QLineEdit, "txtNombres")
        self.txtCorreo = self.findChild(QtWidgets.QLineEdit, "txtCorreo")
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
        archivoConfig=r"C:\Data\Python\2025_01_PythonMJ\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Data\Python\2025_01_PythonMJ\Demos\Logs\LogPyQtDemo05.txt"
        self.Conexion = clienteSQL(archivoConfig,archivoLog)
        self.ListaAlumnos = None
        self.NroRegistros = 0
        self.IndiceRegistro=0
        data = self.Conexion.EjecutarComandoCadena("uspAlumnoListarCsv")
        if(data is not None):
            if(data!=""):
                self.ListaAlumnos = data.split("¬")
                self.NroRegistros = len(self.ListaAlumnos)
                self.consultarRegistro("<<")
            else:
                print("No existen Alumnos registrados") 
        else:
             print("Ocurrio un Error al traer los Alumnos") 
    
    def consultarRegistro(self, opcion):
        if(self.ListaAlumnos is not None):
            if(opcion=="<<"):
                self.IndiceRegistro=0
            elif(opcion=="<" and self.IndiceRegistro>0):
                self.IndiceRegistro-=1
            elif(opcion==">" and self.IndiceRegistro<self.NroRegistros-1):
                self.IndiceRegistro+=1
            elif(opcion==">>"):
                self.IndiceRegistro=self.NroRegistros-1
            self.txtPosicion.setText(f"{self.IndiceRegistro+1} de {self.NroRegistros}")
            fila = self.ListaAlumnos[self.IndiceRegistro]
            campos = fila.split("|")
            self.txtCodigo.setText(campos[0])
            self.txtApellidos.setText(campos[1])
            self.txtNombres.setText(campos[2])
            self.txtCorreo.setText(campos[3])
            rutaFotos = "C:/Data/Python/2025_01_PythonMJ/Imagenes/AlumnosSec/"
            archivo = os.path.join(rutaFotos, campos[0] + ".jpg")
            if(os.path.isfile(archivo)):
                with open(archivo, "rb") as file:
                    bufferCifrado = file.read()
                nSize = len(bufferCifrado)
                clave = 10
                bufferDescifrado = []
                for i in range(nSize):
                    x = bufferCifrado[i] ^ clave
                    bufferDescifrado.append(x)
                buffer = bytes(bufferDescifrado)
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