# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI3.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(585, 584)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.output_txt = QtWidgets.QLabel(self.splitter)
        self.output_txt.setMinimumSize(QtCore.QSize(500, 0))
        self.output_txt.setFrameShape(QtWidgets.QFrame.Box)
        self.output_txt.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output_txt.setLineWidth(1)
        self.output_txt.setMidLineWidth(1)
        self.output_txt.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.output_txt.setObjectName("output_txt")
        self.frame = QtWidgets.QFrame(self.splitter)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.input_txt = QtWidgets.QLineEdit(self.frame)
        self.input_txt.setMaximumSize(QtCore.QSize(16777215, 50))
        self.input_txt.setObjectName("input_txt")
        self.horizontalLayout.addWidget(self.input_txt)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    padding: 5px;\n"
"    margin: 5px;\n"
"    border-radius: 5px;\n"
"    background: rgb(0, 85, 255);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(0, 85, 255, 220);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: rgb(0, 85, 255, 200);\n"
"}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 585, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.output_txt.setText(_translate("MainWindow", ""))
        self.input_txt.setPlaceholderText(_translate("MainWindow", "Input your prompt!"))
        self.pushButton.setText(_translate("MainWindow", "Send"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
