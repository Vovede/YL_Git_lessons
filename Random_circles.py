import sys
import random

from PyQt6.QtCore import QRect
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic


class Circles(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)

        self.circles = []
        self.pushButton.clicked.connect(self.spawnCircles)

    def spawnCircles(self):
        for _ in range(5):
            radius = random.randint(50, 100)
            position = [random.randint(0, 400), random.randint(0, 400)]
            self.circles.append((position[0], position[1], radius))
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)

        for x, y, radius in self.circles:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            qp.setPen(QColor(r, g, b))
            qp.setBrush(QColor(r, g, b, 255))
            qp.drawEllipse(QRect(x, y, radius, radius))

        self.circles = []


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Circles()
    window.show()
    sys.exit(app.exec())
