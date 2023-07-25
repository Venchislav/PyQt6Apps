import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from pygame import mixer
from design import Ui_MainWindow
import webbrowser


class Aut(QMainWindow):
    def __init__(self):
        super(Aut, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.code.clicked.connect(self.get_pattern)
        self.ui.browse.clicked.connect(self.get_pattern)
        self.ui.games.clicked.connect(self.get_pattern)
        self.ui.pushButton.clicked.connect(self.set_link)

    def set_link(self):
        if self.ui.lineEdit.text() != '':
            self.web[-1] = self.ui.lineEdit.text()

    def get_pattern(self):
        mixer.init()
        mixer.music.load('press.mp3')
        mixer.music.play()
        btn = self.sender()
        match btn.objectName():
            case 'code':
                self.web = ['https://github.com/Venchislav',
                       'https://www.codewars.com/dashboard',
                       'https://www.youtube.com',
                       'https://www.youtube.com/watch?v=4xDzrJKXOOY&ab_channel=LofiGirl']
                for i in self.web:
                    webbrowser.open(i)
                os.startfile(r'C:\Program Files\JetBrains\PyCharm Community Edition 2023.1.2\bin\pycharm64.exe')
            case 'browse':
                os.startfile(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
            case 'games':
                webbrowser.open('https://www.youtube.com/watch?v=4xDzrJKXOOY&ab_channel=LofiGirl')
                os.startfile(r'C:\Program Files (x86)\Steam\steam.exe')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Aut()
    window.show()

    sys.exit(app.exec())
