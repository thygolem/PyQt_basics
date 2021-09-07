import sys
from PyQt5.QtWidgets import QDialog, QApplication
from DialogoClaseVuelo import DialogoClaseVuelo


class DialogoClaseVueloAplicacion(QDialog):
    '''
    Aplicacion para elegir la clase de vuelo. 
    El sistema muestra en la etiqueta el atributo seleccionado
    '''
    def __init__(self):
        super().__init__()
        self.dialogo = DialogoClaseVuelo()
        self.dialogo.setupUi(self)

        self.dialogo.rbn_primera_clase.toggled.connect(self.mostrar_informacion)
        self.dialogo.rbn_clase_negocios.toggled.connect(self.mostrar_informacion)
        self.dialogo.rbn_clase_economica.toggled.connect(self.mostrar_informacion)

        self.show()

    def mostrar_informacion(self):
        coste_vuelo = 0 # Declaramos el valor inicial del precio de vuelo

        if self.dialogo.rbn_primera_clase.isChecked() == True:
            coste_vuelo = 190
        if self.dialogo.rbn_clase_negocios.isChecked() == True:
            coste_vuelo = 130
        if self.dialogo.rbn_clase_economica.isChecked() == True:
            coste_vuelo = 90

        self.dialogo.lbl_resultado_seleccion.setText('El coste del vuelo es de {}€'.format(coste_vuelo))


if __name__ == '__main__':
    app = QApplication(sys.argv) # Creamos la app y le pasamos la lista de argumentos recibidos desde la consola
    dialogo = DialogoClaseVueloAplicacion() # Usamos la clase creada en este archivo
    dialogo.show() # Ejecutamos la clase
    sys.exit(app.exec_())