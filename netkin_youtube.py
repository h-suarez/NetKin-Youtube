# pyinstaller -F --onefile --windowed --name="Netkin Youtube" --hidden-import=youtube_dl netkin_youtube.py
import os
from tkinter import *
from tkinter import messagebox
from youtube_dl import YoutubeDL as ydl, DownloadError

#* Ruta de descarga
rootDownload = '\\'.join(os.getcwd().split('\\')[:3]) + r'\Downloads'

#* Formatos de descarga
formatoAudio = {
    "format" : "bestaudio[ext=m4a]",
    'quiet' : False,
    "postprocessors" : [{
        "key": "FFmpegExtractAudio",
        "preferredcodec"  : "m4a",
        "preferredquality"  : '192'
    }],
    "extractaudio": False,
    "outtmpl"     : f'{rootDownload}\\Audios\\' + "/%(title)s.%(ext)s",
}
formatoVideo = {
    "format" : "best",
    'quiet' : False,
    "extractaudio": False,
    "outtmpl"     : f'{rootDownload}\\Videos\\' + "/%(title)s.%(ext)s",
}

def showMessage(nivel, msg):
    if nivel == 1:
        messagebox.showinfo("Mensaje", msg)
    elif nivel == 2:
        messagebox.showwarning("Mensaje", msg)
    else:
        messagebox.showerror("Mensaje", msg)

def saveUrls(url, carp):
    try:
        if carp == 'mp4':
            archivo = open(rootDownload + r'\Videos\Descargas.txt', 'a', encoding='utf8')
        elif carp == 'mp3':
            archivo = open(rootDownload + r'\Audios\Descargas.txt', 'a', encoding='utf8')
        archivo.write(url + ',\n')
    except Exception as e:
        print('Error al guardar la url: ', e)
    finally:
        archivo.close()

def verifyPath(path):
    existe = os.path.exists(rootDownload + f'\\{path}')
    return existe

def openVideos():
    if verifyPath('Videos'):
        os.startfile(rootDownload + '\\Videos')
    else:
        showMessage(2, 'Aun no ha descargado un video.')

def openAudios():
    if verifyPath('Audios'):
        os.startfile(rootDownload + '\\Audios')
    else:
        showMessage(2, 'Aun no ha descargado un video.')

def validationUrl(url):
    if url == '':
        showMessage(2, 'No ingreso la url del video.')
        return False
    elif url[:32] != 'https://www.youtube.com/watch?v=':
        showMessage(2, 'La URL no es valida.')
        return False
    else:
        return True

def downloadVideo():
    url = txtUrl.get().replace(' ', "")[:43]
    try:
        if validationUrl(url):
            with ydl(formatoVideo) as dic:
                dic.download([url])
            saveUrls(url, 'mp3')
            showMessage(1, 'Descarga completada.')
            txtUrl.delete(0, END)
        else:
            pass
    except DownloadError as e:
        print('El video a descargar no esta disponible o no existe: ', e)
        showMessage(2, 'El video a descargar no esta disponible o no existe.')
    except Exception as e:
        print('Ocurrion un problema: ', e)
        showMessage(2, 'Ocurrion un problema.')

def downloadAudio():
    url = txtUrl.get().replace(' ', "")[:43]
    try:
        if validationUrl(url):
            with ydl(formatoAudio) as dic:
                dic.download([url])
            saveUrls(url, 'mp3')
            showMessage(1, 'Descarga completada.')
            txtUrl.delete(0, END)
        else:
            pass
    except DownloadError as e:
        print('El video a descargar no esta disponible o no existe: ', e)
        showMessage(2, 'El video a descargar no esta disponible o no existe.')
    except Exception as e:
        print('Ocurrion un problema: ', e)
        showMessage(2, 'Ocurrion un problema.')

def downloadAudioEnt(event):
    url = txtUrl.get().replace(' ', "")[:43]
    try:
        if validationUrl(url):
            with ydl(formatoAudio) as dic:
                dic.download([url])
            saveUrls(url, 'mp3')
            showMessage(1, 'Descarga completada.')
            txtUrl.delete(0, END)
        else:
            pass
    except DownloadError as e:
        print('El video a descargar no esta disponible o no existe: ', e)
        showMessage(2, 'El video a descargar no esta disponible o no existe.')
    except Exception as e:
        print('Ocurrion un problema: ', e)
        showMessage(2, 'Ocurrion un problema.')

#* Creación de la vista
principal = Tk()
principal.title('NetKin YouTube')
principal.geometry('500x250+450+200')
principal.config(bg='#070F1C')
principal.resizable(0, 0)

lblTitulo = Label(
    principal, 
    text="NetKin YouTube",
    fg="white",
    bg="#070F1C",
    font=("Comic Sans MS", 30),
)
lblTitulo.place(x=20, y=15)

txtUrl = Entry(
    width=40,
    font=('Helvetica', 15),
    justify='center',
    borderwidth=0,
)
txtUrl.bind('<Return>', downloadAudioEnt)
txtUrl.focus()
txtUrl.place(x=22, y=90)

btnM4A = Button(
    principal,
    text='M4A (Ent)',
    font=('Comic Sans MS', 10),
    fg='white',
    activeforeground='white',
    bg='#2E750C',
    activebackground="#214F0B",
    width=25,
    borderwidth=1,
    command=downloadAudio
)
btnM4A.place(x=22, y=130)

btnMP4 = Button(
    principal,
    text='MP4',
    font=('Comic Sans MS', 10),
    fg='white',
    activeforeground='white',
    bg='#0F044F',
    activebackground="#0F044F",
    width=25,
    borderwidth=1,
    command=downloadVideo
)
btnMP4.place(x=255, y=130)

btnOpenAud = Button(
    principal,
    text='Ver Audios',
    font=('Comic Sans MS', 10),
    fg='white',
    activeforeground='white',
    bg='#212F3D',
    activebackground="#212F3D",
    width=25,
    borderwidth=1,
    command=openAudios
)
btnOpenAud.place(x=22, y=180)
btnOpenVid = Button(
    principal,
    text='Ver videos',
    font=('Comic Sans MS', 10),
    fg='white',
    activeforeground='white',
    bg='#212F3D',
    activebackground="#212F3D",
    width=25,
    borderwidth=1,
    command=openVideos
)
btnOpenVid.place(x=255, y=180)

principal.mainloop()

#* pip freeze > requirements.txt => Para generar en un txt las librerias que se deben instalar