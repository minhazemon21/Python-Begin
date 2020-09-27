import pyautogui
import time
msg = 100
while msg > 0:
    time.sleep(1)
    pyautogui.typewrite('I love u sona.')
    time.sleep(1)
    pyautogui.press('enter')
    msg = msg - 1



