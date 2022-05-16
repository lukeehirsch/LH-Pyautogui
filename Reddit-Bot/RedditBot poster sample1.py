if x.day ==25:
    action = confirm(text='Today is 25th, What do we do?', title='Reddit boii', buttons=['Post', 'Check'])
    sleep(1)
    
    pg.moveTo(125, 15)                                                                      
    pg.click()
    pg.click(1400,510)
    pg.moveTo(600, 383) 
    pg.click()
    sleep(0.5)
    pg.moveTo(639, 409) #open Submit tab
    pg.click()
    sleep(7) #loading
    pg.moveTo(pg.locateCenterOnScreen('rdlink.png', confidence = 0.8)) #finds button
    pg.click()
    pg.press('tab')
    pg.press('tab')
    pg.write(random.choice(EXAMPLETITLES), interval=0.05)
    pg.press('tab')
    pg.write('https://i.imgur.com/EXAMPLEIMG.jpg')
    pg.press('tab')
    pg.press('tab')
    pg.press('enter')        #BUTTON
    if action =='Post':
        pg.press('tab')
        pg.press('enter')   #POSTBUTTON
        time.sleep(2)
    pg.hotkey('ctrl','w')
    sleep(0.5)
    pg.press('enter')

    pg.moveTo(125, 15)                                                                          
    pg.click()
    pg.click(1400,510)
    pg.moveTo(600, 400) 
    pg.click()
    sleep(0.5)
    pg.moveTo(624, 428)
    pg.click()
    sleep(7) #loading
    pg.moveTo(pg.locateCenterOnScreen('rdlinkselected.png', confidence = 0.8)) #finds button
    pg.click()
    pg.press('tab')
    pg.write(random.choice(EXAMPLETITLES), interval=0.05)
    pg.press('tab')
    pg.write('https://i.imgur.com/EXAMPLEIMG.jpg')
    pg.press('tab')
    pg.press('tab')
    pg.press('enter')        #BUTTON
    if action =='Post':
        pg.press('tab')
        pg.press('enter')   #POSTBUTTON
        time.sleep(2)
    pg.hotkey('ctrl','w')
    sleep(0.5)
    pg.press('enter')

    pg.moveTo(125, 15)                                                                          
    pg.click()
    pg.click(1400,510)
    pg.moveTo(600, 414) #r/thiccertahnuthink
    pg.click()
    sleep(0.5)
    pg.moveTo(620, 441)
    pg.click()
    sleep(7) #loading
    pg.moveTo(pg.locateCenterOnScreen('rdlinkselected.png', confidence = 0.8)) #finds button
    pg.click()
    pg.press('tab')
    pg.write(random.choice(EXAMPLETITLES), interval=0.05)
    pg.press('tab')
    pg.write('https://i.imgur.com/EXAMPLEIMG.jpg')
    pg.press('tab')
    pg.press('tab')
    pg.press('enter')        #BUTTON
    pg.press('tab')
    pg.press('enter')       #FLAIRS
    pg.press('tab')
    pg.press('tab')
    pg.press('tab')
    pg.press('down')
    pg.press('tab')
    pg.press('enter')
    pg.click(981,503)
    pg.press('tab')
    pg.press('tab')
    pg.press('tab')
    if action =='Post':
        pg.press('tab')
        pg.press('enter')   #POSTBUTTON
        time.sleep(2)
    pg.hotkey('ctrl','w')
    sleep(0.5)
    pg.press('enter')

    pg.moveTo(125, 15)                                                                          
    pg.click()
    pg.click(1400,510)
    pg.moveTo(600, 430) 
    pg.click()
    sleep(0.5)
    pg.moveTo(630, 455)
    pg.click()
    sleep(7) #loading
    pg.moveTo(pg.locateCenterOnScreen('rdlink.png', confidence = 0.8)) #finds button
    pg.click()
    pg.press('tab')
    pg.press('tab')
    pg.write(random.choice(EXAMPLETITLES), interval=0.05)
    pg.press('tab')
    pg.write('https://i.imgur.com/EXAMPLEIMG.jpg')
    pg.press('tab')
    pg.press('tab')
    pg.press('enter')        #BUTTON
    if action =='Post':
        pg.press('tab')
        pg.press('enter')   #POSTBUTTON
        time.sleep(2)
    pg.hotkey('ctrl','w')
    sleep(0.5)
    pg.press('enter')

    pg.moveTo(125, 15)
    pg.click()
    pg.click(1400,510)
    pg.moveTo(588, 446)
    pg.click()
    sleep(0.5)
    pg.moveTo(650, 473) #link
    pg.click()
    sleep(7) #loads
    pg.moveTo(pg.locateCenterOnScreen('rdlink.png', confidence = 0.8)) #finds button
    pg.click()
    pg.press('tab')
    pg.press('tab')
    pg.write(random.choice(EXAMPLETITLES), interval=0.05)
    pg.press('tab')
    pg.write('https://i.imgur.com/EXAMPLEIMG.jpg')
    pg.press('tab')
    pg.press('tab')
    pg.press('enter')        #BUTTON
    if action =='Post':
        pg.press('tab')
        pg.press('enter')   #POSTBUTTON
        time.sleep(2)
    pg.hotkey('ctrl','w')   #close tab
    sleep(0.5)
    pg.press('enter')

    pg.moveTo(125, 15)                                                   
    pg.click()
    pg.click(1400,510)
    pg.moveTo(600, 625) 
    pg.click()
    sleep(0.5)
    pg.moveTo(640, 655) #link
    pg.click()
    sleep(7) #loads
    pg.moveTo(pg.locateCenterOnScreen('rdlinkselected.png', confidence = 0.8)) #finds button
    pg.click()
    pg.press('tab')
    pg.write(random.choice(EXAMPLETITLES), interval=0.05)  #title
    pg.press('tab')
    pg.write('https://i.imgur.com/EXAMPLEIMG.jpg')
    pg.press('tab')
    pg.press('tab')
    pg.press('enter')        #BUTTON
    if action =='Post':
        pg.press('tab')
        pg.press('enter')   #POSTBUTTON
        time.sleep(2)
    pg.hotkey('ctrl','w')   #close tab
    sleep(0.5)
    pg.press('enter')

    pg.moveTo(125, 15)
    pg.click()
    pg.click(1400,510)
    pg.moveTo(600, 643)     
    pg.click()
    sleep(0.5)
    pg.moveTo(640, 673) #link
    pg.click()
    sleep(7) #tarda en abrir la pagina
    pg.moveTo(pg.locateCenterOnScreen('rdlink.png', confidence = 0.8)) #finds button
    pg.click()
    pg.press('tab')
    pg.press('tab')
    pg.write(random.choice(EXAMPLETITLES), interval=0.05)  #title
    pg.press('tab')
    pg.write('https://i.imgur.com/EXAMPLEIMG.jpg')
    pg.press('tab')
    pg.press('tab')
    pg.press('enter')        #BUTTON
    if action =='Post':
        pg.press('tab')
        pg.press('enter')   #POSTBUTTON
        time.sleep(2)
    pg.hotkey('ctrl','w')   #close tab
    sleep(0.5)
    pg.press('enter')

    pg.moveTo(125, 15)
    pg.click()
    pg.click(1400,510)
    pg.moveTo(600, 660)   
    pg.click()
    sleep(0.5)
    pg.moveTo(640, 685) #link
    pg.click()
    sleep(7) #loads
    pg.moveTo(pg.locateCenterOnScreen('rdlinkselected.png', confidence = 0.8)) #finds button
    pg.click()
    pg.press('tab')
    pg.write(random.choice(EXAMPLETITLES), interval=0.05)  #title
    pg.press('tab')
    pg.write('https://i.imgur.com/EXAMPLEIMG.jpg')
    pg.press('tab')
    pg.press('enter')        #BUTTON
    if action =='Post':
        pg.press('tab')
        pg.press('enter')   #POSTBUTTON
        time.sleep(2)
    pg.hotkey('ctrl','w')   #close tab
    sleep(0.5)
    pg.press('enter')
