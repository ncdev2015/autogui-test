import os
import pyautogui
import time
import subprocess
import pydirectinput

#pyautogui.FAILSAFE = False

#Params
xStartGame = 985
yStartGame = 570
sleepToStart = 5

xAcceptLaunch = 1366 / 2 - 100
yAceptyLaunch = 768 / 2 + 135

# Lauch MU app
os.startfile (r"MU Online.lnk")



time.sleep(sleepToStart)
pydirectinput.click(x=xStartGame, y=yStartGame, clicks=1, interval=0, button='left')

time.sleep(35)
pydirectinput.moveTo(519, 370)
pydirectinput.moveTo(100, 150)
#pydirectinput.click(x=xStartGame, y=yStartGame, clicks=1, interval=0, button='left')

# Obtiene la posición del mouse en tiempo real
while(True):
    print(pydirectinput.position())
