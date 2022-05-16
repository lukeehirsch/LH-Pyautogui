from pyautogui import *
import pyautogui as pg
from time import sleep
import keyboard
import random
import win32api, win32con
import datetime


pg.FAILSAFE = True
pg.PAUSE = 1


vueltas = ''
vueltas = int(prompt(text='How many times do we do this? 1,2,3,... // exit', title='ImgToTextBot' , default=''))
if vueltas =="exit":
    exit()
for i in range (vueltas):
    sleep(1)
    pg.moveTo(370, 380)
    pg.click(button='right')
    pg.moveTo(482, 441)
    pg.press('enter')
    time.sleep(12)      #loads document
    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'c')
    pg.hotkey('ctrl', 'w')
    pg.hotkey('ctrl', '2')
    pg.hotkey('ctrl', 'v')
    pg.press('right')
    pg.hotkey('ctrl', '1')
    pg.moveTo(370, 380)
    pg.click()
    pg.press('delete')
    pg.moveTo(370, 380)
    pg.click()
    pg.press('delete')
exit()


