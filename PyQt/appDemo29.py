import sys, os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QTreeWidgetItem, QListWidgetItem
from PyQt5.QtGui import QIcon

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo29.ui", self)
        twDirectorio = self.findChild(QtWidgets.QTreeWidget, "twDirectorio")
        self.lwArchivo = self.findChild(QtWidgets.QListWidget, "lwArchivo")
        twDirectorio.header().resizeSection(0, 500)
        twDirectorio.currentItemChanged.connect(self.mostrarArchivos)
        self.lwArchivo.doubleClicked.connect(self.abrirArchivo)
        
        rutaInicio = "C:/Data/Python/2025_01_PythonMJ"
        listaFS = os.walk(rutaInicio)
        c=1
        rutas = []
        nodos = []
        for raiz, directorios, archivos in listaFS:
            rutas.append(raiz)            
            carpeta = os.path.basename(raiz)
            if(c==1):
                nodoPadre = QTreeWidgetItem()
                nodoPadre.setText(0, carpeta)
                nodoPadre.setIcon(0,QIcon("C:/Data/Python/2025_01_PythonMJ/Imagenes/Iconos/Folder.jpg"))
                nodos.append(nodoPadre)
                twDirectorio.addTopLevelItem(nodoPadre)
                self.listarArchivos(raiz)
            else:
                ruta = os.path.dirname(raiz)
                nodoHijo = QTreeWidgetItem()
                nodoHijo.setText(0, carpeta)
                nodoHijo.setIcon(0,QIcon("C:/Data/Python/2025_01_PythonMJ/Imagenes/Iconos/Folder.jpg"))
                nodos.append(nodoHijo)
                pos = rutas.index(ruta)
                if(pos>-1):
                    nodos[pos].addChild(nodoHijo)
            c=c+1
    
    def mostrarArchivos(self, nodo):
        ruta = []
        directorio = nodo.text(0)
        ruta.append(directorio)
        while True:
            padre = nodo.parent()
            if padre is not None:
                directorio = padre.text(0)
                ruta.append(directorio)
                nodo = padre
            else:
                break
        if(len(ruta)>0):
            ruta.reverse()
            directorio = os.path.join("C:/Data/Python/", "\\".join(ruta))
            self.listarArchivos(directorio)

    def listarArchivos(self, directorio):
        self.lwArchivo.clear()
        self.DirectorioActual = directorio
        listaArchivos = os.listdir(directorio)
        for item in listaArchivos:
            archivo = os.path.join(directorio, item)
            if(os.path.isfile(archivo)):
                ruta = "C:/Data/Python/2025_01_PythonMJ/Imagenes/Iconos/"
                tipo = archivo.split(".")[-1]
                archivoIcono = ruta + tipo + ".jpg"
                if(not os.path.isfile(archivoIcono)):
                    archivoIcono = ruta + "txt.jpg"
                icono = QIcon(archivoIcono)
                fila = QListWidgetItem(icono, item)
                self.lwArchivo.addItem(fila)
    
    def abrirArchivo(self):
        archivo = os.path.join(self.DirectorioActual, self.lwArchivo.currentItem().text())
        os.startfile(archivo)

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())