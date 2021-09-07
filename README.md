Estas pruebas consisten en realizar ejemplos prácticos del uso entorno de diseño QtDesigner al cual le aportamos un backend de python.

1) instalar todos los paquetes de Qt necesarios.
https://realpython.com/qt-designer-python/

2) En esta ocasión voy a seguir los tutoriales de esta lista de reproducción de John Ortiz Ordóñez.
https://www.youtube.com/watch?v=cdVns1x2pYE&list=PL2PZw96yQChwe5ZrLoRjf8kjTYd3KKzKZ&index=1

#### COMANDOS ÚTILES
$ python3 -m venv ./venv
$ source venv/bin/activate

#### UNA VEZ REALIZADO EL DISEÑO DE LA INTERFAZ EN QT DESIGNER:
$ pyuic5 {NombreDelArchivoExportado.ui} > {NombreDelArchivoExportado.py}



#### Importar librerias y archivos
import sys
from PyQt5.QtWidgets import QDialog, QApplication