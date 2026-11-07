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
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QVBoxLayout, QWidget)
import recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(896, 870)
        MainWindow.setFocusPolicy(Qt.WheelFocus)
        MainWindow.setContextMenuPolicy(Qt.PreventContextMenu)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.gridWidget = QWidget(self.centralwidget)
        self.gridWidget.setObjectName(u"gridWidget")
        self.gridWidget.setMaximumSize(QSize(16777215, 185))
        self.gridLayout = QGridLayout(self.gridWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.cantidadIntroducida = QSpinBox(self.gridWidget)
        self.cantidadIntroducida.setObjectName(u"cantidadIntroducida")
        font1 = QFont()
        font1.setPointSize(16)
        self.cantidadIntroducida.setFont(font1)
        self.cantidadIntroducida.setMaximum(999999999)

        self.gridLayout.addWidget(self.cantidadIntroducida, 4, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logo2 = QLabel(self.gridWidget)
        self.logo2.setObjectName(u"logo2")
        self.logo2.setMaximumSize(QSize(68, 68))
        self.logo2.setPixmap(QPixmap(u":/imagenes/eeuu.png"))
        self.logo2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.logo2)

        self.textoDivisa2 = QLabel(self.gridWidget)
        self.textoDivisa2.setObjectName(u"textoDivisa2")
        self.textoDivisa2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.textoDivisa2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logo1 = QLabel(self.gridWidget)
        self.logo1.setObjectName(u"logo1")
        self.logo1.setMaximumSize(QSize(68, 68))
        self.logo1.setFont(font1)
        self.logo1.setPixmap(QPixmap(u":/imagenes/espania.png"))
        self.logo1.setScaledContents(True)

        self.horizontalLayout.addWidget(self.logo1)

        self.textoDivisa1 = QLabel(self.gridWidget)
        self.textoDivisa1.setObjectName(u"textoDivisa1")
        self.textoDivisa1.setMaximumSize(QSize(16777215, 61))
        self.textoDivisa1.setFont(font1)
        self.textoDivisa1.setTabletTracking(False)
        self.textoDivisa1.setMargin(0)

        self.horizontalLayout.addWidget(self.textoDivisa1)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.cantidadResultado = QLineEdit(self.gridWidget)
        self.cantidadResultado.setObjectName(u"cantidadResultado")
        self.cantidadResultado.setEnabled(False)
        self.cantidadResultado.setMaximumSize(QSize(365, 16777215))
        self.cantidadResultado.setFont(font1)

        self.gridLayout.addWidget(self.cantidadResultado, 4, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.gridWidget)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.tipoConversion = QLabel(self.centralwidget)
        self.tipoConversion.setObjectName(u"tipoConversion")
        self.tipoConversion.setMaximumSize(QSize(16777215, 30))
        self.tipoConversion.setFont(font1)
        self.tipoConversion.setMargin(0)

        self.verticalLayout_3.addWidget(self.tipoConversion)

        self.seleccionarDivisa = QComboBox(self.centralwidget)
        self.seleccionarDivisa.addItem("")
        self.seleccionarDivisa.addItem("")
        self.seleccionarDivisa.setObjectName(u"seleccionarDivisa")
        self.seleccionarDivisa.setFont(font1)

        self.verticalLayout_3.addWidget(self.seleccionarDivisa)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.botonConvertir = QPushButton(self.centralwidget)
        self.botonConvertir.setObjectName(u"botonConvertir")
        self.botonConvertir.setMaximumSize(QSize(500, 40))
        self.botonConvertir.setFont(font1)
        self.botonConvertir.setAutoFillBackground(False)
        self.botonConvertir.setAutoDefault(False)

        self.horizontalLayout_3.addWidget(self.botonConvertir)

        self.botonSalir = QPushButton(self.centralwidget)
        self.botonSalir.setObjectName(u"botonSalir")
        self.botonSalir.setMaximumSize(QSize(500, 40))
        self.botonSalir.setFont(font1)

        self.horizontalLayout_3.addWidget(self.botonSalir)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 896, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.botonConvertir.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Conversor de divisas", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Conversor de divisas", None))
        self.logo2.setText("")
        self.textoDivisa2.setText(QCoreApplication.translate("MainWindow", u"Cantidad en dolares ( $ )", None))
        self.logo1.setText("")
        self.textoDivisa1.setText(QCoreApplication.translate("MainWindow", u"Cantidad en euros ( \u20ac )", None))
        self.tipoConversion.setText(QCoreApplication.translate("MainWindow", u"Tipo de conversi\u00f3n", None))
        self.seleccionarDivisa.setItemText(0, QCoreApplication.translate("MainWindow", u"Euro ( \u20ac ) -> Dolar ( $ )", None))
        self.seleccionarDivisa.setItemText(1, QCoreApplication.translate("MainWindow", u"Dolar ( $ ) -> Euro ( \u20ac )", None))

        self.botonConvertir.setText(QCoreApplication.translate("MainWindow", u"Convertir", None))
        self.botonSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
    # retranslateUi

