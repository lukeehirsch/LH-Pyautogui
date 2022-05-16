from pyautogui import *
import pyautogui as pg
from time import sleep

pg.FAILSAFE = True
pg.PAUSE = 0.7

if pg.confirm(text='Do we need to open set up?(Axie Marketplace and Google sheets)', title='Claim Bot', buttons=['YES', 'NO']) =='YES':   
#OPENS SET UP
    
#DESLOG
pg.click(66,1021)
pg.moveTo(pg.locateCenterOnScreen('logout.png', confidence=0.8))
pg.click()

loggeado = ''
loggeado = pg.confirm(text='Remember to be logged to Ronin', title='Claim Bot', buttons=['Done', 'Cancel'])
sleep(1)
if loggeado == 'Cancel':
    exit()
if loggeado == 'Done':
    time.sleep(1)
#ASK WHICH ACCOUNT IS READY TO CLAIM       
    if account == '1':
        #LOGS AND CONFIRM

    if account == '2':
        #LOGS AND CONFIRM

    if account == '3':
        #LOGS AND CONFIRM

        
    
##START CLAIM
        
pg.moveTo(pg.locateCenterOnScreen('claimtokens.png', confidence=0.8))
pg.click()
pg.hotkey('ctrl','t')
pg.write('https://scatter.roninchain.com/')
pg.press('enter')

#CLAIMS SLP HERE

pg.hotkey('ctrl','2') #CHANGES TAB TO SHEETS
time.sleep(1)
#GOES TO CELLS AND COMPLETE INPUTS
sleep(0.5)
pg.press('enter')
pg.hotkey('ctrl','v')
time.sleep(1)
#PROCEDS TO WRITE THE SCATTER FILE WITH ADRESSES AND AMMOUNTS
pg.moveTo(pg.locateCenterOnScreen('approveslp.png', confidence=0.8))
pg.click()
#CONFIRMS TRANSACTIONS

exit()
