# https://www.youtube.com/watch?v=j7VZsCCnptM

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #-> Expected Condition

os.environ['PATH'] += r"C:\\Users\\volod\\Downloads\\chromedriver.exe"
driver = webdriver.Chrome()
driver.get("https://www.seleniumeasy.com/jenkins-tutorials")

progress = driver.get_element_by_class_name('node')
print(f"{progress.text == 'Completed!'}")  # prints in format

driver.find_element_by_link_text("What is Jenkins and Use of it?").click()
driver.implicitly_wait(2)

## 'progress-label' tag for Download bar
progress_element = driver.find_element_by_class_name('progress-label') 
## A Boolean statement, comparison, when progress bar completes it should say 'Completed!' 
print(f"{progress_element.text == 'Completed!'}")  -> indicates 'False'

## Task here is, write a code to wait for download bar to complete sucessful, show no errors, instead of 'False'
## Writing condition for WAIT
## (driver, <seconds>) -> wait approx 30 seconds for downloading bar to complete
## After this code runs, it will complete and return no output, as if contition is True
WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        # accepts two arguments: Elements filtration and Expected text
        (By.CLASS_NAME, 'progress-label'), 'Complete!'
    )
)