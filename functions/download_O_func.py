from yt_dlp import YoutubeDL as yt, DownloadError, DownloadCancelled, SameFileError
from resources import form_download as fm, dialog_screen as dl

def downloadMp4(url: str):
    try:
        with yt(fm.formatVideoOthers('Otros')) as dic:
            dic.download([url])
        dl.showMessage('Descarga completa.')
    except DownloadError as e:
        dl.showMessage('El video a descargar no esta disponible o no existe.')
        print('El video a descargar no esta disponible o no existe: ', e)
    except DownloadCancelled as e:
        dl.showMessage('Se detuvo el proceso de descarga.')
        print('Se detuvo el proceso de descarga: ', e)
    except SameFileError as e:
        dl.showMessage('Sobrecarga de descarga de archivos.')
        print('Sobrecarga de descarga de archivos: ', e)
    except Exception as e:
        dl.showMessage('Ocurrion un problema.')
        print('Ocurrion un problema: ', e)

def downloadM4a(url: str):
    try:
        with yt(fm.formatAudioOthers('Otros')) as dic:
            dic.download([url])
        dl.showMessage('Descarga completa.')
    except DownloadError as e:
        dl.showMessage('El video a descargar no esta disponible o no existe.')
        print('El video a descargar no esta disponible o no existe: ', e)
    except DownloadCancelled as e:
        dl.showMessage('Se detuvo el proceso de descarga.')
        print('Se detuvo el proceso de descarga: ', e)
    except SameFileError as e:
        dl.showMessage('Sobrecarga de descarga de archivos.')
        print('Sobrecarga de descarga de archivos: ', e)
    except Exception as e:
        dl.showMessage('Ocurrion un problema.')
        print('Ocurrion un problema: ', e)