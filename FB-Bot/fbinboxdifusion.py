from pyautogui import *
import pyautogui as pg
import time
import keyboard
import random



pg.FAILSAFE = True



time.sleep(2)
pg.moveTo(680, 600)

    
while True:
    time.sleep(1)
    pg.moveTo(233, 890)
    time.sleep(0.5)
    pg.click()
    time.sleep(1)
    pg.moveTo(670, 942)
    time.sleep(2)
    if pg.pixelMatchesColor(670, 942, (245, 246, 247))== True:  #if it the account is not longer available or is blocked
        pg.moveTo(233, 890)
        time.sleep(0.5)
        pg.scroll(100)
    else:
        time.sleep(0.5)
        pg.click()
        time.sleep(1)
        pg.hotkey('ctrl', 'v') #having the text coppied
        time.sleep(1)
        pg.press('enter')
        time.sleep(0.5)
        pg.moveTo(1396, 978)
        time.sleep(0.5)
        pg.click()
        time.sleep(1.5)
        pg.write('fotomu0504x1')    #whatever the name of the pic to send
        time.sleep(0.5)
        pg.press('enter')    
        time.sleep(8)
        pg.moveTo(670, 942)
        time.sleep(0.5)
        pg.click()
        pg.press('enter')    
        time.sleep(2)
    
