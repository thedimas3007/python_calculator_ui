# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(389, 544)
        Form.setStyleSheet("QWidget {\n"
"  background-color: black\n"
"}")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 60, 361, 482))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.button_add = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_add.setFont(font)
        self.button_add.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"  background-color: #FFA500;\n"
"  border: none;\n"
"  border-radius: 37px;\n"
"  height: 75px;\n"
"  width: 75px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #DD8000;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #BB5E00;\n"
"}")
        self.button_add.setObjectName("button_add")
        self.gridLayout.addWidget(self.button_add, 3, 3, 1, 1)
        self.button_neg = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_neg.setFont(font)
        self.button_neg.setStyleSheet("QPushButton {\n"
"  background-color: #a9a9a9;\n"
"  border: none;\n"
"  border-radius: 37px;\n"
"  height: 75px;\n"
"  width: 75px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #696969;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #555555;\n"
"}")
        self.button_neg.setObjectName("button_neg")
        self.gridLayout.addWidget(self.button_neg, 0, 1, 1, 1)
        self.button_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_1.setFont(font)
        self.button_1.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"  background-color: #696969;\n"
"  border: none;\n"
"  border-radius: 37px;\n"
"  height: 75px;\n"
"  width: 75px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #555555;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #454545;\n"
"}")
        self.button_1.setObjectName("button_1")
        self.gridLayout.addWidget(self.button_1, 3, 0, 1, 1)
        self.button_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_8.setFont(font)
        self.button_8.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"  background-color: #696969;\n"
"  border: none;\n"
"  border-radius: 37px;\n"
"  height: 75px;\n"
"  width: 75px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #555555;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #454545;\n"
"}")
        self.button_8.setObjectName("button_8")
        self.gridLayout.addWidget(self.button_8, 1, 1, 1, 1)
        self.button_sub = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_sub.setFont(font)
        self.button_sub.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"  background-color: #FFA500;\n"
"  border: none;\n"
"  border-radius: 37px;\n"
"  height: 75px;\n"
"  width: 75px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #DD8000;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #BB5E00;\n"
"}")
        self.button_sub.setObjectName("button_sub")
        self.gridLayout.addWidget(self.button_sub, 2, 3, 1, 1)
        self.button_per = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_per.setFont(font)
        self.button_per.setStyleSheet("QPushButton {\n"
"  background-color: #a9a9a9;\n"
"  border: none;\n"
"  border-radius: 37px;\n"
"  height: 75px;\n"
"  width: 75px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #696969;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #555555;\n"
"}")
        self.button_per.setObjectName("button_per")
        self.gridLayout.addWidget(self.button_per, 0, 2, 1, 1)
        self.button_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_6.setFont(font)
        self.button_6.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"  background-color: #696969;\n"
"  border: none;\n"
"  border-radius: 37px;\n"
"  height: 75px;\n"
"  width: 75px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #555555;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #454545;\n"
"}")
        self.button_6.setObjectName("button_6")
        self.gridLayout.addWidget(self.button_6, 2, 2, 1, 1)
        self.button_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_9.setFont(font)
        self.button_9.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"  background-color: #696969;\n"
"  border: none;\n"
"  border-radius: 37px;\n"
"  height: 75px;\n"
"  width: 75px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #555555;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #454545;\n"
"}")
        self.button_9.setObjectName("button_9")
        self.gridLayout.addWidget(self.button_9, 1, 2, 1, 1)
        self.button_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_3.setFont(font)
        self.button_3.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"  background-color: #696969;\n"
"  border: none;\n"
"  border-radius: 37px;\n"
"  height: 75px;\n"
"  width: 75px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #555555;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #454545;\n"
"}")
        self.button_3.setObjectName("button_3")
        self.gridLayout.addWidget(self.button_3, 3, 2, 1, 1)
        self.button_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_4.setFont(font)
        self.button_4.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"  background-color: #696969;\n"
"  border: none;\n"
"  border-radius: 37px;\n"
"  height: 75px;\n"
"  width: 75px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #555555;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #454545;\n"
"}")
        self.button_4.setObjectName("button_4")
        self.gridLayout.addWidget(self.button_4, 2, 0, 1, 1)
        self.button_comma = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_comma.setFont(font)
        self.button_comma.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"  background-color: #696969;\n"
"  border: none;\n"
"  border-radius: 37px;\n"
"  height: 75px;\n"
"  width: 75px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #555555;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #454545;\n"
"}")
        self.button_comma.setObjectName("button_comma")
        self.gridLayout.addWidget(self.button_comma, 4, 2, 1, 1)
        self.button_multi = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_multi.setFont(font)
        self.button_multi.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"  background-color: #FFA500;\n"
"  border: none;\n"
"  border-radius: 37px;\n"
"  height: 75px;\n"
"  width: 75px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #DD8000;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #BB5E00;\n"
"}")
        self.button_multi.setObjectName("button_multi")
        self.gridLayout.addWidget(self.button_multi, 1, 3, 1, 1)
        self.button_clear = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_clear.setFont(font)
        self.button_clear.setStyleSheet("QPushButton {\n"
"  background-color: #a9a9a9;\n"
"  border: none;\n"
"  border-radius: 37px;\n"
"  height: 75px;\n"
"  width: 75px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #696969;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #555555;\n"
"}")
        self.button_clear.setObjectName("button_clear")
        self.gridLayout.addWidget(self.button_clear, 0, 0, 1, 1)
        self.button_equal = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_equal.setFont(font)
        self.button_equal.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"  background-color: #FFA500;\n"
"  border: none;\n"
"  border-radius: 37px;\n"
"  height: 75px;\n"
"  width: 75px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #DD8000;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #BB5E00;\n"
"}")
        self.button_equal.setObjectName("button_equal")
        self.gridLayout.addWidget(self.button_equal, 4, 3, 1, 1)
        self.button_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_5.setFont(font)
        self.button_5.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"  background-color: #696969;\n"
"  border: none;\n"
"  border-radius: 37px;\n"
"  height: 75px;\n"
"  width: 75px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #555555;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #454545;\n"
"}")
        self.button_5.setObjectName("button_5")
        self.gridLayout.addWidget(self.button_5, 2, 1, 1, 1)
        self.button_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_7.setFont(font)
        self.button_7.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"  background-color: #696969;\n"
"  border: none;\n"
"  border-radius: 37px;\n"
"  height: 75px;\n"
"  width: 75px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #555555;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #454545;\n"
"}")
        self.button_7.setObjectName("button_7")
        self.gridLayout.addWidget(self.button_7, 1, 0, 1, 1)
        self.button_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_0.setFont(font)
        self.button_0.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"  background-color: #696969;\n"
"  border: none;\n"
"  border-radius: 37px;\n"
"  height: 75px;\n"
"  width: 75px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #555555;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #454545;\n"
"}")
        self.button_0.setObjectName("button_0")
        self.gridLayout.addWidget(self.button_0, 4, 1, 1, 1)
        self.button_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_2.setFont(font)
        self.button_2.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"  background-color: #696969;\n"
"  border: none;\n"
"  border-radius: 37px;\n"
"  height: 75px;\n"
"  width: 75px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #555555;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #454545;\n"
"}")
        self.button_2.setObjectName("button_2")
        self.gridLayout.addWidget(self.button_2, 3, 1, 1, 1)
        self.button_div = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_div.setFont(font)
        self.button_div.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"  background-color: #FFA500;\n"
"  border: none;\n"
"  border-radius: 37px;\n"
"  height: 75px;\n"
"  width: 75px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #DD8000;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #BB5E00;\n"
"}")
        self.button_div.setObjectName("button_div")
        self.gridLayout.addWidget(self.button_div, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"  color: white;\n"
"  text-align: right;\n"
"  font-size: 40px;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculator"))
        self.button_add.setText(_translate("Form", "+"))
        self.button_neg.setText(_translate("Form", "+/-"))
        self.button_1.setText(_translate("Form", "1"))
        self.button_8.setText(_translate("Form", "8"))
        self.button_sub.setText(_translate("Form", "-"))
        self.button_per.setText(_translate("Form", "%"))
        self.button_6.setText(_translate("Form", "6"))
        self.button_9.setText(_translate("Form", "9"))
        self.button_3.setText(_translate("Form", "3"))
        self.button_4.setText(_translate("Form", "4"))
        self.button_comma.setText(_translate("Form", ","))
        self.button_multi.setText(_translate("Form", "×"))
        self.button_clear.setText(_translate("Form", "AC"))
        self.button_equal.setText(_translate("Form", "="))
        self.button_5.setText(_translate("Form", "5"))
        self.button_7.setText(_translate("Form", "7"))
        self.button_0.setText(_translate("Form", "0"))
        self.button_2.setText(_translate("Form", "2"))
        self.button_div.setText(_translate("Form", "÷"))
        self.label.setText(_translate("Form", "0"))