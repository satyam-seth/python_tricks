import time
import pyautogui

pyautogui.hotkey('win', '4')
pyautogui.hotkey('ctrl', 'f')
pyautogui.hotkey('ctrl', 'a')
pyautogui.keyDown('backspace')
pyautogui.write('Contact Name')
pyautogui.keyDown('down')
pyautogui.keyDown('enter')

for _ in range(50):
    pyautogui.write('Hello world!')
    pyautogui.keyDown('enter')
    time.sleep(0.5)