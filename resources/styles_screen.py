from PyQt6.QtGui import QFont

def getFont(font: str, size: int):
    return QFont(font, size)

#* Variables compartidas:

iconApp = r'yticon.ico'
#* Iniciar de izquierda a derecha => x1: 1, y1: 1
#* Iniciar de arriba hacia abajo  => x1: 0, y1: 0
gradientUi = 'background: qlineargradient(x1: 1, y1: 1, x2: 0, y2: 1, stop: 0 #6f0000, stop: 1 #200122);'

fontLabTitle = getFont(font='Comic Sans MS', size=20)
fontLabUrl = getFont(font='Comic Sans MS', size=14)
styleSheetLabel = 'background-color: transparent; color: white; font-family: Comic Sans MS;'

styleSheetInput = 'background-color: transparent; color: white; border-bottom: 2px dotted #154360'
fontInputs = getFont(font='Comic Sans MS', size=14)

styleSheetButton = '''
    QPushButton {
        background: qlineargradient(x1: 1, y1: 1, x2: 0, y2: 1, stop: 0 #0b8793, stop: 1 #360033); 
        font-family: Comic Sans MS;
        color: white; 
        font-size: 11pt; 
        border-radius: 10%; 
        font-weight: bold;
        border: 1px solid #130f40;
    }
    QPushButton:hover { 
        background: qlineargradient(x1: 1, y1: 1, x2: 0, y2: 1, stop: 0 #302b63, stop: 1 #0f0c29);
        border-color: #0a3d62;
        font-size: 12pt; 
        font-weight: normal;
    }
'''
styleSheetBtnOpenVid = '''
    QPushButton {
        background: qlineargradient(x1: 1, y1: 1, x2: 0, y2: 1, stop: 0 #0f9b0f, stop: 1 #000000); 
        border-radius: 10px; 
        color: white; 
        font-size: 11pt; 
        font-weight: bold; 
        font-family: Comic Sans MS;
    }
    QPushButton:hover { 
        background: qlineargradient(x1: 1, y1: 1, x2: 0, y2: 1, stop: 0 #33581D, stop: 1 #000000);
        border-color: #0a3d62;
        font-size: 12pt; 
        font-weight: normal;
    }
'''
styleSheetBtnOpenAud = '''
    QPushButton{
        background: qlineargradient(x1: 1, y1: 1, x2: 0, y2: 1, stop: 0 #870000, stop: 1 #190A05); 
        border-radius: 10px; 
        color: white; 
        font-size: 11pt; 
        font-weight: bold; 
        font-family: Comic Sans MS;
    }
    QPushButton:hover { 
        background: qlineargradient(x1: 1, y1: 1, x2: 0, y2: 1, stop: 0 #6f0000, stop: 1 #190A05);
        border-color: #0a3d62;
        font-size: 12pt; 
        font-weight: normal; 
    }
'''

styleSheetMsg = '''
    QMessageBox { 
        background: qlineargradient(x1: 1, y1: 1, x2: 0, y2: 1, stop: 0 #190A05, stop: 1 #870000); 
        font-family: Comic Sans MS;
    }
    QMessageBox QLabel { 
        color: white; 
        font-size: 14pt; 
        padding-right: 25px;
    }
    QMessageBox QPushButton { 
        width: 80px; 
        color: white;
        font-size: 14pt; 
        font-family: Comic Sans MS;
        background-color: #30336b;
        border: 1px solid #130f40; 
        border-radius: 10%;
    }
    QMessageBox QPushButton:hover { 
        background-color: #130f40;
        border-color: #0a3d62;
    }
'''

