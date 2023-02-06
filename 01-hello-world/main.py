# Install PyAutoGUI
# pip install pyautogui

import pyautogui

print(pyautogui.position())
print(pyautogui.size())
print(pyautogui.onScreen(1920, 1080))
pyautogui.moveTo(800, 600, duration=10)
pyautogui.moveRel(10, 0, duration=5)
pyautogui.typewrite('Hello world!\n', interval=1)