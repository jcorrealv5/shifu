import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog

class Dialogo(QDialog):
    def _init_(self):
        QDialog._init_(self)

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())