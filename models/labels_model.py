from resources import styles_screen as st
from PyQt6.QtWidgets import QLabel

def generateTitle(self):
    titleLabel = QLabel(self)
    titleLabel.setText('NetKin DAV')
    titleLabel.setFont(st.fontLabTitle)
    titleLabel.move(260, 20)
    titleLabel.setStyleSheet(st.styleSheetLabel)

def generateLabelUrl(self):
    urlLabel = QLabel(self)
    urlLabel.setText('URL:')
    urlLabel.setFont(st.fontLabUrl)
    urlLabel.move(30, 130)
    urlLabel.setStyleSheet(st.styleSheetLabel)

def generateLabelUser(self):
    userLabel = QLabel(self)
    userLabel.setText('User:')
    userLabel.setFont(st.fontLabUrl)
    userLabel.move(30, 230)
    userLabel.setStyleSheet(st.styleSheetLabel)

def generateLabelPassword(self):
    claveLabel = QLabel(self)
    claveLabel.setText('Clave:')
    claveLabel.setFont(st.fontLabUrl)
    claveLabel.move(30, 280)
    claveLabel.setStyleSheet(st.styleSheetLabel)