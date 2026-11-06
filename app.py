from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow

from interfaz_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.botonConvertir.clicked.connect(self.conversor_divisas)
        self.seleccionarDivisa.currentIndexChanged.connect(self.cambiar_posicionesself)




    def conversor_divisas(self,cantidad):
        #  tipo = self.seleccionarDivisa()
        #  tipo = tipo.text()
        valor = self.cantidadIntroducida.value()

        divisa = self.seleccionarDivisa.currentIndex()

        if divisa == 0:
            valor = valor * 1.12
            valor = round(valor, 2)

        else:
            valor = valor * 0.89
            valor = round(valor, 2)

        self.cantidadResultado.setText(str(valor))

    def cambiar_posicionesself(self):

        divisa = self.seleccionarDivisa.currentIndex()
        if divisa == 0:
            self.logo1.setPixmap(QPixmap("espania.png"))
            self.logo2.setPixmap(QPixmap("eeuu.png"))
            self.textoDivisa1.setText("Cantidad en eruros ( € )")
            self.textoDivisa2.setText("Cantidad en dolares ( $ )")

        else:
            self.logo1.setPixmap(QPixmap("eeuu.png"))
            self.logo2.setPixmap(QPixmap("espania.png"))
            self.textoDivisa1.setText("Cantidad en dolares ( $ )")
            self.textoDivisa2.setText("Cantidad en eruros ( € )")



app = QApplication()
window = MainWindow()
window.show()
app.exec()