import random
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5.QtGui import QColor, QPainter
import sys


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.drawCircle)
        self.x = 0
        self.y = 0
        self.diameter = 0
        self.circleDrawn = False

    def paintEvent(self, event):
        if self.circleDrawn:
            qp = QPainter()
            qp.begin(self)
            pen = qp.pen()
            pen.setColor(QColor(255, 255, 0))
            pen.setWidth(3)
            qp.setPen(pen)
            qp.drawEllipse(self.x, self.y, self.diameter, self.diameter)
            qp.end()

    def drawCircle(self):
        self.diameter = random.randint(50, 200)
        self.x = random.randint(0, 742 - self.diameter)
        self.y = random.randint(0, 562 - self.diameter)
        self.circleDrawn = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
