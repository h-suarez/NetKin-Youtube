from functions import (
    download_Y_func as yd, 
    download_F_func as fd, 
    download_I_func as id, 
    download_O_func as od, 
    validators_url_func as val
)

def downloadY(url: str, opt:str):
    if opt == 'M4A' and val.isValidUrlYou(url):
        yd.downloadM4a(url[:43])
        val.saveUrls(url, opt, 'YouTube')
    elif opt == 'MP4' and val.isValidUrlYou(url):
        yd.downloadMp4(url[:43])
        val.saveUrls(url, opt, 'YouTube')
    else:
        pass

def downloadF(url: str, opt:str):
    if opt == 'M4A' and val.isValidUrlFace(url):
        fd.downloadM4a(url)
        val.saveUrls(url, opt, 'Facebook')
    elif opt == 'MP4' and val.isValidUrlFace(url):
        fd.downloadMp4(url)
        val.saveUrls(url, opt, 'Facebook')
    else:
        pass

def downloadI(url: str, opt:str):
    if opt == 'M4A' and val.isValidUrlInst(url):
        id.downloadM4a(url)
        val.saveUrls(url, opt, 'Instagram')
    elif opt == 'MP4' and val.isValidUrlInst(url):
        id.downloadMp4(url)
        val.saveUrls(url, opt, 'Instagram')
    else:
        pass

def downloadO(url: str, opt:str):
    newUrl = url[:39] if 'twitch' in url != -1 else url
    if opt == 'M4A' and val.isValidUrlOthers(newUrl):
        od.downloadM4a(newUrl)
        val.saveUrls(url, opt, 'Otros')
    elif opt == 'MP4' and val.isValidUrlOthers(newUrl):
        od.downloadMp4(newUrl)
        val.saveUrls(url, opt, 'Otros')
    else:
        pass

def downloadVidNet(url: str, net: str, opt: str):
    if net == 'YouTube':
        downloadY(url, opt)
    elif net == 'Facebook':
        downloadF(url, opt)
    elif net == 'Instagram':
        downloadI(url, opt)
    elif net == 'Otros':
        downloadO(url, opt)
    else:
        print('Opción no valida')