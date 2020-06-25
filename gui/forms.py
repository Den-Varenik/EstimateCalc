from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow
from lib.classes import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self._form = loadUi('MainWindow.ui')
        self._form.pushButton.clicked.connect(self.calc_slot)
        self._form.pushButton_2.clicked.connect(self.clear_slot)
        self._form.pushButton_3.clicked.connect(self.reset_slot)

    def open(self) -> None:
        self._form.show()

    def calc_slot(self) -> None:
        params = [(self._form.textEdit.toPlainText().strip()).split('\n'),
                  (self._form.textEdit_2.toPlainText().strip()).split('\n'),
                  (self._form.textEdit_3.toPlainText().strip()).split('\n'),
                  (self._form.textEdit_4.toPlainText().strip()).split('\n')]
        params = list(map(lambda param: list(map(self.__calc_slot, param)), params))
        to_figure = params.copy()
        for i in range(len(to_figure)):
            if i != 0:
                to_figure[i] = list(zip(*[iter(to_figure[i])] * i))
            else:
                to_figure[i] = list(zip(*[iter(to_figure[i])] * 1))
        for i in to_figure:
            i = self.__bool_figure(i)
        to_figure = [[self.__create_figures(values, to_figure.index(param), param.index(values)) for values in param] \
                     for param in to_figure]
        text = ''
        for figure in to_figure:
            for item in figure:
                if not item:
                    text += 'Ошибка\n'
                else:
                    text += f'{item.shape_id}. S = {item.calc_S()}\n'
            text += '\n'
        self._form.textEdit_5.setText('')
        self._form.textEdit_5.setText(text)

    @staticmethod
    def __calc_slot(value):
        try:
            value = float(value)
        except ValueError:
            value = False
        return value

    @staticmethod
    def __bool_figure(arr):
        for i in range(len(arr)):
            if False in arr[i]:
                arr[i] = False
        return arr

    @staticmethod
    def __create_figures(values, index, shape_id):
        print(index)
        if type(values) is tuple:
            if len(values) == 1 and index == 0:
                return Circle(shape_id + 1, values[0])
            elif len(values) == 1 and index == 1:
                return Square(shape_id + 1, values[0])
            elif len(values) == 2:
                return Rectangle(shape_id + 1, values[0], values[1])
            elif len(values) == 3:
                return Triangle(shape_id + 1, values[0], values[1], values[2])
        return False

    def clear_slot(self) -> None:
        self._form.textEdit.setText('')
        self._form.textEdit_2.setText('')
        self._form.textEdit_3.setText('')
        self._form.textEdit_4.setText('')

    def reset_slot(self) -> None:
        self._form.textEdit_5.setText('')
