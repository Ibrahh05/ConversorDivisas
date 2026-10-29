# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(731, 555)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.titulo = QLineEdit(self.centralwidget)
        self.titulo.setObjectName(u"titulo")
        font = QFont()
        font.setPointSize(16)
        self.titulo.setFont(font)
        self.titulo.setEchoMode(QLineEdit.EchoMode.Normal)
        self.titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.titulo)

        self.seleccionarDivisa = QComboBox(self.centralwidget)
        self.seleccionarDivisa.addItem("")
        self.seleccionarDivisa.addItem("")
        self.seleccionarDivisa.setObjectName(u"seleccionarDivisa")

        self.verticalLayout_3.addWidget(self.seleccionarDivisa)

        self.cantidadIntroducida = QSpinBox(self.centralwidget)
        self.cantidadIntroducida.setObjectName(u"cantidadIntroducida")

        self.verticalLayout_3.addWidget(self.cantidadIntroducida)

        self.cantidadResultado = QLineEdit(self.centralwidget)
        self.cantidadResultado.setObjectName(u"cantidadResultado")
        self.cantidadResultado.setEnabled(False)

        self.verticalLayout_3.addWidget(self.cantidadResultado)

        self.botonConvertir = QPushButton(self.centralwidget)
        self.botonConvertir.setObjectName(u"botonConvertir")
        self.botonConvertir.setFont(font)

        self.verticalLayout_3.addWidget(self.botonConvertir)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 731, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Conversor de divisas", None))
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"Conversor de divisas", None))
        self.seleccionarDivisa.setItemText(0, QCoreApplication.translate("MainWindow", u"Euro ( \u20ac ) -> Dolar ( $ )", None))
        self.seleccionarDivisa.setItemText(1, QCoreApplication.translate("MainWindow", u"Dolar ( $ ) -> Euro ( \u20ac )", None))

        self.botonConvertir.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

