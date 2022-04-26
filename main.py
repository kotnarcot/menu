from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import webbrowser
import sys


def runButton():
    webbrowser.open('https://lite-1x9065007.top/ru/registration?type=fast', new=2)


def mainApp():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle('qwertyuiop')
    window.setGeometry(500, 250, 500, 500)

    tekst = QtWidgets.QLabel(window)
    tekst.setText('asdfghjkl')
    tekst.move(200, 200)
    tekst.adjustSize()

    btn = QtWidgets.QPushButton(window)
    btn.move(250, 250)
    btn.setText('zxcvbnm')
    btn.setFixedWidth(300)
    btn.clicked.connect(runButton)

    window.show()
    sys.exit(app.exec_())


mainApp()