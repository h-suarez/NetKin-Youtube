from resources import styles_screen as st
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (QPushButton, QGraphicsDropShadowEffect)

def generateButtonDownload(self, download):
    btnDownload = QPushButton('Descargar', self)
    btnDownload.resize(150, 30)
    btnDownload.move(520, 125)
    btnDownload.setStyleSheet(st.styleSheetButton)
    sombra = QGraphicsDropShadowEffect(self)
    sombra.setBlurRadius(30)
    sombra.setColor(QColor(7, 33, 49, 255))
    btnDownload.setGraphicsEffect(sombra)
    btnDownload.clicked.connect(download)

def generateBtnVideos(self, openVids):
    btnVideos = QPushButton('Ver videos', self)
    btnVideos.resize(150, 30)
    btnVideos.move(180, 240)
    btnVideos.setStyleSheet(st.styleSheetBtnOpenVid)
    sombra = QGraphicsDropShadowEffect(self)
    sombra.setBlurRadius(30)
    sombra.setColor(QColor(5, 43, 2, 255))
    btnVideos.setGraphicsEffect(sombra)
    btnVideos.clicked.connect(openVids)

def generateBtnAudios(self, openAudi):
    btnAudios = QPushButton('Ver audios', self)
    btnAudios.resize(150, 30)
    btnAudios.move(350, 240)
    btnAudios.setStyleSheet(st.styleSheetBtnOpenAud)
    sombra = QGraphicsDropShadowEffect(self)
    sombra.setBlurRadius(30)
    sombra.setColor(QColor(186, 4, 40, 255))
    btnAudios.setGraphicsEffect(sombra)
    btnAudios.clicked.connect(openAudi)