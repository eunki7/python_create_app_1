# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        fileRunPath = os.path.dirname(__file__)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(742, 667)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(fileRunPath + "/resource/ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 181, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(fileRunPath + "/resource/logo.png"))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 251, 311))
        self.groupBox.setObjectName("groupBox")
        self.swordEdit = QtWidgets.QLineEdit(self.groupBox)
        self.swordEdit.setGeometry(QtCore.QRect(10, 20, 161, 31))
        self.swordEdit.setPlaceholderText("입력 후 Enter 또는 시작..")
        self.swordEdit.setObjectName("swordEdit")
        self.startSearchWordButton = QtWidgets.QPushButton(self.groupBox)
        self.startSearchWordButton.setGeometry(QtCore.QRect(180, 20, 61, 31))
        self.startSearchWordButton.setAutoDefault(False)
        self.startSearchWordButton.setObjectName("startSearchWordButton")
        self.listWidget_3 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_3.setGeometry(QtCore.QRect(10, 60, 231, 201))
        self.listWidget_3.setStyleSheet("background-color: rgb(255, 254, 247);")
        self.listWidget_3.setObjectName("listWidget_3")
        self.initButton = QtWidgets.QPushButton(self.groupBox)
        self.initButton.setGeometry(QtCore.QRect(10, 270, 71, 31))
        self.initButton.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.initButton.setObjectName("initButton")
        self.saveResultWord = QtWidgets.QPushButton(self.groupBox)
        self.saveResultWord.setGeometry(QtCore.QRect(90, 270, 71, 31))
        self.saveResultWord.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.saveResultWord.setObjectName("saveResultWord")
        self.exitButton = QtWidgets.QPushButton(self.groupBox)
        self.exitButton.setGeometry(QtCore.QRect(170, 270, 71, 31))
        self.exitButton.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.exitButton.setObjectName("exitButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(270, 70, 461, 311))
        self.groupBox_2.setObjectName("groupBox_2")
        self.webView = QtWebEngineWidgets.QWebEngineView(self.groupBox_2)
        self.webView.setGeometry(QtCore.QRect(10, 20, 441, 281))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 390, 351, 271))
        self.groupBox_3.setObjectName("groupBox_3")
        self.listWidget_1 = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget_1.setGeometry(QtCore.QRect(10, 20, 331, 241))
        self.listWidget_1.setStyleSheet("background-color: rgb(239, 255, 255);")
        self.listWidget_1.setObjectName("listWidget_1")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(380, 390, 351, 271))
        self.groupBox_4.setObjectName("groupBox_4")
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox_4)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 20, 331, 241))
        self.listWidget_2.setStyleSheet("background-color: rgb(234, 225, 255);")
        self.listWidget_2.setObjectName("listWidget_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 10, 551, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(fileRunPath + "/resource/title.png"))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "검색어 설정"))
        self.startSearchWordButton.setText(_translate("MainWindow", "시작"))
        self.initButton.setText(_translate("MainWindow", "초기화"))
        self.saveResultWord.setText(_translate("MainWindow", "저장"))
        self.exitButton.setText(_translate("MainWindow", "종료"))
        self.groupBox_2.setTitle(_translate("MainWindow", "미리보기"))
        self.groupBox_3.setTitle(_translate("MainWindow", "1차 연관검색어( 더블 클릭 ▶ 2차 연관검색어 )"))
        self.groupBox_4.setTitle(_translate("MainWindow", "2차 연관검색어"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
