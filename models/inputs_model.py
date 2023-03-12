from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLineEdit, QCheckBox
from resources import styles_screen as st

class GenerateInputs():

    def generateInputUrl(self, download):
        self.urlInput = QLineEdit(self)
        self.urlInput.resize(400, 30)
        self.urlInput.move(90, 124)
        self.urlInput.setStyleSheet(st.styleSheetInput)
        self.urlInput.setFont(st.fontInputs)
        self.urlInput.setClearButtonEnabled(True)
        self.urlInput.setFrame(False)
        self.urlInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.urlInput.returnPressed.connect(download)
        self.urlInput.setFocus()

    def getUrl(self):
        return self.urlInput.text().replace(' ', "")
    
    def cleanUrl(self):
        self.urlInput.clear()
