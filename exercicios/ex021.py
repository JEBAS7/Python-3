# import winsound

# O Windows vai ler e reproduzir o som de forma nativa instantaneamente
# winsound.PlaySound('ex021.wav', winsound.SND_FILENAME)

from playsound import playsound

# Ela toca o áudio de forma nativa e segura
playsound('ex021.mp3')


