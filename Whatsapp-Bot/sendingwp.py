from pyautogui import *
import pyautogui as pg
import time
import keyboard
import random
import win32api, win32con


pg.FAILSAFE = True

vueltas = ''
vueltas = int(prompt(text='Cuantos numeros hay para mandar?', title='WpBot' , default=''))
###
##while True:
for i in range(vueltas):
    time.sleep(0.5)
    pg.moveTo(34, 220)
    time.sleep(0.5)
    pg.click()
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(0.5)
    pg.hotkey('ctrl', 'c')
    time.sleep(0.5)
    pg.hotkey('ctrl', '1')
    time.sleep(0.5)
    pg.moveTo(302, 52)
    time.sleep(0.5)
    pg.click()
    time.sleep(0.2)
    pg.click()
    time.sleep(0.2)
    pg.click()
    time.sleep(0.2)
    pg.press('delete')
    time.sleep(0.2)
    pg.write('https://api.whatsapp.com/send?phone=')
    time.sleep(0.5)
    pg.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(1.5)
    pg.press('left')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(3)
    #####ESCRIBIR MENSAJES#####
    if pg.pixelMatchesColor(1657, 1010, (42, 57, 66)) == True:
        pg.moveTo(1657, 1010)
        time.sleep(0.5)
        pg.click()
        pg.moveTo(1370, 1010)
        time.sleep(0.5)
        pg.click()
        pg.moveTo(1370, 945)
        time.sleep(0.5)
        pg.click()
        time.sleep(0.5)
        pg.moveTo(1423, 473)
        time.sleep(0.5)
        pg.click() 
        time.sleep(0.5)
        pg.write('"fotomu0504x2" "fotomu0504x1" ')
        time.sleep(0.5)
        pg.press('enter')
        time.sleep(3)
        pg.press('enter')
        time.sleep(1)
        pg.moveTo(557, 15)
        time.sleep(0.5)
        pg.click()
        time.sleep(0.5)
        pg.moveTo(430, 310)
        time.sleep(0.5)
        pg.click()
        time.sleep(0.5)
        pg.hotkey('ctrl', 'a')
        time.sleep(1)
        pg.hotkey('ctrl', 'c')
        time.sleep(1)
        pg.hotkey('alt', 'tab')
        time.sleep(1)
        pg.hotkey('ctrl', 'v')
        time.sleep(1)
        pg.press('enter')
    time.sleep(4)
    pg.moveTo(360, 15)    
    time.sleep(0.2)
    pg.click()
    time.sleep(0.5)
    pg.press('down')
    time.sleep(0.5)
exit()
     
    





    

    

    



