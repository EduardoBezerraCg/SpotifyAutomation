import time

import pyautogui
from time import sleep

import subprocess

# #Abrindo o spotify
# #Lembrar de procurar pelo executavel
open_spotify = r'C:\Users\Eduardo Bezerra\AppData\Roaming\Spotify\spotify.exe'
subprocess.Popen(open_spotify)
time.sleep(5)

#Selecionar a musica que vc quer:
search_msc = input(str("Qual musica gostaria de ouvir? "))
pyautogui.click(112, 128, duration=2)
pyautogui.click(478, 73, duration=0.5)
pyautogui.write(search_msc)
time.sleep(1.00)
pyautogui.click(729,411, duration=0.5)


# pyautogui.click(1210,115, duration=1)
# pyautogui.write('Sertanojo Nutela')
# pyautogui.click(1191,59, duration=1)
