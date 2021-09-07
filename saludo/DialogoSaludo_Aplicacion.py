import sys
from PyQt5.QtWidgets import QDialog, QApplication
from DialogoSaludo import *


class DialogoSaludoAplicacion (QDialog):
    '''
    Creamos objeto de nuestro diálogo saludo
    '''
    def __init__(self):
        super().__init__()

        self.dialogo = Ui_DialogoSaludar()
        self.dialogo.setupUi(self)

        self.dialogo.btn_saludar.clicked.connect(self.mostrar_saludo) # Event Handler
        # Vinculamos el botón con el método 'mostrar saludo' que creamos más abajo
        self.show()

    def mostrar_saludo(self):
        mensaje = self.dialogo.txt_nombre.text() # text() para obtener el texto de diálogo
        self.dialogo.lbl_msg_saludo.setText(mensaje)
        # Le asignamos al elemento que deberá mostrar el texto, el mensaje que el usuario ha escrito

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = DialogoSaludoAplicacion()
    dialogo.show()
    sys.exit(app.exec_())