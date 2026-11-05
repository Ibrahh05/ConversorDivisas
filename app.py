from PySide6.QtWidgets import QApplication, QMainWindow

from interfaz_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.botonConvertir.clicked.connect(self.conversor_divisas)

    def conversor_divisas(self,cantidad):
      #  tipo = self.seleccionarDivisa()
      #  tipo = tipo.text()
      valor = self.cantidadIntroducida.value()

      divisa = self.seleccionarDivisa.currentIndex()

      valor = valor * 1.12

      self.cantidadResultado.setText(str(valor))




app = QApplication()
window = MainWindow()
window.show()
app.exec()