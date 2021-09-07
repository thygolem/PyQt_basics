# https://www.youtube.com/watch?v=JTR8BDa2Vb4&list=PL2PZw96yQChwe5ZrLoRjf8kjTYd3KKzKZ&index=8
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from DialogoVentaCamisa import DialogoVentaCamisa

class DialogoVentaCamisaAplicacion(QDialog):
    '''Aplicación de selección de producto y tipo de pago'''
    def __init__(self):
        super().__init__()

        self.ui = DialogoVentaCamisa()
        self.ui.setupUi(self)
        
        self.ui.rbn_talla_m.toggled.connect(self.mostrar_informacion)
        self.ui.rbn_talla_l.toggled.connect(self.mostrar_informacion)
        self.ui.rbn_talla_xl.toggled.connect(self.mostrar_informacion)
        self.ui.rbn_talla_xxl.toggled.connect(self.mostrar_informacion)

        self.ui.rbn_pago_tarjeta.toggled.connect(self.mostrar_informacion)
        self.ui.rbn_pago_domiciliado.toggled.connect(self.mostrar_informacion)
        self.ui.rbn_pago_presencial.toggled.connect(self.mostrar_informacion)
        

        self.show()

    def mostrar_informacion(self):
        '''Devolver el dato correcto'''
        talla_seleccionada = ''
        metodo_pago = ''

        if self.ui.rbn_talla_m.isChecked() == True:
            talla_seleccionada = 'M' 
        if self.ui.rbn_talla_l.isChecked() == True:
            talla_seleccionada = 'L'
        if self.ui.rbn_talla_xl.isChecked() == True:
            talla_seleccionada = 'XL'
        if self.ui.rbn_talla_xxl.isChecked() == True:
            talla_seleccionada = 'XXL'

        if self.ui.rbn_pago_tarjeta.isChecked() == True:
            metodo_pago = 'con trajeta' 
        if self.ui.rbn_pago_domiciliado.isChecked() == True:
            metodo_pago = 'Domiciliado'
        if self.ui.rbn_pago_presencial.isChecked() == True:
            metodo_pago = 'Presencial'

        self.ui.lbl_mostrar_talla_pago.setText('La talla {} con pago {}'.format(talla_seleccionada, metodo_pago))

if __name__ == '__main__':
    app = QApplication(sys.argv) # Creamos la app y le pasamos la lista de argumentos recibidos desde la consola
    dialogo = DialogoVentaCamisaAplicacion() # Usamos la clase creada en este archivo
    dialogo.show() # Ejecutamos la clase
    
    sys.exit(app.exec_())