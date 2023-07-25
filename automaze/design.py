
################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(749, 375)
        MainWindow.setMinimumSize(QSize(749, 375))
        MainWindow.setMaximumSize(QSize(749, 375))
        MainWindow.setStyleSheet(u"QWidget{\n"
"	color: white;\n"
"	background-color: black;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: white;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	border-radius: 14px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border-radius: 8px;\n"
"	background-color: white;\n"
"	color: black;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(140, 150, 481, 111))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 0, 231, 71))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 50, 391, 71))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 350, 121, 21))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 350, 121, 21))
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(630, 350, 121, 21))
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.games = QPushButton(self.centralwidget)
        self.games.setObjectName(u"games")
        self.games.setGeometry(QRect(460, 200, 156, 109))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.games.sizePolicy().hasHeightForWidth())
        self.games.setSizePolicy(sizePolicy)
        self.games.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/steam_220789.png", QSize(), QIcon.Normal, QIcon.Off)
        self.games.setIcon(icon)
        self.games.setIconSize(QSize(64, 64))
        self.code = QPushButton(self.centralwidget)
        self.code.setObjectName(u"code")
        self.code.setGeometry(QRect(137, 200, 156, 109))
        sizePolicy.setHeightForWidth(self.code.sizePolicy().hasHeightForWidth())
        self.code.setSizePolicy(sizePolicy)
        self.code.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/web-programming_1336593.png", QSize(), QIcon.Normal, QIcon.Off)
        self.code.setIcon(icon1)
        self.code.setIconSize(QSize(64, 64))
        self.browse = QPushButton(self.centralwidget)
        self.browse.setObjectName(u"browse")
        self.browse.setGeometry(QRect(299, 200, 155, 109))
        sizePolicy.setHeightForWidth(self.browse.sizePolicy().hasHeightForWidth())
        self.browse.setSizePolicy(sizePolicy)
        self.browse.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/internet_2985047.png", QSize(), QIcon.Normal, QIcon.Off)
        self.browse.setIcon(icon2)
        self.browse.setIconSize(QSize(64, 64))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(160, 130, 331, 16))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(500, 130, 101, 20))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Automaze", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Automaze", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"stay productive", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"VENCHISLAV", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"2023", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PYTHON", None))
        self.games.setText("")
        self.code.setText("")
        self.browse.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Custom video link from web", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"confirm", None))
    # retranslateUi

