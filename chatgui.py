# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 285)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtRecvdMessage = QtWidgets.QTextEdit(self.centralwidget)
        self.txtRecvdMessage.setGeometry(QtCore.QRect(10, 10, 301, 161))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtRecvdMessage.setFont(font)
        self.txtRecvdMessage.setTabChangesFocus(True)
        self.txtRecvdMessage.setObjectName("txtRecvdMessage")
        self.pbSendMessage = QtWidgets.QPushButton(self.centralwidget)
        self.pbSendMessage.setGeometry(QtCore.QRect(10, 220, 111, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbSendMessage.setFont(font)
        self.pbSendMessage.setAutoDefault(True)
        self.pbSendMessage.setDefault(False)
        self.pbSendMessage.setObjectName("pbSendMessage")
        self.pbExit = QtWidgets.QPushButton(self.centralwidget)
        self.pbExit.setGeometry(QtCore.QRect(260, 220, 51, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbExit.setFont(font)
        self.pbExit.setAutoDefault(True)
        self.pbExit.setDefault(False)
        self.pbExit.setObjectName("pbExit")
        self.txtMessageOut = QtWidgets.QTextEdit(self.centralwidget)
        self.txtMessageOut.setGeometry(QtCore.QRect(10, 177, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtMessageOut.setFont(font)
        self.txtMessageOut.setTabChangesFocus(True)
        self.txtMessageOut.setObjectName("txtMessageOut")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtRecvdMessage, self.txtMessageOut)
        MainWindow.setTabOrder(self.txtMessageOut, self.pbSendMessage)
        MainWindow.setTabOrder(self.pbSendMessage, self.pbExit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pbSendMessage.setText(_translate("MainWindow", "Send Message"))
        self.pbExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
