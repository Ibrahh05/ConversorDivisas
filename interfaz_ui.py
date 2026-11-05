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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)
import recursos_rc
import recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(849, 837)
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

        self.gridWidget = QWidget(self.centralwidget)
        self.gridWidget.setObjectName(u"gridWidget")
        self.gridWidget.setMaximumSize(QSize(16777215, 185))
        self.gridLayout = QGridLayout(self.gridWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.cantidadResultado = QLineEdit(self.gridWidget)
        self.cantidadResultado.setObjectName(u"cantidadResultado")
        self.cantidadResultado.setEnabled(False)
        self.cantidadResultado.setMaximumSize(QSize(365, 16777215))
        self.cantidadResultado.setFont(font)

        self.gridLayout.addWidget(self.cantidadResultado, 4, 1, 1, 1)

        self.cantidadIntroducida = QSpinBox(self.gridWidget)
        self.cantidadIntroducida.setObjectName(u"cantidadIntroducida")
        self.cantidadIntroducida.setFont(font)

        self.gridLayout.addWidget(self.cantidadIntroducida, 4, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logoEsp = QLabel(self.gridWidget)
        self.logoEsp.setObjectName(u"logoEsp")
        self.logoEsp.setMaximumSize(QSize(68, 68))
        self.logoEsp.setFont(font)
        self.logoEsp.setPixmap(QPixmap(u":/imagenes/espania.png"))
        self.logoEsp.setScaledContents(True)

        self.horizontalLayout.addWidget(self.logoEsp)

        self.texto_euros = QLabel(self.gridWidget)
        self.texto_euros.setObjectName(u"texto_euros")
        self.texto_euros.setMaximumSize(QSize(16777215, 61))
        self.texto_euros.setFont(font)
        self.texto_euros.setTabletTracking(False)
        self.texto_euros.setMargin(0)

        self.horizontalLayout.addWidget(self.texto_euros)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logoEu = QLabel(self.gridWidget)
        self.logoEu.setObjectName(u"logoEu")
        self.logoEu.setMaximumSize(QSize(68, 68))
        self.logoEu.setPixmap(QPixmap(u":/imagenes/eeuu.png"))
        self.logoEu.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.logoEu)

        self.texto_dolares = QLabel(self.gridWidget)
        self.texto_dolares.setObjectName(u"texto_dolares")
        self.texto_dolares.setFont(font)

        self.horizontalLayout_2.addWidget(self.texto_dolares)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.gridWidget)

        self.tipoConversion = QLabel(self.centralwidget)
        self.tipoConversion.setObjectName(u"tipoConversion")
        self.tipoConversion.setMaximumSize(QSize(16777215, 30))
        self.tipoConversion.setFont(font)
        self.tipoConversion.setMargin(0)

        self.verticalLayout_3.addWidget(self.tipoConversion)

        self.seleccionarDivisa = QComboBox(self.centralwidget)
        self.seleccionarDivisa.addItem("")
        self.seleccionarDivisa.addItem("")
        self.seleccionarDivisa.setObjectName(u"seleccionarDivisa")
        self.seleccionarDivisa.setFont(font)

        self.verticalLayout_3.addWidget(self.seleccionarDivisa)

        self.botonConvertir = QPushButton(self.centralwidget)
        self.botonConvertir.setObjectName(u"botonConvertir")
        self.botonConvertir.setFont(font)

        self.verticalLayout_3.addWidget(self.botonConvertir)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 849, 22))
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
        self.logoEsp.setText("")
        self.texto_euros.setText(QCoreApplication.translate("MainWindow", u"Cantidad en euros ( \u20ac )", None))
        self.logoEu.setText("")
        self.texto_dolares.setText(QCoreApplication.translate("MainWindow", u"Cantidad en dolares ( $ )", None))
        self.tipoConversion.setText(QCoreApplication.translate("MainWindow", u"Tipo de conversi\u00f3n", None))
        self.seleccionarDivisa.setItemText(0, QCoreApplication.translate("MainWindow", u"Euro ( \u20ac ) -> Dolar ( $ )", None))
        self.seleccionarDivisa.setItemText(1, QCoreApplication.translate("MainWindow", u"Dolar ( $ ) -> Euro ( \u20ac )", None))

        self.botonConvertir.setText(QCoreApplication.translate("MainWindow", u"Convertir", None))
    # retranslateUi

