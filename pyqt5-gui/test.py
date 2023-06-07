import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(800, 600)
        self.setWindowTitle('Painter Board')

        self.label = QLabel(self)
        self.label.setGeometry(0, 200, 400, 400)
        self.label.setPixmap(QPixmap("../img/products/Sunglasses/Sunglasses1.png"))
        self.label.setScaledContents(True)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())