import pyautogui
from time import sleep

pyautogui.press('win')
pyautogui.PAUSE = 3
pyautogui.write('firefox')
pyautogui.press("enter")
pyautogui.click(x=867, y=755)
pyautogui.hotkey("ctrl", 't')
pyautogui.write('google')
pyautogui.press('enter')

