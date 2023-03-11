from models.main_model import MainMenu
from PyQt6.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MainMenu()
    sys.exit(app.exec())