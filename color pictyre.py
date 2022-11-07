import sys
import random

from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


class Effect(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.app = app
        self.filename = QFileDialog.getOpenFileName(self, 'Выберите картинку', '', 'Картинки (*.jpg)')[0]
        self.orig_image = Image.open(self.filename)
        self.curr_image = Image.open(self.filename)
        self.degree = 0
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image.setPixmap(self.a)
        self.image.setPixmap(self.pixmap)
        for button in self.channelButtons.buttons():
            button.clicked.connect(self.rotate)
        for button in self.channelButtons.buttons():
            button.clicked.connect(self.black_white)
        for button in self.channelButtons.buttons():
            button.clicked.connect(self.gray)
        for button in self.channelButtons.buttons():
            button.clicked.connect(self.noises)
        for button in self.channelButtons.buttons():
            button.clicked.connect(self.negative)
        for button in self.channelButtons.buttons():
            button.clicked.connect(self.sepia)

    def rotate(self):
        if self.sender() is self.pushButton_2:
            self.degree -= 90
            degree = -90
        else:
            self.degree += 90
            degree = 90
        self.degree %= 360
        self.curr_image = self.curr_image.rotate(degree, expand=True)
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image.setPixmap(self.pixmap)

    def black_white(self):
        if self.sender() is self.pushButton_3:
            self.curr_image = self.orig_image.copy()
            pixels = self.curr_image.load()
            x, y = self.curr_image.size
            for i in range(x):
                for j in range(y):
                    r = pixels[i, j][0]
                    g = pixels[i, j][1]
                    b = pixels[i, j][2]
                    S = r + g + b
                    if S > ((255 // 2) * 3):
                        r, g, b = 255, 255, 255
                    else:
                        a, b, c = 0, 0, 0
                    pixels = (i, j), (r, g, b)
            self.curr_image = self.curr_image.rotate(self.degree, expand=True)
            self.a = ImageQt(self.curr_image)
            self.pixmap = QPixmap.fromImage(self.a)
            self.image.setPixmap(self.pixmap)

    def gray(self):
        if self.sender() is self.pushButton_5:
            self.curr_image = self.orig_image.copy()
            pixels = self.curr_image.load()
            x, y = self.curr_image.size
            for i in range(x):
                for j in range(y):
                    r = pixels[i, j][0]
                    g = pixels[i, j][1]
                    b = pixels[i, j][2]
                    S = (r + g + b) // 3
                    pixels = (i, j), (S, S, S)
            self.curr_image = self.curr_image.rotate(self.degree, expand=True)
            self.a = ImageQt(self.curr_image)
            self.pixmap = QPixmap.fromImage(self.a)
            self.image.setPixmap(self.pixmap)

    def noises(self):
        if self.sender() is self.pushButton_7:
            self.curr_image = self.orig_image.copy()
            factor = 0  # рандомное число от 10 до 500
            pixels = self.curr_image.load()
            x, y = self.curr_image.size
            for i in range(x):
                for j in range(y):
                    rand = random.randint(-factor, factor)
                    r = pixels[i, j][0] + rand
                    g = pixels[i, j][1] + rand
                    b = pixels[i, j][2] + rand
                    if r < 0:
                        r = 0
                    if g < 0:
                        g = 0
                    if b < 0:
                        b = 0
                    if r > 255:
                        r = 255
                    if r > 255:
                        r = 255
                    if b > 255:
                        b = 255
                    pixels = (i, j), (r, g, b)
            self.curr_image = self.curr_image.rotate(self.degree, expand=True)
            self.a = ImageQt(self.curr_image)
            self.pixmap = QPixmap.fromImage(self.a)
            self.image.setPixmap(self.pixmap)

    def negative(self):
        if self.sender() is self.pushButton_4:
            self.curr_image = self.orig_image.copy()
            pixels = self.curr_image.load()
            x, y = self.curr_image.size
            for i in range(x):
                for j in range(y):
                    r = pixels[i, j][0]
                    g = pixels[i, j][1]
                    b = pixels[i, j][2]
                    pixels = (i, j), (255 - r, 255 - g, 255 - b)
            self.curr_image = self.curr_image.rotate(self.degree, expand=True)
            self.a = ImageQt(self.curr_image)
            self.pixmap = QPixmap.fromImage(self.a)
            self.image.setPixmap(self.pixmap)

    def sepia(self):
        if self.sender() is self.pushButton_6:
            self.curr_image = self.orig_image.copy()
            depth = 0  # рандомное число от 10 до 500
            pixels = self.curr_image.load()
            x, y = self.curr_image.size
            for i in range(x):
                for j in range(y):
                    r = pixels[i, j][0]
                    g = pixels[i, j][1]
                    b = pixels[i, j][2]
                    S = (r + g + b) // 3
                    r = S + depth * 2
                    g = S + depth
                    b = S
                    if r > 255:
                        r = 255
                    if g > 255:
                        g = 255
                    if b > 255:
                        b = 255
                    pixels = (i, j), (r, g, b)
            self.curr_image = self.curr_image.rotate(self.degree, expand=True)
            self.a = ImageQt(self.curr_image)
            self.pixmap = QPixmap.fromImage(self.a)
            self.image.setPixmap(self.pixmap)

    def transparency(self):
        if self.sender() is self.verticalSlider:
            pass

def except_hook(clc, exception, traseback):
    sys.__excepthook__(clc, exception, traseback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = Effect()
    ex.show()
    sys.exit(app.exec())