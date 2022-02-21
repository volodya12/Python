''' Alert '''
# https://chercher.tech/practice/practice-pop-ups-selenium-webdriver
# https://rahulshettyacademy.com/AutomationPractice/  -> Alerts

# pop-ups that appear on web (they are mostly java/javascript pop-ups)
# You must switch from HTML to Javascript DOM (pop-up)

driver.find_element_by_css_selector("#name").send_keys("option 3")
driver.find_element_by_id("alertbtn").click()

# To SWITCH, must create "alert" object/variable
# 'driver.switch_to.alert' must be in a Variable to work with JavaScript
# Switches to Alert popup which is in Javascript
alert = driver.switch_to.alert    
print(alert.text)

# Verify 'option 3' keyed inside box
alertText = alert.text
assert "option 3" in alertText   

# "accept" method will accept alert by clicking OK
alert.accept()
alert.dismiss()  # cancel alert 
------------------------------------
# Hide / Show Buttons 
# Its good practice to have "Assertions" for true/false

assert driver.find_element_by_id("displayed-text").is_displayed() # True or False
#print(driver.find_element_by_id("displayed-text").is_displayed()) # True or False
driver.find_element_by_id("hide-textbox").click()

assert not driver.find_element_by_id("displayed-text").is_displayed() # True or False
#print(driver.find_element_by_id("displayed-text").is_displayed()) # True or False

#===========================================================
''' Double Click / Right-Click / Alert/popup '''
driver = webdriver.Chrome(executable_path = "C:\\Users\\volod\\Downloads\\chromedriver.exe")
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

action = ActionChains(driver)
action.double_click(driver.find_element_by_id("double-click")).perform() 
action.context_click(driver.find_element_by_id("double-click")).perform() # Perform Right-Click 


# Switch to Javascript to perform action on Pop-up
alert = driver.switch_to.alert
alert.accept()
time.sleep(10)

