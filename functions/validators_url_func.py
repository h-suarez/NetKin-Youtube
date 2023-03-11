from resources import dialog_screen as dl, form_download as fd

def saveUrls(url, opt, network):
    try:
        archivo = open(fd.rootDownload + fr'\{network} Audios\Descargas.txt', 'a', encoding='utf8') if opt == 'M4A' else open(fd.rootDownload + fr'\{network} Videos\Descargas.txt', 'a', encoding='utf8')
        archivo.write(url + ',\n')
    except Exception as e:
        print('Error al guardar la url: ', e)
    finally:
        archivo.close()

def isValidUrlYou(url: str):
    if url == '':
        dl.showMessage('No ingreso la url del video.')
        return False
    elif url[:32] != 'https://www.youtube.com/watch?v=':
        dl.showMessage('La URL no es valida.')
        return False
    return True

def isValidUrlFace(url: str):
    if url == '':
        dl.showMessage('No ingreso la url del video.')
        return False
    elif url[:25] != 'https://www.facebook.com/':
        dl.showMessage('La URL no es valida.')
        return False
    return True

def isValidUrlInst(url: str):
    if url == '':
        dl.showMessage('No ingreso la url del video.')
        return False
    elif url[:26] != 'https://www.instagram.com/':
        dl.showMessage('La URL no es valida.')
        return False
    return True

def isValidUrlOthers(url: str):
    if url == '':
        dl.showMessage('No ingreso la url del video.')
        return False
    elif url[:8] != 'https://':
        dl.showMessage('La URL no es valida.')
        return False
    return True