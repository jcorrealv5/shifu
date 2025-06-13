import sys
from PyQt5 import QtWidgets, uic, QtPrintSupport
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPainter, QImage
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL
from modWindowsPyQt import MessageBox, TableView, CustomTableViewModel
from modPDF import Pdf

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo54.ui", self)
        #Obtener los controles de la GUI
        tblProducto = self.findChild(QtWidgets.QTableView, "tblProducto")
        self.lblTotalRegistros = self.findChild(QtWidgets.QLabel, "lblTotalRegistros")
        btnPreview = self.findChild(QtWidgets.QPushButton, "btnPreview")
        btnPrint = self.findChild(QtWidgets.QPushButton, "btnPrint")
        btnExportarPdf = self.findChild(QtWidgets.QPushButton, "btnExportarPdf")
        
        #Programar los eventos clicks de los Botones
        btnPreview.clicked.connect(self.previewReporte)
        btnPrint.clicked.connect(self.printReporte)
        btnExportarPdf.clicked.connect(self.exportarPdf)
        
        #Acceso a Datos
        archivoConfig=r"C:\Users\jhonf\Documents\Shifu\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Users\jhonf\Documents\Shifu\Demos\Logs\LogPyQtDemo05.txt"
        con = clienteSQL(archivoConfig, archivoLog)
        data = con.EjecutarComandoCadena("uspProductoListarCsv")
        if(data is not None):
            if(data!=""):
                self.listaProductos = data.split("¬")
                anchos = self.listaProductos[1].split("|")
                #Crear el Modelo desde el origen de datos
                modelo = CustomTableViewModel(self.listaProductos, esFloat=True)
                #Enlazar el Modelo al Control QTableView
                tblProducto.setModel(modelo)                
                #Configurar anchos
                TableView.ConfigurarAnchos(tblProducto, anchos)
                #Mostrar el Total de registros
                self.lblTotalRegistros.setText(str(modelo.rowCount()))
            else:
                MessageBox.Show("No existe registros en Productos")
        else:
            MessageBox.Show("Ocurrio un Error al listar los Productos")
    
    def previewReporte(self):
        dlgPreview = QtPrintSupport.QPrintPreviewDialog()
        size = self.pantalla.size()
        dlgPreview.setGeometry(0,0,size.width(),size.height())
        dlgPreview.paintRequested.connect(self.crearPaginasImprimir)
        dlgPreview.setWindowTitle("Reporte de Productos")
        dlgPreview.exec()
    
    def crearPaginasImprimir(self, printer):
        cabeceras = self.listaProductos[0].split("|")
        anchos = self.listaProductos[1].split("|")
        nRegistros = len(self.listaProductos)-3
        nCampos = len(cabeceras)
        lineasPagina = 18
        totalPaginas = int(nRegistros / lineasPagina)
        if(nRegistros % lineasPagina > 0):
            totalPaginas += 1
        print("Total de Paginas: ", totalPaginas)
        qp = QPainter()
        qp.begin(printer)
        cr=3
        margenIzquierdo = 100
        margenSuperior = 50
        espaciadoRegistro = 50
        espaciadoLineas = 30
        for i in range(totalPaginas):
            #Mostrar la imagen con el Logo
            destino = QRectF(margenIzquierdo+150,margenSuperior,margenIzquierdo+300,margenSuperior+70)
            imagen = QImage("C:/Users/jhonf/Documents/Shifu/PyQt/descarga.png")
            origen = QRectF(0,0,416,220)
            qp.drawImage(destino, imagen, origen)
            #Escribir las cabeceras de la tabla al inicio de cada pagina
            x=margenIzquierdo
            y=margenSuperior + 200
            for j in range(nCampos):
                qp.drawText(x,y,cabeceras[j])
                x += int(anchos[j])
            x=margenIzquierdo
            y+=espaciadoLineas
            qp.drawLine(x, y, 750, y)
            y+=espaciadoLineas
            for f in range(lineasPagina):
                if(cr<nRegistros+3):
                    campos = self.listaProductos[cr].split("|")
                    x=margenIzquierdo
                    for j in range(nCampos):
                        qp.drawText(x,y,campos[j])
                        x += int(anchos[j])
                    y+=espaciadoRegistro
                    cr+=1
                else:
                    break
            x=margenIzquierdo
            qp.drawLine(x, y, 750, y)
            y+=espaciadoLineas
            qp.drawText(600,y,"Pagina " + str(i+1) + " de " + str(totalPaginas))
            if(i<totalPaginas-1):
                printer.newPage()
        qp.end()
    
    def printReporte(self):
        dlgPrint = QtPrintSupport.QPrintDialog()
        if dlgPrint.exec()==QtWidgets.QDialog.Accepted:
            self.crearPaginasImprimir(dlgPrint.printer())
        
    def exportarPdf(self):
        lista = []
        for i in range(3, len(self.listaProductos)):
            campos = self.listaProductos[i].split("|")
            lista.append(campos)
        cabeceras = self.listaProductos[0].split("|")
        anchos = self.listaProductos[1].split("|")
        anchos = [int(ancho) for ancho in anchos]
        print("cabeceras", cabeceras)
        print("anchos", anchos)
        Pdf.ExportarDesdeLista(lista, cabeceras, anchos, "Reporte de Productos", "Productos.pdf")
        MessageBox.Show("Se exporto al archivo: Productos.pdf")
    
app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.pantalla = app.primaryScreen()
dlg.show()
sys.exit(app.exec_())