''' Windows New Tab'''
## Parent window = Main Page
## Child window = secondary page (new tab), link clicked on from Main Page

# Using "window_handles"

## driver.window_handles -> store all open tabs in a list ("parentID", "childID")

# driver = webdriver.Chrome(executable_path = "C:\\Users\\volod\\Downloads\\chromedriver.exe")
# driver.get("https://the-internet.herokuapp.com/windows")

# driver.find_element_by_link_text("Click Here").click()

# childwindow = driver.window_handles[1]               #> Identifies NEW Open tabs. 0 is Main Page
# driver.switch_to.window(childwindow)              #> pass child window name to switch to another(Child) tab window
# print(driver.find_element_by_tag_name("h3").text)
##driver.close() 
# driver.switch_to.window(driver.window_handles[0])              #> Pass Parent window to switch back to Main window tab
# print(driver.find_element_by_tag_name("h3").text)
# assert "Opening a new window" == driver.find_element_by_tag_name("h3").text     #> If NO errors, ASSERT is Correct.
# time.sleep(10)