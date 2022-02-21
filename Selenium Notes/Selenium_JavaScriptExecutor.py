''' JavaScript HTML DOM (JavaScript code in Selenium) '''

### DOM Method by JavaScript -> allows to access ALL objects/elements on the web page (Document Object Model)
### From Inspect -> Console -> type: document.get<will get sooo much diff elements>
### Selenium have method to execute JavaScript code 
### JavaScript DOM (Methods) is rarely used but ONLY used if SELENIUM CANT handle it.

# driver = webdriver.Chrome(executable_path = "C:\\Users\\volod\\Downloads\\chromedriver.exe")
# driver.get("https://rahulshettyacademy.com/angularpractice/")
# 
# driver.find_element_by_name("name").send_keys("hello")
# print(driver.find_element_by_name("name").text)             #> will NOT print text "hello"
# print(driver.find_element_by_name("name").get_attribute("value"))    #> Will print text "hello"
# 
# ## Now, execute in JS DOM (javascript code)
# ## 'execute_script' is class for JavaScript code

# print(driver.execute_script('return document.getElementsByName("name")[0].value'))    #> Prints "hello"
#                               ^prints text in console                      ^method that prints text from textbox
# shopButton = driver.find_element_by_css_selector("a[href*='shop']")

##/ 'arguments' -> first parm, []->defines which argument to execute (0 is 'shopButton')
##/ 'shopButon' -> is a Variable.
##/ '.click()'  -> is a method/action
##/ ';'         -> ends javascript code

# driver.execute_script("arguments[0].click();",shopButton)                         

''' Scrolling / Scroll bar -> NOT supported by Selenium '''
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")   #> ';' indicates END step
# time.sleep(5)