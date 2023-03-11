from resources import styles_screen as st
from PyQt6.QtWidgets import (QButtonGroup, QRadioButton)

class GenerateRadios():

    def generateNetworks(self):
        self.group1 = QButtonGroup(self)
        
        self.radYout = QRadioButton('Youtube', self)
        self.radFace = QRadioButton('Facebook', self)
        self.radInst = QRadioButton('Instagram', self)
        self.radOthers = QRadioButton('Otros', self)

        self.group1.addButton(self.radYout)
        self.group1.addButton(self.radFace)
        self.group1.addButton(self.radInst)
        self.group1.addButton(self.radOthers)

        self.group1.buttons()[0].setChecked(True)

        self.radYout.move(120, 85)
        self.radYout.setStyleSheet(st.styleSheetLabel)
        self.radFace.move(220, 85)
        self.radFace.setStyleSheet(st.styleSheetLabel)
        self.radInst.move(320, 85)
        self.radInst.setStyleSheet(st.styleSheetLabel)
        self.radOthers.move(420, 85)
        self.radOthers.setStyleSheet(st.styleSheetLabel)
        
    def generateOptionsOfDownload(self):
        self.group2 = QButtonGroup(self)
        self.radM4a = QRadioButton('M4A', self)
        self.radMp4 = QRadioButton('MP4', self)

        self.group2.addButton(self.radM4a)
        self.group2.addButton(self.radMp4)

        self.group2.buttons()[0].setChecked(True)

        self.radM4a.move(220, 180)
        self.radM4a.setStyleSheet(st.styleSheetLabel)
        self.radMp4.move(320, 180)
        self.radMp4.setStyleSheet(st.styleSheetLabel)

    def getOptionOfDownload(self):
        opt = 'M4A' if self.radM4a.isChecked() else 'MP4'
        return opt
    
    def getSelectNetwork(self):
        if self.radYout.isChecked():
            return 'YouTube'
        elif self.radFace.isChecked(): 
            return 'Facebook'
        elif self.radInst.isChecked():
            return 'Instagram'
        else:
            return 'Otros'