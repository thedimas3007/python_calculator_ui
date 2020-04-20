# импортируем библиотеки
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_Form
import sys


# создание окна
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

# логика приложения

val = 0.0000 # число с начала операции (нолики в конце для того чтобы считалось как число с плавающей точкой)
mode = "" # режим операции (1 -, 2 +, 3 *, 4 /)
dot = False

def b0():
  global mode 
  if ui.label.text() != "0" and len(ui.label.text()) < 15:
    ui.label.setText(ui.label.text() + "0")
  if mode == "0":
    ui.label.setText("0")
    mode = ""
def b1():
  global mode
  if ui.label.text() != "0" and len(ui.label.text()) < 15:
    ui.label.setText(ui.label.text() + "1")
  elif len(ui.label.text()) < 15:
    ui.label.setText("1")
  if mode == "0":
    ui.label.setText("1")
    mode = ""
def b2():
  global mode
  if ui.label.text() != "0" and len(ui.label.text()) < 15:
    ui.label.setText(ui.label.text() + "2")
  elif len(ui.label.text()) < 15:
    ui.label.setText("2")
  if mode == "0":
    ui.label.setText("2")
    mode = ""
def b3():
  global mode
  if ui.label.text() != "0" and len(ui.label.text()) < 15:
    ui.label.setText(ui.label.text() + "3")
  elif len(ui.label.text()) < 15:
    ui.label.setText("3")
  if mode == "0":
    ui.label.setText("3")
    mode = ""
def b4():
  global mode
  if ui.label.text() != "0" and len(ui.label.text()) < 15:
    ui.label.setText(ui.label.text() + "4")
  elif len(ui.label.text()) < 15:
    ui.label.setText("4")
  if mode == "0":
    ui.label.setText("4")
    mode = ""
def b5():
  global mode
  if ui.label.text() != "0" and len(ui.label.text()) < 15:
    ui.label.setText(ui.label.text() + "5")
  elif len(ui.label.text()) < 15:
    ui.label.setText("5")
  if mode == "0":
    ui.label.setText("5")
    mode = ""
def b6():
  global mode
  if ui.label.text() != "0" and len(ui.label.text()) < 15:
    ui.label.setText(ui.label.text() + "6")
  elif len(ui.label.text()) < 15:
    ui.label.setText("6")
  if mode == "0":
    ui.label.setText("6")
    mode = ""
def b7():
  global mode
  if ui.label.text() != "0" and len(ui.label.text()) < 15:
    ui.label.setText(ui.label.text() + "7")
  elif len(ui.label.text()) < 15:
    ui.label.setText("7")
  if mode == "0":
    ui.label.setText("7")
    mode = ""
def b8():
  global mode
  if ui.label.text() != "0" and len(ui.label.text()) < 15:
    ui.label.setText(ui.label.text() + "8")
  elif len(ui.label.text()) < 15:
    ui.label.setText("8")
  if mode == "0":
    ui.label.setText("8")
    mode = ""
def b9():
  global mode
  if ui.label.text() != "0" and len(ui.label.text()) < 15:
    ui.label.setText(ui.label.text() + "9")
  elif len(ui.label.text()) < 15:
    ui.label.setText("9")
  if mode == "0":
    ui.label.setText("9")
    mode = ""
def clear():
  ui.label.setText("0")
  global val, dot
  val = float(ui.label.text())
  dot = False
def subtract():
  global val, mode, dot
  val = float(ui.label.text())
  ui.label.setText("0")
  mode = "1"
  dot = False
def add():
  global val, mode, dot
  val = float(ui.label.text())
  ui.label.setText("0")
  mode = "2"
  dot = False
def multiply():
  global val, mode, dot
  val = float(ui.label.text())
  ui.label.setText("0")
  mode = "3"
  dot = False
def divide():
  global val, mode, dot
  val = float(ui.label.text())
  ui.label.setText("0")
  mode = "4"
  dot = False
def percent():
  ui.label.setText(format(float(ui.label.text()) / 100, '.5f'))
def negative():
    ui.label.setText(str(0 - float(ui.label.text())))
def equal():
  global val, mode, dot
  try:
    if   mode == "1":
      val -= float(ui.label.text())
    elif mode == "2":
      val += float(ui.label.text())
    elif mode == "3":
      val *= float(ui.label.text())
    elif mode == "4":
      val /= float(ui.label.text())
    mode = "0"
    if val == int(val):
      ui.label.setText(str(int(val)))
    else:
      ui.label.setText(format(val, '.5f'))
  except ZeroDivisionError:
    ui.label.setText("Ошибка")
  dot = False
def comma():
  global dot
  if not dot and len(ui.label.text()) < 15:
    ui.label.setText(ui.label.text() + ".")
    dot = True

ui.button_0.clicked.connect(b0)
ui.button_1.clicked.connect(b1)
ui.button_2.clicked.connect(b2)
ui.button_3.clicked.connect(b3)
ui.button_4.clicked.connect(b4)
ui.button_5.clicked.connect(b5)
ui.button_6.clicked.connect(b6)
ui.button_7.clicked.connect(b7)
ui.button_8.clicked.connect(b8)
ui.button_9.clicked.connect(b9)
ui.button_clear.clicked.connect(clear)
ui.button_div.clicked.connect(divide)
ui.button_multi.clicked.connect(multiply)
ui.button_add.clicked.connect(add)
ui.button_sub.clicked.connect(subtract)
ui.button_equal.clicked.connect(equal)
ui.button_per.clicked.connect(percent)
ui.button_neg.clicked.connect(negative)
ui.button_comma.clicked.connect(comma)

# цикл приложения
sys.exit(app.exec_())