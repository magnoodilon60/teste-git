#requeriments
#instalar o pytube
#pip install pytube

from pytube import YouTube
link = input("Insira a URL do Video: ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()

