from pyautogui import *
import pyautogui as pg
from time import sleep
import cv2

pg.FAILSAFE = True
pg.PAUSE = 0.7

sleep(2)
pg.press('winleft')
pg.write('chrome', interval =0.15)
pg.press('enter')
sleep(1)
pg.hotkey('winleft', 'up')
pg.write('https://www.hospitalitaliano.org.ar/#!/home/principal')
pg.press('enter')
sleep(5)

pg.moveTo(pg.locateCenterOnScreen('portaldepacientes.png', confidence = 0.8))
pg.click()
sleep(5)

pg.moveTo(pg.locateCenterOnScreen('ingresarportal.png', confidence = 0.8))
pg.click()
sleep(5)

pg.moveTo(pg.locateCenterOnScreen('turnosportal.png', confidence = 0.8))
pg.click()
sleep(1)
pg.move(0,40)
pg.click()
sleep(1)


pg.moveTo(pg.locateCenterOnScreen('continuarportal.png', confidence = 0.8))
pg.click()
sleep(3)

pg.moveTo(pg.locateCenterOnScreen('apellidono.png', confidence = 0.8))
pg.click()
sleep(1)

pg.moveTo(pg.locateCenterOnScreen('ingreseespecialidad.png', confidence = 0.8))
pg.click()
sleep(1)

pg.write('oftalmologia')
sleep(1)
pg.press('down')
pg.press('enter')

pg.moveTo(pg.locateCenterOnScreen('lugardeatencion.png', confidence = 0.8))
pg.click()
sleep(1)


pg.write('central')
pg.press('enter')
pg.write('caballito')
pg.press('enter')
pg.write('belgrano')
pg.press('enter')
pg.write('villa')
pg.press('enter')
pg.write('villa')
pg.press('enter')
pg.write('particulares')
pg.press('enter')

pg.moveTo(pg.locateCenterOnScreen('buscarturnos.png', confidence = 0.8))
pg.click()
sleep(1)

exit()
