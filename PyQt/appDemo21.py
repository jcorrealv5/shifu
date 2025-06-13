import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QMessageBox
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo21.ui",self)
        self.cboDepartamento = self.findChild(QtWidgets.QComboBox, "cboDepartamento")
        self.cboProvincia = self.findChild(QtWidgets.QComboBox, "cboProvincia")
        self.cboDistrito = self.findChild(QtWidgets.QComboBox, "cboDistrito")
        btnVerUbigeo = self.findChild(QtWidgets.QPushButton, "btnVerUbigeo")
        #Programar Controles de la GUI
        btnVerUbigeo.clicked.connect(self.mostrarUbigeo)
        self.cboDepartamento.currentIndexChanged.connect(self.listarProvincias)
        self.cboProvincia.currentIndexChanged.connect(self.listarDistritos)
        
        #Conectar a Base de Datos y traer los Nombres de los Alumnos
        archivoConfig=r"C:\Users\jhonf\Documents\Shifu\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Users\jhonf\Documents\Shifu\Demos\Logs\LogPyQtDemo05.txt"
        conexion = clienteSQL(archivoConfig,archivoLog)
        data = conexion.EjecutarComandoCadena("uspUbigeoListarCsv")
        msg = QMessageBox()
        if(data is not None):
            if(data!=""):
                self.ListaUbigeo = data.split("¬")
                self.NroRegistros = len(self.ListaUbigeo)
                self.listarDepartamentos()
        else:
            msg.setText("Ocurrio un Error al obtener el Ubigeo")
            msg.exec()
    
    def listarDepartamentos(self):
        listaNomDptos = []
        self.ListaCodDptos = []
        for i in range(self.NroRegistros):
            idDpto = self.ListaUbigeo[i][0:2]
            idProv = self.ListaUbigeo[i][2:4]
            idDist = self.ListaUbigeo[i][4:6]            
            if(idDpto!='00' and idProv=='00' and idDist=='00'):
                self.ListaCodDptos.append(idDpto)
                listaNomDptos.append(self.ListaUbigeo[i][6:])
        self.cboDepartamento.addItems(listaNomDptos)

    def listarProvincias(self):
        self.cboProvincia.clear()
        indice = self.cboDepartamento.currentIndex()
        idDptoSel = self.ListaCodDptos[indice]
        listaNomProvs = []
        self.ListaCodProvs = []
        for i in range(self.NroRegistros):
            idDpto = self.ListaUbigeo[i][0:2]
            idProv = self.ListaUbigeo[i][2:4]
            idDist = self.ListaUbigeo[i][4:6]            
            if(idDpto==idDptoSel and idProv!='00' and idDist=='00'):
                self.ListaCodProvs.append(idProv)
                listaNomProvs.append(self.ListaUbigeo[i][6:])
        self.cboProvincia.addItems(listaNomProvs)
        
    def listarDistritos(self):
        self.cboDistrito.clear()
        indiceDpto = self.cboDepartamento.currentIndex()        
        idDptoSel = self.ListaCodDptos[indiceDpto]
        indiceProv = self.cboProvincia.currentIndex()        
        idProvSel = self.ListaCodProvs[indiceProv]
        listaNomDists = []
        self.ListaCodDists = []
        for i in range(self.NroRegistros):
            idDpto = self.ListaUbigeo[i][0:2]
            idProv = self.ListaUbigeo[i][2:4]
            idDist = self.ListaUbigeo[i][4:6]            
            if(idDpto==idDptoSel and idProv==idProvSel and idDist!='00'):
                self.ListaCodDists.append(idDist)
                listaNomDists.append(self.ListaUbigeo[i][6:])
        self.cboDistrito.addItems(listaNomDists)

    def mostrarUbigeo(self):
        indiceDpto = self.cboDepartamento.currentIndex()        
        idDptoSel = self.ListaCodDptos[indiceDpto]
        indiceProv = self.cboProvincia.currentIndex()        
        idProvSel = self.ListaCodProvs[indiceProv]
        indiceDist = self.cboDistrito.currentIndex()        
        idDistSel = self.ListaCodDists[indiceDist]
        rpta = "Seleccionaste el Ubigeo: " + idDptoSel + idProvSel + idDistSel  
        msg = QMessageBox()
        msg.setText(rpta)
        msg.exec()

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())