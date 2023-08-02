
################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(581, 411)
        MainWindow.setMinimumSize(QSize(581, 411))
        MainWindow.setMaximumSize(QSize(581, 411))
        icon = QIcon()
        icon.addFile(u":/box/unlock.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget{\n"
"	background-color: white;\n"
"	color: black;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border-radius: 5px;\n"
"	background-color: black;\n"
"	color: white;\n"
"	font-weight: 8px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: white;\n"
"	background-color: black;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: white;\n"
"	background-color: black;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    color: black;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    color: black;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(200, 10, 181, 41))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.logo.setFont(font)
        self.logo.setAlignment(Qt.AlignCenter)
        self.password = QLineEdit(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(50, 140, 411, 31))
        self.password.setAlignment(Qt.AlignCenter)
        self.password.setReadOnly(True)
        self.generate = QPushButton(self.centralwidget)
        self.generate.setObjectName(u"generate")
        self.generate.setGeometry(QRect(240, 190, 91, 31))
        self.generate.setCursor(QCursor(Qt.PointingHandCursor))
        self.len = QLineEdit(self.centralwidget)
        self.len.setObjectName(u"len")
        self.len.setGeometry(QRect(212, 239, 151, 31))
        self.len.setMaxLength(3)
        self.len.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 390, 131, 21))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(220, 390, 131, 21))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(470, 390, 131, 21))
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.digits = QCheckBox(self.centralwidget)
        self.digits.setObjectName(u"digits")
        self.digits.setGeometry(QRect(180, 300, 71, 21))
        font2 = QFont()
        font2.setBold(True)
        self.digits.setFont(font2)
        self.digits.setLayoutDirection(Qt.LeftToRight)
        self.ascii = QCheckBox(self.centralwidget)
        self.ascii.setObjectName(u"ascii")
        self.ascii.setGeometry(QRect(260, 300, 71, 21))
        self.ascii.setFont(font2)
        self.ascii.setLayoutDirection(Qt.LeftToRight)
        self.upper = QCheckBox(self.centralwidget)
        self.upper.setObjectName(u"upper")
        self.upper.setGeometry(QRect(330, 300, 71, 21))
        self.upper.setFont(font2)
        self.upper.setLayoutDirection(Qt.LeftToRight)
        self.generate_2 = QPushButton(self.centralwidget)
        self.generate_2.setObjectName(u"generate_2")
        self.generate_2.setGeometry(QRect(470, 140, 61, 31))
        self.generate_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(257, 50, 71, 61))
        self.label.setPixmap(QPixmap(u":/box/unlock.png"))
        self.label.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"PASSWORDIVE", None))
        self.password.setText(QCoreApplication.translate("MainWindow", u"e*@mp|3 p@ssw0r|)", None))
        self.generate.setText(QCoreApplication.translate("MainWindow", u"GENERATE", None))
        self.len.setPlaceholderText(QCoreApplication.translate("MainWindow", u"length", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"DEEP DIVE.AI", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"1.02", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"PYTHON", None))
        self.digits.setText(QCoreApplication.translate("MainWindow", u"123", None))
        self.ascii.setText(QCoreApplication.translate("MainWindow", u"!@&#", None))
        self.upper.setText(QCoreApplication.translate("MainWindow", u"A-Z", None))
        self.generate_2.setText(QCoreApplication.translate("MainWindow", u"COPY", None))
        self.label.setText("")
    # retranslateUi

