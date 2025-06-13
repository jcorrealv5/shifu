import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QMessageBox
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL
from modWindowsPyQt import CustomTableViewModel

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo42.ui", self)
        tblProducto = self.findChild(QtWidgets.QTableView, "tblProducto")
        lblTotalRegistros = self.findChild(QtWidgets.QLabel, "lblTotalRegistros")
        #Acceso a Datos usando la clase clienteSQL
        archivoConfig=r"C:\Users\jhonf\Documents\Shifu\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Users\jhonf\Documents\Shifu\Demos\Logs\LogPyQtDemo05.txt"
        con = clienteSQL(archivoConfig, archivoLog)
        data = con.EjecutarComandoCadena("uspProductoListarCsv")
        dlg = QMessageBox()
        if(data is not None):
            if(data!=""):
                listaProductos = data.split("¬")
                #Crear el Modelo usando una Clase Personalizada
                formatoFilas = {"ColorTextoPar": "red", "ColorFondoPar": "pink",
                                "ColorTextoImpar": "red", "ColorFondoImpar": "orange"}
                modelo = CustomTableViewModel(listaProductos, formatoFilas=formatoFilas)
                #Enlazar el Modelo a Control Vista: QTableView
                tblProducto.setModel(modelo)
                #Configurar los anchos del control
                anchos = listaProductos[1].split("|")
                nCampos = len(anchos)
                for j in range(nCampos):
                    tblProducto.setColumnWidth(j, int(anchos[j]))
                #Mostrar el Numero de Registros desde el Modelo
                lblTotalRegistros.setText(str(modelo.rowCount()))
            else:
                dlg.setText("No existe registros de Productos")
                dlg.exec()
        else:
            dlg.setText("Ocurrio un Error al Listar los Productos")
            dlg.exec()

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())