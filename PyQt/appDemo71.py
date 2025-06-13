import sys
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL
from modPDF import Pdf
from modWindowsPyQt import MessageBox
from PyQt5.QtCore import QThread

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo71.ui", self)
        #Obtener los Conteoles de la GUI
        self.btnConsultarCubso = self.findChild(QtWidgets.QPushButton, "btnConsultarCubso")
        self.btnExportarPDF = self.findChild(QtWidgets.QPushButton, "btnExportarPDF")
        self.pbrConsulta = self.findChild(QtWidgets.QProgressBar, "pbrConsulta")
        self.tblCubso = self.findChild(QtWidgets.QTableWidget, "tblCubso")
        self.btnPrimero = self.findChild(QtWidgets.QPushButton, "btnPrimero")
        self.btnAnterior = self.findChild(QtWidgets.QPushButton, "btnAnterior")
        self.cboPaginaActual = self.findChild(QtWidgets.QComboBox, "cboPaginaActual")
        self.txtTotalPaginas = self.findChild(QtWidgets.QLineEdit, "txtTotalPaginas")
        self.btnSiguiente = self.findChild(QtWidgets.QPushButton, "btnSiguiente")
        self.btnUltimo = self.findChild(QtWidgets.QPushButton, "btnUltimo")
        self.lblMensaje = self.findChild(QtWidgets.QLabel, "lblMensaje")
        #Programar los eventos clicks de los Botones
        self.btnConsultarCubso.clicked.connect(self.consultarCubso)
        self.btnExportarPDF.clicked.connect(self.exportarPDF)
        self.btnPrimero.clicked.connect(lambda: self.paginar(-1))
        self.btnAnterior.clicked.connect(lambda: self.paginar(-2))
        self.btnSiguiente.clicked.connect(lambda: self.paginar(-3))
        self.btnUltimo.clicked.connect(lambda: self.paginar(-4))        
        #Configurar el Control QTableWidget para mostrar los registros
        self.paginasBloque = 10
        self.tblCubso.setColumnCount(4)
        self.tblCubso.setRowCount(self.paginasBloque)
        self.cabeceras = ["Id", "Codigo", "Descripcion", "Precio"]
        self.tblCubso.setHorizontalHeaderLabels(self.cabeceras)
        self.anchos = [50, 200, 550, 100]
        for j in range(4):
            self.tblCubso.setColumnWidth(j, self.anchos[j])
            
    def consultarCubso(self):
        self.listaCubso = []
        archivoConfig=r"C:\Users\jhonf\Documents\Shifu\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Users\jhonf\Documents\Shifu\Demos\Logs\LogPyQtDemo05.txt"
        self.con = clienteSQL(archivoConfig, archivoLog)
        data = self.con.EjecutarComandoCadena("uspCubsoContar")
        if(data is not None):
            if(data!=""):
                self.indicePagina = 0
                
                self.totalRegistros = int(data)
                self.viajesBloque = 10000
                self.viajesTotal = int(self.totalRegistros / self.viajesBloque)
                if(self.totalRegistros % self.viajesBloque > 0):
                    self.viajesTotal += 1
                self.viajesContador = 0
                
                self.pbrConsulta.setMaximum(self.viajesTotal)
                self.lblMensaje.setText("Cargando 0 de " + str(self.totalRegistros))           
                
                self.totalPaginas = int(self.totalRegistros / self.paginasBloque)
                if(self.totalRegistros % self.paginasBloque > 0):
                    self.totalPaginas += 1                    
                self.txtTotalPaginas.setText(str(self.totalPaginas))
                
                #Cargar el Combo con los Numeros de Paginas
                for i in range(self.totalPaginas):
                    self.cboPaginaActual.addItem(str(i + 1))
                #Programar el evento currentIndexChanged del ComboBox
                self.cboPaginaActual.currentIndexChanged.connect(self.paginar)
                self.habilitarBotones(False)
                self.obtenerBloqueRegistrosBD()
    
    def obtenerBloqueRegistrosBD(self):
        self.hilo = WorkerBD(self)
        self.hilo.finalizado.connect(self.mostrarBloqueBD)
        self.hilo.start()
    
    def mostrarBloqueBD(self, data):
        if(data is not None):
            if(data!=""):
                lista = data.split(";")
                nRegistros = len(lista)
                for i in range(nRegistros):
                    self.listaCubso.append(lista[i].split("|"))
                self.viajesContador += 1
                self.pbrConsulta.setValue(self.viajesContador)
                self.lblMensaje.setText("Cargando " + str(len(self.listaCubso)) + " de " + str(self.totalRegistros))
                if(self.viajesContador == 1):
                    self.mostrarPagina()
                if(self.viajesContador < self.viajesTotal):
                    self.obtenerBloqueRegistrosBD()
                else:
                    self.habilitarBotones(True)
    
    def mostrarPagina(self):
        inicio = self.indicePagina * self.paginasBloque
        fin = inicio + self.paginasBloque
        fila = 0
        for i in range(inicio, fin):
            if(i<self.totalRegistros-1):
                for j in range(4):
                    item = QTableWidgetItem(self.listaCubso[i][j])
                    self.tblCubso.setItem(fila, j, item)                
            else:
                for j in range(4):
                    item = QTableWidgetItem("")
                    self.tblCubso.setItem(fila, j, item)
            fila += 1
        self.cboPaginaActual.setCurrentIndex(self.indicePagina)
    
    def habilitarBotones(self, habilitado):
        self.btnConsultarCubso.setEnabled(habilitado)
        self.btnExportarPDF.setEnabled(habilitado)
        self.btnPrimero.setEnabled(habilitado)
        self.btnAnterior.setEnabled(habilitado)
        self.btnSiguiente.setEnabled(habilitado)
        self.btnUltimo.setEnabled(habilitado)
        self.cboPaginaActual.setEnabled(habilitado)
    
    def exportarPDF(self):
        self.habilitarBotones(False)
        self.hilo = WorkerExportar(self)
        self.hilo.finalizado.connect(self.mostrarRptaExportar)
        self.hilo.start()
    
    def mostrarRptaExportar(self, rpta):
        self.habilitarBotones(True)
        MessageBox.Show(rpta)
    
    def paginar(self, indice):
        if(indice==-1):
            self.indicePagina = 0
        elif(indice==-2):
            if(self.indicePagina>0):
                self.indicePagina -= 1
        elif(indice==-3):
            if(self.indicePagina<self.totalPaginas-1):
                self.indicePagina += 1
        elif(indice==-4):
            self.indicePagina = self.totalPaginas-1
        else:
            self.indicePagina = indice
        self.mostrarPagina()

class WorkerBD(QThread):
    finalizado = QtCore.pyqtSignal(str)
    
    def __init__(self, parent):
        super(WorkerBD, self).__init__(parent) 
        self.viajesContador = parent.viajesContador
        self.viajesBloque = parent.viajesBloque
        self.con = parent.con
    
    def run(self):
        params = str(self.viajesContador+1) + "|" + str(self.viajesBloque)
        data = self.con.EjecutarComandoCadena("uspCubsoPaginarCsvPy", "data", params)
        self.finalizado.emit(data)
        
class WorkerExportar(QThread):
    finalizado = QtCore.pyqtSignal(str)
    
    def __init__(self, parent):
        super(WorkerExportar, self).__init__(parent) 
        self.listaCubso = parent.listaCubso
        self.cabeceras = parent.cabeceras
        self.anchos = parent.anchos
        print("self.cabeceras", self.cabeceras)
        print("self.anchos", self.anchos)
    
    def run(self):
        Pdf.ExportarDesdeLista(self.listaCubso, self.cabeceras, self.anchos, "Reporte de Cubso", "Cubso.pdf")
        self.finalizado.emit("Se creo el archivo Cubso.pdf")

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())