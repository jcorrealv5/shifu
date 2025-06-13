import sys, importlib
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QMdiArea, QMenuBar, QAction
from appDemo64_Login import Login
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL
from modWindowsPyQt import MessageBox

class Principal(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        print("Inicio")
        dlgLogin = Login()
        dlgLogin.exec_()
        print("Dialogo")
        if(dlgLogin.Rpta!=""):
            self.ventana = QMainWindow(self)
            self.ventana.setWindowState(Qt.WindowMaximized)
            self.ventana.setWindowTitle("Demo de Sistema Windows")        
            self.mdi = QMdiArea()
            self.ventana.setCentralWidget(self.mdi)
            bar = QMenuBar(self)
            archivoConfig = r"C:\Data\Python\2025_01_PythonMJ\Demos\00_Modulos\Config_BD_DACP_2025.txt"
            archivoLog = r"C:\Data\Python\2025_01_PythonMJ\Demos\Logs\LogPyQt_Demo64.txt"
            con = clienteSQL(archivoConfig, archivoLog)
            rpta = con.EjecutarComandoCadena("uspMenuListarCsv")
            print("rpta", rpta)
            if(rpta is not None):
                if(rpta!=""):
                    self.listaMenu = rpta.split("¬")
                    nLista = len(self.listaMenu)
                    for i in range(nLista):
                        campos = self.listaMenu[i].split("|")
                        if(campos[3]=="0"):
                            opcPadre = bar.addMenu(campos[1])
                            opcPadre.triggered[QAction].connect(self.seleccionarMenu)
                            self.crearSubMenu(opcPadre, campos[0])
                        else:
                            break
                else:
                    MessageBox.Show("No hay registros en el Menu")
            else:
                MessageBox.Show("Ocurrio un Error al traer el Menu")
            print("ventana")
            self.ventana.setMenuBar(bar)
            self.ventana.show()
            print("mostrar")
        else:
            self.close()
            sys.exit()
    
    def crearSubMenu(self, opcPadre, idPadre):
        nMenus = len(self.listaMenu)
        for i in range(nMenus):
            campos = self.listaMenu[i].split("|")
            if(campos[3]==idPadre):
                if(campos[2]==""):
                    opcHijo = opcPadre.addMenu(campos[1])
                else:
                    opcHijo = opcPadre.addAction(campos[1])
                    opcHijo.setData(campos[2])
                    print("Hijo: ", campos[2])
                self.crearSubMenu(opcHijo, campos[0])
    
    def seleccionarMenu(self, opcion):
        nombreModulo = "appDemo64_" + opcion.data()
        nombreClase = opcion.data()
        tabla = opcion.text()
        print("nombreModulo:", nombreModulo)
        print("nombreClase:", nombreClase)
        print("tabla:", tabla)
        self.ventana.tabla = tabla
        modulo = importlib.import_module(nombreModulo)
        tipo = getattr(modulo, nombreClase)
        frm = tipo(self.ventana)
        if frm!=None:
            self.mdi.addSubWindow(frm)
            frm.show()

app = QtWidgets.QApplication(sys.argv)
obj = Principal()
#obj.show()
obj.hide()
sys.exit( app.exec_() )