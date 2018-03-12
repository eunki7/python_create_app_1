import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from pyqt_basic_ui import Ui_MainWindow

#첫 번째 방법(변환 : pyuic5 -x uiFileName.ui -o uiFileName.py)
#form_class = uic.loadUiType("C:/Django/workspace/python-class1/section_final/example/pyqt_basic_ui.ui")[0]
class TestForm(QMainWindow, Ui_MainWindow): #MyWindow(QMainWindow, form_class)
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()
