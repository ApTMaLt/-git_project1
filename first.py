import sys
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Рисование')
        uic.loadUi('krygi.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_figure(qp)
        qp.end()

    def draw_figure(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        w = randint(0, 200)
        qp.drawEllipse(randint(100, 700) - w // 2, randint(100, 350) - w // 2, w, w)

    def paint(self):
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
