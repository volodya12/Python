from _typeshed import FileDescriptor
from os import link, name, waitpid
from typing import OrderedDict
import time
from selenium.webdriver import ActionChains
from selenium import webdriver

# Relative XPath = //label[contains(text()),'Password')] - shortcut (better version, better performance)
# Absolute XPath = /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/form[1]/label[1] - full path from beginning

''' Web links to practice Selenium automation '''
#### Udemy -> Selenium Webdriver with PYTHON from Scratch + Frameworks
# https://rahulshettyacademy.com/dropdownsPractise/ ---> practice drop downs 
# https://rahulshettyacademy.com/#/practice-project  ---> other project pages to practice on
# https://login.salesforce.com/  
# https://rahulshettyacademy.com/seleniumPractise/#/
# https://the-internet.herokuapp.com/ -> Frames and more (https://the-internet.herokuapp.com/iframe)
'''CSS Selector Functions'''
# https://www.w3schools.com/cssref/css_selectors.asp
'''XPath Functions'''
# https://www.w3schools.com/xml/xpath_syntax.asp

'''TIPS'''
# To View ALL Options from 'Import' such 'Keys' = Hightlight 'Keys' and press F12
# Ctrl + Space = drop down to view options
# CSS Selector and XPath replaces many tags which can be invoked with. Replaces tags like id, class, name, and more.
# Use 'ChroPath' extension, makes it very easy to see tags as you look for them. Activate it from "Elements" tab after Inspect
# XPath vs CSS Selector = CSS does NOT have the ability to Traverse (going from one tag up/down to another)
#                                = XPath HAVE ability to Traverse (jump from one tag down/up to another tag)(div/label)
# From Inspect -> Console -> type: document.<will get sooo much diff elements>
# Selenium have method to execute JavaScript code 
# JavaScript DOM (Methods) is rarely used but ONLY used if SELENIUM CANT handle it.
# Selenium DONT have ability to SCROLL, JavaScript Does

'''repeat lesson 10 (Selenium Webdriver with Python from Scratch + Frameworks) udemy '''

'''Selenium works only with HTML tags'''
'''Automation usually runs fast when testing website. To SLOW things down, must use "Debugger" which you manually set a checkpoint on very left, right before text.
Then you would execute entire script and Test will stop at "debug" checkpoint, from there, you can test, Step-by-step'''

'''If red line appears underneath the Object, and it don't need to be defined as variable.
Navigate over it, and Click "Import <whatever package> associated with Object'''

## driver = webdriver.Firefox(executable_path="get path to geckodriver.exe")
## driver.get("https://rahulshettyacademy.com")

#### Internet Explorer web browser
## driver = webdriver.Ie(executable_path="get path to IEDriverServer.exe")
## driver.get("https://rahulshettyacademy.com")

## this opens Chrome web driver
driver = webdriver.Chrome(executable_path="C:\\Users\\volod\\Downloads\\chromedriver.exe")
## this opens specific URL
driver.get("https://rahulshettyacademy.com")

=================================================================
## show title of web page
print(driver.title)
print(driver.current_url)
## Verifies that Page user landed on is Correct, and not redirected per cyber attack 
print(driver.current_url)
## Navigates to different web site
driver.get("http://rahulshettyacademy.com/AutomationPractice")
## Come back to previous page (hit back button)
driver.back()
## Refreshes Web page
driver.refresh()
driver.maximize_window()
driver.minimize_window()
#
## Close Web Driver (chrome)
driver.close()
####### Closes multiple (all) Chrome windows
driver.quit()

# driver = webdriver.Chrome(executable_path="C:\\Users\\volod\\Downloads\\chromedriver.exe")
# driver.get("https://rahulshettyacademy.com/angularpractice/")
-------------------------------------
assert print(driver.title) == "http://rahulshettyacademy.com/AutomationPractice"
If assert is NOT true, Code will fail with error
If assert PASS no errors will display and Code runs Smooth
============================================================

IN Console:
                https://rahulshettyacademy.com/angularpractice/
xpath = $x("input[class*='input']")  = find_element_by_xpath("input[class*='input']") 
xpath = $x("//input[@type='submit']")  = find_element_by_xpath("//input[@type='submit']")
xpath = $x("//*[contains(@class,'alert-success']") = find_element_by_xpath_selector("//*[contains(@class,'alert-success']")
xpath = find_element_by_xpath("//a[text()='Cancel']").Click() -> 'a' is tagname
xpath = find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']")
xpath works well with tag "div" 

css = $("input[name='name']")          = find_element_by_css_selector("input[name='name']")
css = $("div[class*='alert-success']") = find_element_by_css_selector("[class*='alert-success']")
                        
                        (https://login.salesforce.com/)
css = $("input#username")  = find_element_by_css_selector("input#username") 
css = $("#username") =       find_element_by_css_selector("#username") -> if shows as 'id' tag name -> can be used as CSS selector 
css = $("input.password")  = find_element_by_css_selector("input.password")  -> Valid attribute of class
                        (https://rahulshettyacademy.com/seleniumPractise/) -> after items added to cart, proceed to checkout. Discount amount title
css = $(".discountAmt") = find_element_by_css_selector(".discountAmt")   -> valid attribute of class (span is tag name (optional))
css = $("p.product-name") = find_element_by_css_selector("p.product-name") -> 'p' is tag for title 'Product Name' within cart 

## If "print(driver.find_element_by_name("name").text)" -> Won't display text as suppose to, use "get_attribute" method.
## driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").get_attribute("value") #> will show text in 'Name' field 

#==============================================
### Type of Tags

# name = find_element_by_name("name")
# id = find_element_by_id
# className = find_element_by_class_name("alert-success")
# linkText = if anchor <a> is present, may use actual link name or <a href ...</a> -> valid as linkText
# tagName = actual tag name ("h3")
# if tag name is Value = get_attribute('value') == 'valueTag'

'''---Parent to Child tags  ->  (https://login.salesforce.com/)'''
# if Child tags class, id, other tag is dymanic (always changing), then start with Parent tag (div or something else)
XPATH:
$x("//div[@id='usernamegroup']")  -> parent
$x("//div[@id='usernamegroup']/label")  -> accessing Child thru tag "label" with (/)
CSS:
$("div[id='usernamegroup']")  -> parent
$("div[id='usernamegroup'] label")  -> accessing Child thru tag "label" with (space)

'''---GrandParents to Parent to Child tags  ->  (https://login.salesforce.com/)'''
# if Parent tags class, id, other tag is dymanic (always changing), then start with Grand Parent tag (div or form ....)
XPATH: (GrandParent to Parent to Child)
$x("//form[@name='login']/div[1]")  -> (form)GrandParent/Parent -> careful, few elements may be found 
#   div[1] -> identifies the first <div> tag (index)
$x("//form[@name='login']/div[1]/label") -> obtaining "Username" text. It is located INSIDE of Parent tag.
# print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
CSS: (GrandParent to Child)
$("form[name='login'] label:nth-child(3)")  -> obtaining "Password" text. It is located OUTSIDE of Parent tag.
# print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)
------------------
### Asterisk
//tagname*[@attribute='value']  asterisk is optional - represents any tag name

######### Locators: ################
# id -         find_element_by_id
# name -       find_element_by_name
# xpath -      find_element_by_xpath
# css -        find_element_by_css_selector
# class name - find_element_by_class_name
# link text -  find_element_by_link_text
# tag name -   find_element_by_tag_name("h3") -> actual tag name

''' ------- Different way of Coding ------------ '''
### This is prep
def print_hi(name):
    print(f'Hi, {name}')

## This is execution code (can be executed within different file.py by importing Prep from filename) -> look into "run.py"
if __name__ == '__main__':
    print_hi('PyCharm')

#--------------------------------------------------------------------------
''' CSS Syntax '''
# element_by_css_selector("tagname[attribute='value']") - CSS can read this syntax
#       
#           <tagname> is optional (not required in Console. Can do $("[name='name']")
#           input[name='name'] or input[required type='text'] - will only work if its unique and other fields don't have same "required type" as text.

#    Console = $("input[name='name']") -> hit Enter, links should appear identifying proper fields of Name='name'
#           If there are two elements with "name" value, ONLY first-one will be used. NOT second, or third.

''' XPath Syntax '''
# element_by_xpath("//tagname[@attribute='value']")
#    
#       //input[@type='submit']       -> "input" tagname is optional
#    
#    Console = $x("//input[@type='submit']")

''' Sends keys into field, where keys are entered '''
## action.context_click(driver.find_element_by_id("double-click")).perform() ------> Does Right-click
#   - requires import and ActionChains()
# print(driver.find_element_by_id("display-text").is_Displayed())  ----------------> True/False
# print(driver.find_element_by_id("display-text").is_Selected())  ----------------> True/False
## To Pass Assertion... in False statement
#   - assert not driver.find_element_by_id("displayed-text").is_displayed() #> will PASS cuz of 'assert not' - opposite of True
# driver.find_element_by_id("exampleCheck1").clear()       -------------------------> Clears the field
# driver.find_element_by_name("name").send_keys("Kyle Smith")       ----------------> user keys into input field
# driver.find_element_by_name("email").send_keys("kylesmith@yahoo.com")
# driver.find_element_by_id("exampleInputPassword1").send_keys("How are you my dear")
# driver.find_element_by_id("exampleCheck1").click()       -------------------------> user Clicks on Button
# driver.find_element_by_css_selector("input[name='name']").click()
# driver.find_element_by_css_selector(".password").clear() ----------------------> clears the field
# driver.find_element_by_xpath("//input[@type='submit']").click()
# driver.find_element_by_class_name("alert-success").text ------------------------> will get you text only
# print(driver.find_element_by_class_name("alert-success").text) ------------------------> will PRINT text onto terminal
# driver.find_element_by_link_text("Forgot Your Password?").Click()  -> User Clicks on Link
#           this object will only work if anchor '<a' is present for that link

'''--- Create Xpath via Text'''
# Alternative of linktext
# works in xpath only
'''<a> tag name'''
# must have anchor of <a> 
# "text" won't appear as an attribute like "class" or "type" or "id" and so on. It will be wrapped up in <a .... blah blah ....>Forgot Your Password?</a>

# //tagname[text()='xxx']
# Console -> $x("//a[text()='Forgot Your Password']")
# driver.find_element_by_xpath("//a[text()='Forgot Your Password']").Click() -> 'a' is tagname

''' Customized CSS Syntax '''
## Classes:If you see this:
## Classes usually seperated by space.

## <div class="alert alert-success alert-dismissible"> -> spaces in between keyword, that means that 'div' has three classes.

# Console -> $("div[class*='alert-success']")  --------------------------------> since there are many values per Class, * indicates all class values
# driver.find_element_by_class_name("alert-success").text
### OR CSS
# driver.find_element_by_css_selector("[class*='alert-success']")

''' Customized CSS Syntax '''
# tagname[attribute*='value']
# ex: dev[class*='alert-me']

###### Prints the outcome to the Terminal
# print(driver.find_element_by_class_name("alert_success").text)
    # prints("Success! The Form has been submitted successfully!")
    # If many Classes exist for same object, use class this way
        # $("input[class*='alert-success']")   adding asterick * 

''' Generating CSS from ID '''
# https://login.salesforce.com/

# IF <input class = "username wide w2"> for particular input Field
# use tag id  
#     $('#username') -> the input from inspection of website should highlight
# driver.find_element_by_by_css_selector("#username").send_keys("Vlad")
#                  
#                    $("input[id='username']") -> in Console with tag name
#                    $('#username') -----------> in Console Without tag name

''' Generating CSS from ClassName '''
# tagname.className
#     console -> $(".password") 
# driver.find_element_by_css_selector(".password").send_keys("love")
# driver.find_element_by_css_selector(".password").clear()

''' Customized XPath Syntax '''
# //tagname*[@attribute='value']  astericks is optional - represents any tag name
# //div*[@type='submit']

''' XPath '''
# Console -> $x("//*[contains(@class,'alert-success']")
# find_element_by_xpath("//*[contains(@class,'alert-success']")

''' For LinkText '''
# Inspect -> choose: "Forgot your Password?" -> the anchor should be "a" (<a id=... >)
# driver.find_element_by_link_text("Forgot Your Password?").Click()  -> User Clicks on Link
#           this object will only work if anchor '<a' is present for that link

'''--------------------Static Drop Downs -------------'''
# https://rahulshettyacademy.com/angularpractice/

## driver = webdriver.Firefox(executable_path="get path to geckodriver.exe")
## driver.get("https://rahulshettyacademy.com/angularpractice/")

# "select class" provides the methods to handle options for dropdown

# dropdown = select(driver.find_element_by_id("exampleFormControlSelect1"))
#### Several ways to select option from DropDown
# dropdown.select_by_visible_text("Female") -> by text
# dropdown.select_by_index(0) -> by index
# dropdown.select_by_value("Female")  -> by "value" located within the field

'''------------------ User Input Drop Down (dynamic) ---------------'''
# import time
# from selenium import webdriver
# driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

# driver.find_element_by_id("autosuggest").send_keys("ind")   ---------> after typing "ind", dropdown options will display
# time.sleep(2)     -----> will wait for 2 seconds to load dropdown options
# countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
## Since there are 3 options displayed for keyword "ind", we are iterating thru those options, when it hits the one we need "india", it will click on it.
# print(len(countries))     -> gives count of how many countries listed under "ind" keyword
# for country in countries:
#    if country.text == "india":     --> looking for match "india"
#        country.click()             -> once match found, Click on it
#        break                      -> this will Abrupt the Loop cuz we are done searching for right option

# print(driver.find_element_by_id("autosuggest").text)  -> this sometimes may work as verification to see what "text" is present on "autosuggest" field (but in this case, it returns as blank )
## 'get_attribute' gets and stores the value from 'autosuggest' field

# assert (driver.find_element_by_id("autosuggest").get_attribute('value') == 'India'  

'''------------------ Assertions ----------------'''
# driver.find_element_by_xpath("//input[@type='submit']").click()      ---> click botton "Submit" and Success message will appear
# message = driver.find_element_by_class_name("alert_success").text
# assert "success" in message      -> this runs assert function, with keyword 'success' to confirm variable 'message' has passed

# assert "success" == message

'''--------------------- Check Box ---------------'''
# https://rahulshettyacademy.com/AutomationPractice/
## IN this practice, we want to check ALL boxes. For this, we need to inspect filepath and find common Attribute In this case, its "type="checkbox"

# driver = webdriver.Firefox(executable_path="get path to geckodriver.exe")
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# //input[@type='checkbox']

# checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
# print(len(checkboxes))   -> gives count of how many checkboxes in "type=checkbox" attribute (3)

# for i in checkboxes:
#    i.click()       --> this will click all checkboxes on that page in (type=checkbox) attribute
#    assert.i.is_selected()    -> this asserts that all 3 checkboxes are selected 
'''if you want to select checkbox 'option 2'''
# for i in checkboxes:
#    print(i.get_attribute("value"))  -> this will print how "value" for checkboxes will display in terminal (good info for you)(then, "print" may be removed)
#    if i.get_attribute("value") == "option2":
#       i.click()       
#       assert i.is_selected()    

# Above explains, Loop thru all attributes containing "value" and print them in Terminal.

'''----- RadioButtons ------ CANNOT be selected all at once, they are not meant for that'''
# radiobutton = drive.find_elements_by_name("radioButton")
## Dont need to use For LOOP. Can use "Index"

#radiobutton = driver.find_elements_by_xpath("//input[@type='radio']")
#radiobutton[2].click()
#assert radiobutton[2].is_selected()   -> verify button selected

'''deal with pop-ups that appear on web (they are mostly java/javascript pop-ups) -- Contains one OK button'''
## tag name is #name (in CSS)
## all pop-ups are in java/javascript mode. 
## "driver" is only used in HTML
## You must switch HTML driver to javascript pop-up

# textValidate = "option 3"                               -------> will later help to validate Assertion of this text
# driver.find_element_by_css_selector("#name").send_keys("option 3")
# driver.find_element_by_id("alertbtn").click()

## to SWITCH, must create "alert" object/variable
# alert = driver.switch_to.alert      ---------------> this switches to alert() pop-up which written in javascript

## Prints text on the Alert pop-up
# print(alert.text)

## now, remove "print(alert.text)" and give it a variable to do assertion later in test
# alertText = alert.text
# assert textValidate in alertText    ----> if test passes, assert is correct, if fail, assert failed.

## "accept" method will accept alert by clicking OK
# alert.accept()
'''------------------ pop-up -- Contains two OK and Cancel button'''
## To Display TWO button Alert, Click "Confirm" button on web
## Clicks "Cancel" button on Alert popup
# alert.dismiss()
'''---------------------- WAITS function - Implicit/Explicit wait ---------------------- section 12:52-53 udemy'''
## implicit_wait() = it is Global wait, means it applies to entire code when mentioned once
##       It will wait 5 seconds until object is loaded. If object loads quickly, it will auto resume.
##       If object will NOT show at all, test resumes after 5 seconds.
##       USE Implicit_wait if entire application/web is huge and lots of data need time to load on page.
##       If each page is using about 3 seconds to load, Implicit wait is way to go.
## time.sleep(4) = wait function that needs ("Import time")
## time.sleep(<amountOfSeconds>) pauses test for few seconds using time class- (part of python, not selenium)

#driver = webdriver.chrome(executable_path="c:\\chromedriver.ext")
### Globaly (applies to every screen on web, waits 5 seconds)
#driver.implicit_wait(5)
#driver.get("https://rahulshettyacademy.com/seleniumPractise/")
### selects class name for input field "search_keyword"
#driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
#time.sleep(4)
### gives count of result show for keyword "ber"
#count = len(driver.find_element_by_xpath("//div[@class='products']/div"))
### varifying that it shows 3 results
#assert count == 3

#buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
#for allBut in buttons:
#    allBut.click()       --> Clicks all buttons (which adds product to the cart on web)

### Clicks on Cart icon (which is an image)
#driver.find_element_by_css_selector("img[alt='Cart']").click()
### After items added to Cart, Clicks on "proceed to checkout"
#driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
### enter Promo Code
#driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
### Clicks on Apply button
#driver.find_element_by_css_selector(".promoBtn").click()
### Print text in Terminal that promo has been applied
#print(driver.find_element_by_css_selector("span.promoInfo").text()

'''--- Explicit_wait ---'''
### Use Explicit_wait when specific page takes a while to load WHILE entire application/web is quick to load.
### Used to target only specific element
### You can put "Explicit_wait" for this specific "promoCode" element
### Package that needs to be imported for this Explicit wait function
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_condition as EC

### "WebDriverWait" object takes TWO arguments (driver, seconds)
#wait = WebDriverWait(driver, 5)
### this saying, i want to wait until "ClASS_NAME, promoCode" is present. 
#wait.until(expected_conditions.presence_of_element_located(By.CLASS_NAME, "promoCode"))
#driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")

#wait.until(expected_conditions.<varias methods to choose from>))
#                                alert_is_present
#                                presence_of_element_located(By.CSS_SELECTOR, "span.promoInfo")

#===========================================================================Continuation
'''From Child to GrandParent'''
## :: double semicolon provides path FROM CHILD to Parent and to GrandParent (if there are two 'div' tags)
## :: makes you go UP in tags
## going from Child to GrandParent
#driver.find_element_by_xpath("//div[@class='product-action']/button/parent::div/parent::div").click()

## This is verification, in a way, check to make sure correct 'add to cart' button is click and matches whats inside the 'Cart'
## Loop go thru products, will find button from 'product-action' class tag, SEE the text and Click the 'add to cart' button.
#for i in buttons:
#    print(i.find_element_by_xpath("parent::div/parent::div/h4").text)   #-> this is sort of verification to print product Name the one Clicked.
#    i.click()
=============================================
==================================================
from selenium.webdriver import ActionChains

Useful functions:
driver.get("website_here")

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

=======================================================================
=======================================================================

#driver = webdriver.Chrome(executable_path="C:\\Users\\volod\\Downloads\\chromedriver.exe")
#driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

#driver.find_element_by_id("autosuggest").send_keys("ind")
#time.sleep(2)

#countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")

#for country in countries:
#    if country.text == "India":
#        country.click()
#        break

#print(driver.find_element_by_id("autosuggest").text)
#assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"
=====================================================================
## Task: Do the comparison between page 1 (product title) vs page 2 (product title)

#list = []
#list2 = []

#page1 = driver.find_element_by_xpath("parent::div/parent::div/h4").text
#page2 = driver.find_element_by_css_selector("p.product-name")

#for i in page1:
#    list.append(i.text)            #> for every title in 'h4', append(add) to 'list' as text
#print(list)                        #> prints to terminal

#for b in page2:
#    list2.append(b.text)           #> for every title in 'h4', append(add) to 'list2' as text
#print(list2)                       #> prints to Terminal

#assert list == list2               #> this asserts that two lists from two different pages are same.
                                    # if error received, 'assert' statement failed, otherwise it passes if no errors
#========================================================================
## Task: Page 2 - Where discount promo is being applied, assert "Total After Discount" amount before promo vs "Total After Discount" amount after Promo
##              Apply assertion and After Promo should be Less Than Before Promo

#beforeDiscount = driver.find_element_by_css_selector(".discountAmt").text
#afterDiscount = driver.find_element_by_css_selector(".discountAmt").text

#assert int(afterDiscount) < int(beforeDiscount)      #> must be converted to 'int' otherwise it will read as String (text)
#or
#assert float(afterDiscount) < float(beforeDiscount)      #> must be converted to 'float' otherwise it will read as String (text)
                                                        # cuz float represents Decimal
#=========================================================================
## Task: Page 2 - Verify the amount of each product matches 'Total Amount'

## For this tag 'p.amount', will receive 6 results. Instead we need only 3. Start with Parent/grandparent
## If all Parents are same <td, td, td>... start with GrandParent <tr>
#productAmount = driver.find_element_by_xpath("//tr/td[5]/p").text

#for i in productAmount:
#    sum = 0 + (int(productAmount.text))      #32+48+60
#print(sum)

#totalAmount = driver.find_element_by_css_selector(".totAmt").text
#or
#totalAmount = int(driver.find_element_by_css_selector(".totAmt").text)   #> convert to INT right away
#assert float(productAmount) == float(totalAmount)

'''check if this code will work (similar to above)'''
#productAmount = int(driver.find_element_by_xpath("//tr/td[5]/p").text)
#totalAmount = int(driver.find_element_by_css_selector(".totAmt"))

#for i in productAmount:
#	sum = 0 + int(productAmount.text)
#print(sum)
#assert int(totalAmount) == int(productAmount)
#================================================================================
''' Click to open New Tab'''
## Parent window = Main Page
## Child window = secondary page (new tab), link clicked on from Main Page

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

#================================================================================
''' 62. tags: iframe, frameset, frame '''
### Selenium only works with HTML tags

# driver.get("https://the-internet.herokuapp.com/iframe")
# 
# driver.switch_to.frame("mce_0_ifr")
# driver.find_element_by_css_selector("#tinymce").clear()
# driver.find_element_by_css_selector("#tinymce").send_keys("Hello World")
# 
# driver.switch_to.default_content()  #> switches back to HTML tags
# print(driver.find_element_by_tag_name("h3").text)

#================================================================================
''' Mouse Over (Hover over) class '''

#from selenium.webdriver import ActionChains

# driver = webdriver.Chrome(executable_path = "C:\\Users\\volod\\Downloads\\chromedriver.exe")
# driver.get("https://rahulshettyacademy.com/AutomationPractice")
# 
# action = ActionChains(driver)                      #> Executes Action
# menu = driver.find_element_by_id("mousehover")
# action.move_to_element(menu).perform()              #> moves mouse over to Element. Argument is the "find_element_by_id"
# childmenu = driver.find_element_by_link_text("Top")  #> hovers over and moves to link called 'Top' 
# # "Top" will move back to Top of the page
# action.move_to_element(childmenu).click().perform()   #> Moves to Element (childmenu) and Clicks. Perform() is necessary for 'ActionChains'
# time.sleep(10)

#=================================================================================
''' Double Click with Pop-up / Right-Click '''

#driver = webdriver.Chrome(executable_path = "C:\\Users\\volod\\Downloads\\chromedriver.exe")
#driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

#action = ActionChains(driver)
#action.context_click(driver.find_element_by_id("double-click")).perform()  #> Does Right-click
#action.double_click(driver.find_element_by_id("double-click")).perform()   #> a javascript pop-up will open
### Switch to Javascript to perform action on Pop-up
#alert = driver.switch_to.alert
#alert.accept()
#time.sleep(10)

#===========================================================================================
## Assert not...  (pass Assert in False statement)

# driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# print(driver.find_element_by_id("displayed-text").is_displayed())
## Assert sucessful only if TRUE
# assert driver.find_element_by_id("displayed-text").is_displayed()  #> True

# driver.find_element_by_id("hide-textbox").click()                 #> Hides 'displayed-text' box
# print(driver.find_element_by_id("displayed-text").is_displayed())  #> prints "False"
## Assert will Fail
# assert driver.find_element_by_id("displayed-text").is_displayed()     #> will bring "AssertionError" error message

## To Pass Assertion...
# assert not driver.find_element_by_id("displayed-text").is_displayed() #> will PASS cuz of 'assert not' - opposite of True
#========================================================================================









