import time
import pyautogui

while True:
    time.sleep(5)
    for i in range(50):
        pyautogui.moveTo(i*10,5)
    pyautogui.press('ctrl')
    for i in range(50):
        pyautogui.moveTo(5,(50-i)*10)
    pyautogui.hotkey('alt','tab')
    for i in range(2):
        time.sleep(2)
        pyautogui.hotkey('win','d')
    for i in range(2):
        time.sleep(2)
        pyautogui.press('win')