from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QWidget
from PyQt5.QtGui import QColor, QPainter
import sys
from ui_file import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
            pen.setColor(QColor(randint(0,255),randint(0,255),randint(0,255)))
            pen.setWidth(3)
            qp.setPen(pen)
            qp.drawEllipse(self.x, self.y, self.diameter, self.diameter)
            qp.end()

    def drawCircle(self):
        self.diameter = randint(50, 200)
        self.x = randint(0, 742 - self.diameter)
        self.y = randint(0, 562 - self.diameter)
        self.circleDrawn = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
