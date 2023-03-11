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
    
    def generateInputUser(self):
        self.urlInputU = QLineEdit(self)
        self.urlInputU.resize(400, 30)
        self.urlInputU.move(90, 224)
        self.urlInputU.setStyleSheet(st.styleSheetInput)
        self.urlInputU.setFont(st.fontInputs)
        self.urlInputU.setClearButtonEnabled(True)
        self.urlInputU.setFrame(False)
        self.urlInputU.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def generateInputPassword(self):
        self.urlInputP = QLineEdit(self)
        self.urlInputP.resize(400, 30)
        self.urlInputP.move(90, 274)
        self.urlInputP.setStyleSheet(st.styleSheetInput)
        self.urlInputP.setFont(st.fontInputs)
        self.urlInputP.setClearButtonEnabled(True)
        self.urlInputP.setFrame(False)
        self.urlInputP.setAlignment(Qt.AlignmentFlag.AlignCenter)
