import os

#* Ruta de descarga
rootDownload = '\\'.join(os.getcwd().split('\\')[:3]) + r'\Downloads'

#* Formatos de descarga

def formatAudioYoutube(network: str):
    formatoAudio = {
        "format" : "bestaudio[ext=m4a]",
        'quiet' : False,
        "postprocessors" : [{
            "key": "FFmpegExtractAudio",
            "preferredcodec"  : "m4a",
            "preferredquality"  : '192'
        }],
        "extractaudio": False,
        "outtmpl"     : f'{rootDownload}\\{network} Audios\\' + "/%(title)s.%(ext)s",
    }
    return formatoAudio

def formatVideoYoutube(network: str):
    formatoVideo = {
        "format" : "best",
        'quiet' : False,
        "extractaudio": False,
        "outtmpl"     : f'{rootDownload}\\{network} Videos\\' + "/%(title)s.%(ext)s",
    }
    return formatoVideo

def formatAudioFacebook(network: str):
    formatoAudio = {
        "format"         : "bestaudio",
        "extractaudio"   : True,
        "audio-format"   : "m4a",
        "outtmpl"        : f'{rootDownload}\\{network} Audios\\' + "/%(title)s.%(ext)s",
    }
    return formatoAudio

def formatVideoFacebook(network: str):
    formatoVideo = {
        "format"   : "best",
        "outtmpl"  : f'{rootDownload}\\{network} Videos\\' + "/%(title)s.%(ext)s",
    }
    return formatoVideo

def formatAudioInstagram(network: str):
    formatoAudio = {
        "quiet"          : True,
        "format"         : "bestaudio/best",
        "postprocessors" : [{
            'key'              : 'FFmpegExtractAudio',
            'preferredcodec'   : 'm4a',
            'preferredquality' : '192',
        }],
        "outtmpl"        : f'{rootDownload}\\{network} Audios\\' + "/%(title)s.%(ext)s",
    }
    return formatoAudio

def formatVideoInstagram(network: str):
    formatoVideo = {
        "format"   : "best",
        "outtmpl"  : f'{rootDownload}\\{network} Videos\\' + "/%(title)s.%(ext)s",
    }
    return formatoVideo

def formatAudioOthers(network: str):
    formatoAudio = {
        "format"         : "bestaudio/best",
        "postprocessors" : [{
            'key'              : 'FFmpegExtractAudio',
            'preferredcodec'   : 'm4a',
            'preferredquality' : '192',
        }],
        "outtmpl"        : f'{rootDownload}\\{network} Audios\\' + "/%(title)s.%(ext)s",
    }
    return formatoAudio

def formatVideoOthers(network: str):
    formatoVideo = {
        "format"   : "best",
        "outtmpl"  : f'{rootDownload}\\{network} Videos\\' + "/%(title)s.%(ext)s",
    }
    return formatoVideo