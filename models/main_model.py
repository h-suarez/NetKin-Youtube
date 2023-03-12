from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (QWidget)
from resources import dimensions_screen as dm, styles_screen as st
from models import labels_model as lb, inputs_model as ip, radios_model as rd, buttons_model as bt
from functions import validator_down_func as vd, validator_files_func as vf

class MainMenu(QWidget):

    def __init__(self):
        super().__init__()
        self.inicialiarUi()

    def inicialiarUi(self):
        self.setWindowTitle("Netkin - Download All Videos")
        self.setGeometry(dm.position_x, dm.position_y, dm.position_w, dm.position_h)
        self.setFixedSize(dm.position_w, dm.position_h)
        self.setWindowIcon(QIcon(st.iconApp))
        self.setStyleSheet(st.gradientUi)
        self.generarFormulario()
        self.show()

    def generarFormulario(self):
        lb.generateTitle(self)
        lb.generateLabelUrl(self)
        ip.GenerateInputs.generateInputUrl(self, self.initDownload)
        rd.GenerateRadios.generateNetworks(self)
        rd.GenerateRadios.generateOptionsOfDownload(self)
        bt.generateButtonDownload(self, self.initDownload)
        bt.generateBtnVideos(self, self.openFileVideos)
        bt.generateBtnAudios(self, self.openFileAudios)

    def initDownload(self):
        vd.downloadVidNet(
            ip.GenerateInputs.getUrl(self), 
            rd.GenerateRadios.getSelectNetwork(self), 
            rd.GenerateRadios.getOptionOfDownload(self)
        )
        ip.GenerateInputs.cleanUrl(self)

    def openFileVideos(self):
        vf.openVideos(rd.GenerateRadios.getSelectNetwork(self))

    def openFileAudios(self):
        vf.openAudios(rd.GenerateRadios.getSelectNetwork(self))