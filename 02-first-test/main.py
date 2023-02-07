import os
import pyautogui
import time
import subprocess
import pydirectinput
import win32api, win32con

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#pyautogui.FAILSAFE = False

#Params
xStartGame = 985
yStartGame = 570
sleepToStart = 8

xAcceptLaunch = 1366 / 2 - 100
yAceptyLaunch = 768 / 2 + 135

# Lauch MU app
os.startfile (r"MU Online.lnk")

time.sleep(sleepToStart)
pydirectinput.click(x=xStartGame, y=yStartGame, clicks=1, interval=0, button='left')

pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('tab')
pyautogui.keyUp('alt')
pydirectinput.click(x=xStartGame, y=yStartGame, clicks=1, interval=0, button='left')

time.sleep(30)

xServerButton = 519
yServerButton = 370

pydirectinput.moveTo(xServerButton, yServerButton)
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('tab')
pyautogui.keyUp('alt')
pydirectinput.moveTo(xServerButton, yServerButton)
leftClick()
time.sleep(1)
pydirectinput.moveTo(687, 473)

leftClick()
time.sleep(1)
pydirectinput.moveTo(687, 402)

# Credenciales

pydirectinput.press('enter')
time.sleep(3)
pydirectinput.moveTo(972, 180)
pydirectinput.moveTo(979, 670)
leftClick()


# Obtiene la posición del mouse en tiempo real
# while(True):
#     print(pydirectinput.position())
