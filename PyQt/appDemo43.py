import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QMessageBox, QHeaderView
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL
from modWindowsPyQt import CustomTableViewModel

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo43.ui", self)
        tblAlumno = self.findChild(QtWidgets.QTableView, "tblAlumno")
        lblTotalRegistros = self.findChild(QtWidgets.QLabel, "lblTotalRegistros")
        #Acceso a Datos usando la clase clienteSQL
        archivoConfig=r"C:\Users\jhonf\Documents\Shifu\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Users\jhonf\Documents\Shifu\Demos\Logs\LogPyQtDemo05.txt"
        con = clienteSQL(archivoConfig, archivoLog)
        data = con.EjecutarComandoCadena("uspAlumnoListarFotoCabCsv")
        dlg = QMessageBox()
        if(data is not None):
            if(data!=""):
                listaAlumnos = data.split("¬")
                formatoFilas = {"ColorTextoPar": "white", "ColorFondoPar": "red",
                                "ColorTextoImpar": "green", "ColorFondoImpar": "yellow"}
                modelo = CustomTableViewModel(listaAlumnos, formatoFilas=formatoFilas)
                #Enlazar el Modelo a Control Vista: QTableView
                tblAlumno.setModel(modelo)
                #Configurar los anchos del control
                anchos = listaAlumnos[1].split("|")
                nCampos = len(anchos)
                for j in range(nCampos):
                    tblAlumno.setColumnWidth(j, int(anchos[j]))
                #Mostrar el Numero de Registros desde el Modelo
                lblTotalRegistros.setText(str(modelo.rowCount()))
                #Ajustar los tamanios de las columnas
                tblAlumno.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            else:
                dlg.setText("No existe registros de Alumnos")
                dlg.exec()
        else:
            dlg.setText("Ocurrio un Error al Listar los Alumnos")
            dlg.exec()

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())