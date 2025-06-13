import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog
sys.path.append("../00_Modulos")
from modUtilidades import Seguridad, Generador
from modWindowsPyQt import Captcha, MessageBox
from modAccesoDatos import clienteSQL

class Login(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.Rpta = ""
        uic.loadUi("dlgDemo64_Login.ui", self)
        self.txtUsuario = self.findChild(QtWidgets.QLineEdit, "txtUsuario")
        self.txtClave = self.findChild(QtWidgets.QLineEdit, "txtClave")
        self.txtCodigo = self.findChild(QtWidgets.QLineEdit, "txtCodigo")
        self.lblCaptcha = self.findChild(QtWidgets.QLabel, "lblCaptcha")
        btnAceptar = self.findChild(QtWidgets.QPushButton, "btnAceptar")
        btnCancelar = self.findChild(QtWidgets.QPushButton, "btnCancelar")
        
        self.lblCaptcha.mousePressEvent = self.cambiarCaptchaMouse
        btnAceptar.clicked.connect(self.validarLogin)
        btnCancelar.clicked.connect(self.salir)
        self.cambiarCaptcha()
    
    def cambiarCaptchaMouse(self, event):
        self.cambiarCaptcha()

    def cambiarCaptcha(self):
        self.codigoGenerado = Generador.Codigo(6)
        Captcha.Crear(self.lblCaptcha.width(), self.lblCaptcha.height(), self.codigoGenerado, 30, 10, self.lblCaptcha)

    def validarLogin(self):
        if(self.txtUsuario.text()!=""):
            if(self.txtClave.text()!=""):
                if(self.txtCodigo.text()!=""):
                    if(self.txtCodigo.text()==self.codigoGenerado):
                        usuario = self.txtUsuario.text()
                        clave = self.txtClave.text()
                        claveCifrada = Seguridad.CifrarSha256Hex(clave)
                        login = usuario + "|" + claveCifrada
                        archivoConfig = r"C:\Data\Python\2025_01_PythonMJ\Demos\00_Modulos\Config_BD_DACP_2025.txt"
                        archivoLog = r"C:\Data\Python\2025_01_PythonMJ\Demos\Logs\LogPyQt_Demo64.txt"
                        con = clienteSQL(archivoConfig, archivoLog)
                        rpta = con.EjecutarComandoCadena("uspUsuarioValidarLoginCsv","Login",login)
                        if(rpta is not None):
                            if(rpta!=""):
                                campos = rpta.split("|")
                                MessageBox.Show("Bienvenido Empresa: " + campos[0]) 
                                self.Rpta = rpta
                                self.close()
                            else:
                                self.Rpta = ""
                                MessageBox.Show("Login invalido. Intenta de Nuevo") 
                        else:
                            MessageBox.Show("Ocurrio un Error al Validar el Login") 
                    else:
                        MessageBox.Show("Codigo del Captcha es Incorrecto") 
                        self.txtCodigo.setFocus()
                else:
                   MessageBox.Show("Ingresa el Codigo") 
                   self.txtCodigo.setFocus()
            else:
               MessageBox.Show("Ingresa la Clave") 
               self.txtClave.setFocus()
        else:
           MessageBox.Show("Ingresa el Usuario") 
           self.txtUsuario.setFocus()
    
    def salir(self):
        self.close()