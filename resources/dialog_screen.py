from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox
from resources import styles_screen as st

def showMessage(msg: str):
    msgBox = QMessageBox()
    msgBox.setWindowIcon(QIcon(st.iconApp))
    msgBox.setWindowTitle('Mensaje')
    msgBox.setText(msg)
    msgBox.setStyleSheet(st.styleSheetMsg)
    msgBox.setFixedSize(200,500)
    msgBox.show()
    msgBox.exec()