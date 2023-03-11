import os
from resources import form_download as fm, dialog_screen as dl

def verifyPath(path):
    existe = os.path.exists(fm.rootDownload + f'\\{path}')
    return existe

def openVideos(network):
    if verifyPath(f'{network} Videos'):
        os.startfile(fm.rootDownload + f'\\{network} Videos')
    else:
        dl.showMessage('Aun no ha descargado un video.')

def openAudios(network):
    if verifyPath(f'{network} Audios'):
        os.startfile(fm.rootDownload + f'\\{network} Audios')
    else:
        dl.showMessage('Aun no ha descargado un audio.')