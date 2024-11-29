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

        self.rads = [i for i in range(50, 100)]
        self.pos = [(x, y) for x in range(400) for y in range(400)]

        self.circles = []
        self.pushButton.clicked.connect(self.spawnCircles)

    def spawnCircles(self):
        for _ in range(5):
            radius = random.choice(self.rads)
            position = random.choice(self.pos)
            self.circles.append((position[0], position[1], radius))
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setPen(QColor(255, 255, 0))
        qp.setBrush(QColor(255, 255, 0, 100))

        for x, y, radius in self.circles:
            qp.drawEllipse(QRect(x, y, radius, radius))
        self.circles = []


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Circles()
    window.show()
    sys.exit(app.exec())
