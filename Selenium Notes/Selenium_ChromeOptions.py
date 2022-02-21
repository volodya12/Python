'''ChromeOptions (type of class) - things can be configured to Chrome before running it '''

ActionChains(driver)                                  -> does variety of actions (mouse over, double click and more)
        use method .Perform() to complete action.
childwindow = driver.window_handles                   -> identifies window tabs
driver.switch_to.default_content()                    -> switches back to HTML tags
driver.switch_to.window(childwindow)                  -> switches to Specific Tab
time.sleep(5)                                         -> waits 5 seconds
Assert                                                -> verifies things          
driver.switch_to.frame("mce_0_ifr")                   -> switches to Frame tag from HTML
driver.close()                          -> close Window
driver.quit()                           -> Close all Windows
driver.back()                           -> navigates back
driver.refresh()                        -> refreshes window
driver.maximize_window()
driver.minimize_window()
driver.switch_to.frame("mce_0_ifr")     -> switches from HTML to frame tag (iframe)
driver.switch_to.default_content()      -> switches back to HTML tags
driver.execute_script()                 -> executes only JavaScript commands/code 
ChromeOptions (type of Class)           -> write instructions to configure Chrome on HOW it should be Invoked.

### Google for more Selenium.webdriver.ChromeOptions 
### Browser headless - when code is executed, you wont see in Front-End. Browser is not Invoked. You only see the results. (faster and less memory space)
### Browser Head mode - User can see Browser Invoking as code executes. 

### Websites with SSL Certification (Click Advanced -> "Proceed at your own risk") - Selenium calls them "Certification errors"
#       - Selenium does NOT ignore them, It will Fail test. 
### Add as many "ChromeOptions" needed

## from selenium.webdriver import ActionChains

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--start-maximized")  #> windows will start at Max size
# chrome_options.add_argument("headless")           #> No Browser will display, only results in Terminal
# chrome_options.add_argument("--ignore-certificate-errors")  #> ignores SSL certificates that makes you click to proceed at your own risk.

##/ Add "options=chrome_options" to Chrome browser
##/ ALL configs in 'chrome_options' is now passed to 'executable_path' argument, to Chrome Browser
# driver = webdriver.Chrome(executable_path = "C:\\Users\\volod\\Downloads\\chromedriver.exe", options=chrome_options)  
# driver.get("https://rahulshettyacademy.com/angularpractice/")

# print(driver.title)  #> prints title of the web (ProtoCommerce)