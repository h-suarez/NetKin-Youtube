import os

#* Ruta de descarga
rootDownload = '\\'.join(os.getcwd().split('\\')[:3]) + r'\Downloads'

#* Formatos de descarga

def formatAudioYoutube(network: str):
    formatoAudio = {
        'format': 'bestaudio[ext=m4a]/bestaudio',
        'outtmpl': f'{rootDownload}\\{network} Audios\\%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
            'preferredquality': '320',
        }],
        'embed-thumbnail': True,
        'embed-metadata': True,
    }
    return formatoAudio

def formatVideoYoutube(network: str):
    formatoVideo = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': f'{rootDownload}\\{network} Videos\\%(title)s.%(ext)s',
        'merge-output-format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'embed-thumbnail': True,
        'embed-subs': True,
        'sub-langs': 'es,en',
    }
    return formatoVideo

def formatAudioFacebook(network: str):
    formatoAudio = {
        'format': 'bestaudio[ext=m4a]/bestaudio',
        'outtmpl': f'{rootDownload}\\{network} Audios\\%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
            'preferredquality': '320',
        }],
        'embed-thumbnail': True,
        'embed-metadata': True,
    }
    return formatoAudio

def formatVideoFacebook(network: str):
    formatoVideo = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': f'{rootDownload}\\{network} Videos\\%(title)s.%(ext)s',
        'merge-output-format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'embed-thumbnail': True,
        'embed-subs': True,
        'sub-langs': 'es,en',
    }
    return formatoVideo

def formatAudioInstagram(network: str):
    formatoAudio = {
        'format': 'bestaudio[ext=m4a]/bestaudio',
        'outtmpl': f'{rootDownload}\\{network} Audios\\%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
            'preferredquality': '320',
        }],
        'embed-thumbnail': True,
        'embed-metadata': True,
    }
    return formatoAudio

def formatVideoInstagram(network: str):
    formatoVideo = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': f'{rootDownload}\\{network} Videos\\%(title)s.%(ext)s',
        'merge-output-format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'embed-thumbnail': True,
        'embed-subs': True,
        'sub-langs': 'es,en',
    }
    return formatoVideo

def formatAudioOthers(network: str):
    formatoAudio = {
        'format': 'bestaudio[ext=m4a]/bestaudio',
        'outtmpl': f'{rootDownload}\\{network} Audios\\%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
            'preferredquality': '320',
        }],
        'embed-thumbnail': True,
        'embed-metadata': True,
    }
    return formatoAudio

def formatVideoOthers(network: str):
    formatoVideo = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': f'{rootDownload}\\{network} Videos\\%(title)s.%(ext)s',
        'merge-output-format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'embed-thumbnail': True,
        'embed-subs': True,
        'sub-langs': 'es,en',
    }
    return formatoVideo