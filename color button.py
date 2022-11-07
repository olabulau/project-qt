import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QColorDialog


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 150, 150)
        self.setWindowTitle('Диалоговые окна')

        self.button_1 = QPushButton(self)
        self.button_1.move(20, 40)
        self.button_1.setText("Кнопка")
        self.button_1.clicked.connect(self.run)

    def run(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_1.setStyleSheet(
                "background-color: {}".format(color.name()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())