from PyQt5.QtWidgets import QApplication
from sys import exit
from gui.forms import MainWindow


if __name__ == '__main__':

    app = QApplication([])
    win = MainWindow()
    win.open()
    exit(app.exec())
