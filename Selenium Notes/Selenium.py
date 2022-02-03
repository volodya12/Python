
from _typeshed import IdentityFunction
from os import error
from selenium import webdriver
import time
from selenium.webdriver import ActionChains

=============================================
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
driver.execute_script()                 -> executes only JavaScript commands/code 
ChromeOptions (type of Class)           -> write instructions to configure Chrome on HOW it should be Invoked.

============================================
#=======================================================================================
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

#===========================================================================================
'''ChromeOptions (type of class) - things can be configured to Chrome before running it '''

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
#==============================================================================================

                        # SELENIUM PYTHON FRAMEWORK DESIGN

#1. PyTest Framework
* pip install pytest
* PyTest Projects Names always starts with "test_<Name>.py" -> test_demo1.py 
* Two SPACES required between Methods/functions
***** MUST HAVE Indentation present when writing Methods **************

* It is RECOMMENDED to build related Test Cases Per "test_pytest.py" file 

* PyTest code must be written in Functions and start with "test_" OR end with "_test"
        * Give MEANINGFUL NAME to a Method 
        
        ex: def test_firstProgram():
                print("Hello World")
* Every Function/PyTest Method is treated as One Test Case  
* An interpreter must be set as PyTest

# Test Case:
        def test_firstProgram():
                print("This is my first Test Case in PyTest")
        assert msg == "This message will not match"        (Test will fail)
#=============================================================
# Use CMD Line to execute ALL PyTests
* cd to PyTestDemo folder project-> key: py.test -v -s
        v-verbose-gives more info after execution
        s-prints console logs such "Hello World"

# Execute only Specific File of PyTest
* cd to PyTestDemo folder project-> key: py.test <fileName>.py -v -s
# Execute ONLY SPECIFIC Test Case/Methods within a File
* cd to PyTestDemo folder project-> key: py.test -k <TestCaseName or partial Name> -v -s
        - if there are several methods/test cases in a pytest file, and only specific once needs to run.
        - runs ONLY methods mentioned as keyword within ALL PyTest files. 
        k- keyword

=================== Mark/Tags =================================
# Execute ONLY Test Case/Methods that have TAG/MARK
#       Mark -> Marking Test Case/Methods with specific Tag for execution purposes
import pytest

@pytest.mark.<Any_tag_name>
def test_secondProgram():
        print("hello people")

* cd to PyTestDemo folder project-> key: py.test -m <tagName> -v -s

# TAG/Mark 
# "@pytest.mark.skip" will actually skip that TEST/Method Even tho, all Tests are meant to run
* cd to PyTestDemo folder project-> key: py.test -v -s

# @pytest.mark.xfail
# Operation that allows to Run Method even tho it would give an Error message (Bug) 
#       but it still needs to run as Pre-requisites. Error will NOT be Reported.

======================== Fixtures =========================================
# Fixtures -> goes into Fnction as a Parameter. When executed, it senses the fixture first before
#        executing function and navigates to THAT fixture.
# Must have "fixture" tag 

@pytest.fixture()
def setup():
        print("I will be executed First")
        yield
        print("I will be executed LAST")

def test_fixtureDemo(setup):
        print("I will execute steps in 'setup' method first because its a fixture")

# Yield -> First, 'Setup' will be executed because of FIXTURE, then, 'fixtureDemo', then anything after "yield"
#       Usually used for closing browser, delete oookies, or something to end test case with.

======================= Conftest.py file =========================================
# Conftest file -> this file would include test cases that are repeatedly used in other files
        * Whenever function with a fixture is being executed, it will look for that specific fixture name in 
        other files, if none found, it will look into "conftest.py" file. 

========================= Class/Scope ======================================================
# Class -> put all test cases into a Class. Segregate methods into Groups
import pytest

@pytest.mark.usefixtures("setup")           #- assuming there is method with fixture 'setup'
class TestExample:
        def test_fixtureDemo(self):
        print("hello world")

        def test_fixtureDemo2(self):
        print("hello world")

        def test_fixtureDemo3(self):
        print("hello world")

# this allows to execute fixture "setup" first, before any of these methods
        # Setup then fixtureDemo, Setup then fixtureDemo1, Setup then fixtureDemo2
* google: scope, class, hooks in pytest 

======================== Data Driven Fixtures ============================================
Section 18, Lesson 81

======================== Parametizing data ===============================================
# Parametizing data with multiple data sets using Fixtures
Section 18, Lesson 82

========================= Reports in HTML ===============================================
pip install pytest-html

py.test --html=report.html -v  #-> will create report as .html file in pytest file folder

* Navigate to pytest folder, look for report.html, right-click-> copy path-> paste into browser

========================= Logs/Logging ==============================================
Log Levels:
        Debug
        Info
        Warning
        error
        critical
--------------------------
import logging

# Indentation must be present when writing Methods

def test_loggingDemo():
# by including __name__, it will log file name this line mentioned in
#       by default, it will print as 'root'
#        This line responsible for printing Logs
        logger = logging.getLogger(__name__)

# 'fileHandler=' is an object
        fileHandler = logging.FileHandler('logfile.log')
# Format your log message line ('formatter='     it is an Object)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")

        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)      # prints starting from INFO level

        logger.debug("A debug statement is executed")
        logger.info("Information Statement")
        logger.warning("Something is in WARNING mode")
        logger.error("This is an error")
        logger.critical("Critical issue")

# When ^ script is executed. It will create 'logfile.log' file with formatted Logging message
#        and print logs there Instead of the Console.
#        AND will print log messages starting from INFO, Warning, Error, Critical 
#                No "debug" message
Prints: date time :INFO : <Project_Folder>.<file_Name> :Information Statement
                  :ERROR : pytestsDemo.test_logging :This is an error
==================
Include all these logging into HTML report
Section 19, lesson 87
====================================================================================










