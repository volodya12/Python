# https://www.youtube.com/watch?v=j7VZsCCnptM

import os
from selenium import webdriver
# all these 'from' is for the 'WebDriverWait -> EC'
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #-> Expected Condition
# import Keyboard keys such: Alt, Shift, Ctrl, Numpad keys
from selenium.webdriver.common.keys import Keys

'''TIPS'''
# To View ALL Options from 'Import' such 'Keys' = Hightlight 'Keys' and press F12
# Ctrl + Space = drop down to view options

os.environ['PATH'] = "C:/Users/volod/Downloads"
driver = webdriver.Chrome()
driver.get("https://www.seleniumeasy.com/jenkins-tutorials")

driver.find_element_by_link_text("What is Jenkins and Use of it?").click()
driver.implicitly_wait(2)

'''----- Handle Popups ---'''

# To click 'No Thanks' on pop-up
# try/except function - if pop-up appears, it will click proper button, BUT pop-up may NOT appear.
try:
    no_button = driver.find_element_by_class_name('at-cm-no-button')
    no_button.click()
except:
    print('No pop-up occured')

sum1 = driver.find_element_by_id('sum1')
sum2 = driver.find_element_by_id('sum2')

# starting with 'Keys.<any Keyboard key can go here such Alt, Shift, F keys>'
sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5) #-> same as keying '15'
sum2.send_keys(15)
