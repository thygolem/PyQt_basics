import sys
from PyQt5.QtWidgets import QDialog, QApplication
from DialogoHelados import DialogoHelados

class DialogoHeladosApp(QDialog):
    '''Usar los checkboxes para mostrar el precio final'''
    def __init__(self):
        super().__init__()

        self.ui = DialogoHelados()
        self.ui.setupUi(self)

        self.ui.chk_chocolate.stateChanged.connect(self.calcular_total)
        self.ui.chk_fresa.stateChanged.connect(self.calcular_total)
        self.ui.chk_vainilla.stateChanged.connect(self.calcular_total)
        self.ui.chk_limon.stateChanged.connect(self.calcular_total)


        self.ui.chk_agua.stateChanged.connect(self.calcular_total)
        self.ui.chk_cafe.stateChanged.connect(self.calcular_total)
        self.ui.chk_refresco.stateChanged.connect(self.calcular_total)
        
        self.show()

    def calcular_total(self):
        total = 0.0
        # HELADOS
        if self.ui.chk_chocolate.isChecked() == True:
            total += 5
        if self.ui.chk_vainilla.isChecked() == True:
            total += 4
        if self.ui.chk_fresa.isChecked() == True:
            total += 6
        if self.ui.chk_limon.isChecked() == True:
            total += 3
        # BEBIDAS
        if self.ui.chk_agua.isChecked() == True:
            total += 2
        if self.ui.chk_cafe.isChecked() == True:
            total += 3
        if self.ui.chk_refresco.isChecked() == True:
            total += 4
        
        self.ui.lbl_total.setText('Total: {}€'.format(total))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = DialogoHeladosApp()
    dialogo.show()

    sys.exit(app.exec_())