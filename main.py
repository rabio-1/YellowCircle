import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.yellowbtn.clicked.connect(self.run)
        self.flag = False

    def paintEvent(self, e):
        if not self.flag:
            return
        qp = QPainter(self)
        qp.begin(self)  # начать изменение
        qp.setPen(QColor('yellow'))  # цвет карандаша
        qp.setBrush(QColor('yellow'))  # цвет кисти для закраски
        for _ in range(randint(1, 10)):
            x = randint(0, 300)
            y = randint(0, 300)
            r = randint(10, 100)  # радиус
            qp.drawEllipse(x, y, r, r)
        qp.end()  # конец изменений

    def run(self):
        self.flag = True
        self.repaint()  # перерисовать содержимое формы


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
