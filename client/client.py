from PySide6.QtWidgets import QApplication
from app import  *
import sys
from connect import *

if __name__ == "__main__":
    app_init = QApplication(sys.argv)# QApplication: Classe responsável por controlar o fluxo de execução do aplicativo
    window = App()
    window.show()
    sys.exit(app_init.exec())