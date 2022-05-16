from pyautogui import *
import pyautogui as pg
import time
import keyboard
import random

pg.FAILSAFE = True

time.sleep(2)

pg.moveTo(350, 200)
pg.click()
time.sleep(2)
    
while keyboard.is_pressed('q') == False:
    pyautogui.moveTo(200, 920)   # moves mouse to menu de chats
    time.sleep(0.5)
    pyautogui.scroll(-100000)   # scroll up 100000 "clicks"
    time.sleep(0.5)

