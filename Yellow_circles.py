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
        qp.setPen(QColor(255, 255, 0))
        qp.setBrush(QColor(255, 255, 0, 255))

        for x, y, radius in self.circles:
            qp.drawEllipse(QRect(x, y, radius, radius))
        self.circles = []


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Circles()
    window.show()
    sys.exit(app.exec())
