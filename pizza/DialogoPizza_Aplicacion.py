# https://www.youtube.com/watch?v=tlOCmdnI0Ao&list=PL2PZw96yQChwe5ZrLoRjf8kjTYd3KKzKZ&index=9

import sys
from PyQt5.QtWidgets import QDialog, QApplication
#, QtWidgets, QPushButton
from DialogoPizza import DialogoPizza

class DialogoPizzaAplicacion(QDialog):
    '''Selección de ingredientes sobre pizza básica aumenta el precio final'''
    def __init__(self):
        super().__init__()

        self.ui = DialogoPizza()
        self.ui.setupUi(self)

        self.ui.chk_queso.stateChanged.connect(self.calcular_precio_final)
        self.ui.chk_champ.stateChanged.connect(self.calcular_precio_final)
        self.ui.chk_salsa.stateChanged.connect(self.calcular_precio_final)

        self.show()

    def calcular_precio_final(self):
        precio_basico = 15

        if self.ui.chk_queso.isChecked() == True:
            precio_basico += 1
        if self.ui.chk_champ.isChecked() == True:
            precio_basico += 1
        if self.ui.chk_salsa.isChecked() == True:
            precio_basico += 2

        self.ui.lbl_precio_final.setText('El precio es {}€'.format(precio_basico))


if __name__ == '__main__':
    app = QApplication(sys.argv) # Creamos la app y le pasamos la lista de argumentos recibidos desde la consola
    dialogo = DialogoPizzaAplicacion() # Usamos la clase creada en este archivo
    dialogo.show() # Ejecutamos la clase
    
    sys.exit(app.exec_())