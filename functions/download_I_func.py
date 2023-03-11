from yt_dlp import YoutubeDL as yt, DownloadError, DownloadCancelled, SameFileError
from resources import form_download as fm, dialog_screen as dl

def downloadMp4(url: str):
    try:
        with yt(fm.formatVideoInstagram('Instagram')) as dic:
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
        with yt(fm.formatAudioInstagram('Instagram')) as dic:
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









# yt-dlp "https://www.instagram.com/<username>/" --username=<tu_nombre_de_usuario> --password=<tu_contraseña>

# import yt_dlp

# # Inicializar una instancia de yt-dlp
# ydl = yt_dlp.YoutubeDL()

# # Iniciar sesión en Instagram (para acceder a los perfiles privados a los que sigues)
# username = 'TU_NOMBRE_DE_USUARIO_DE_INSTAGRAM'
# password = 'TU_CONTRASEÑA_DE_INSTAGRAM'
# cookies = ydl.extractor.instagram.InstagramIE._get_cookies(username, password)

# # Configurar opciones de descarga
# options = {
#     'cookies': cookies,
#     'quiet': True,
#     'outtmpl': 'TU_DIRECTORIO_DE_DESCARGA/%(username)s/%(upload_date)s_%(id)s.%(ext)s',
# }

# # Descargar la última publicación del perfil privado
# ydl.download(['https://www.instagram.com/p/ULTIMA_PUBLICACION_DEL_PERFIL/'], options=options)
