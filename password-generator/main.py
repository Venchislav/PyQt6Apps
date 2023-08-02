import sys
import pygame.mixer
from PySide6.QtWidgets import QApplication, QMainWindow
from design import Ui_MainWindow
import random
import pyperclip
from PyQt6 import QtTest
from PySide6.QtGui import QPixmap


class Psw(QMainWindow):
    def __init__(self):
        super(Psw, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        pygame.mixer.init()
        pygame.mixer.music.load('click.wav')
        self.lock = QPixmap('unlock.png')
        self.copied = QPixmap('copy.png')

        self.ui.len.setText('10')
        self.ui.generate.clicked.connect(self.generate)
        self.ui.generate_2.clicked.connect(self.copy_)

    def copy_(self):
        pygame.mixer.music.play()
        pyperclip.copy(self.ui.password.text())
        self.ui.logo.setText('Copied')
        self.ui.label.setPixmap(self.copied)
        QtTest.QTest.qWait(1000)
        self.ui.logo.setText('PASSWORDIVE')
        self.ui.label.setPixmap(self.lock)

    def generate(self):
        if self.ui.len.text() != '' and int(self.ui.len.text()) > 0:
            signs = 'abcdefghigklmnopqrstuvwxyz'
            if self.ui.digits.isChecked():
                signs += '1234567890'
            if self.ui.ascii.isChecked():
                signs += '!@#$%^&*()_-+"№;:?'
            if self.ui.upper.isChecked():
                signs += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            password = ''
            for i in range(int(self.ui.len.text())):
                password += random.choice(signs)
            self.ui.password.setText(password)
            pygame.mixer.music.play()
        else:
            self.ui.password.setText('Incorrect length!')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Psw()
    window.show()

    sys.exit(app.exec())
