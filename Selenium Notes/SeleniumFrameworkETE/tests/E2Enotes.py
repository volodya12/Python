TIP: Each Class is a Separate File indicates TestCase naming <class Name> -> "HomePage.py"
TIP: Test_e2e.py file contains TestCases of Objects
TIP: Fixture in Conftest used only when used in Multiple TestCases 

## Instance variable vs class Variable
        
Instance Variable = Call it with "self.shop" cuz its part of the Method "def shopItem(self):"
Class Variable = Call it with "<class>.shop"

'''ex: Instance Variable:'''
shops = (By.CSS_SELECTOR, "a[href*='shop']")
def shopItems(self):
        # driver.find_element_by_css_selector("//a[href*='shop']")
        driver.find_element(self.shops)     # Call with Instance.Variable (self.shops)

'''ex: Class Variable:'''
class HomePage:
shops = (By.CSS_SELECTOR, "a[href*='shop']")
def shopItems(self):
        # driver.find_element_by_css_selector("//a[href*='shop']")
        driver.find_element(HomePage.shops)     # Call with Class.Variable (HomePage.shops)

'''Method - refers to function name'''
def shopItems(self):            -> 'shopItems' is Method 
    pass
#=================================================================================
fixture = Stuff that will execute first before Executing actual test cases.
    ex: Create separate file and put WebDriver setup there. Code for launching Browser to specific site.

conftest.py = folder = includes all centralized for fixtures. 
    Declare all your "Fixtures" in Conftest.py and call them into Actual TestCases = separate file 
    Each TestCase is Separate File.py

TestCase = execution start from clicking the link, navigating to the page. Pretty much right after 
    browser launches.

Yield = Lines before 'yield', after Class will be executed first, then TestCase will be executed, AND
    finally, Lines after 'yield', will be executed. 
    EX: Lines after Yield are usually, "driver.close()", "return driver"

'return driver' => Ends the function 

request.cls.driver = driver => Taking 'driver' from fixture and assigned to class (cls) Variable "driver" 
====================================================================
## Accessing Class Variable

Class NumberOne:
    num1 = 200
    num = 100

    def access(self):
        return self.num1 + self.num

#===============================================================
Calling cls Class

'return driver' and yield = CANNOT go together 

------ Conftest File: (contains fixtures)

def setup(request):
    driver = webdriver.Chrome(executable_path = "C://User")
    driver.get("www.yahoo.com")
    driver.maximize.window()
    request.cls.driver = driver         # Calling 'cls' Class Driver from Test File
    yield           # Lines above runs first, then TestCase, and Then lines AFTER "Yield"
    driver.close()

------- Test File:

Class TestOne:

    def test(self):
        self.driver.find_element_by_id("name").click()

        # Adding 'self', this file makes connection with Conftest file
        # Add 'self' to all driver from now on to establish connection
        cards = self.driver.find_element_by_css_selector("#NameLast").click()
        self.driver.find_element_by_css_selector("#LastName").click()
        self.driver.find_element_by_css_selector("#FirstMa,e").send_keys("kyle")

#====================================================================
Inheritance 

File_1: 
# Contains Fixtures
@Test.mark.fixture("setup")     # 'setup' is connection to File_2 Class
class BaseClass:
    pass

TestCase_2:

class TestOne(BaseClass):       # 'BaseClass' is main Inheritance from File_1

    def test(self, setup):      # 'setup' provides inheritance of Parent which is File_1 
                                # 'setup' is optional now since you have 'BaseClass' as inheritance
                                # 'setup' can be removed
        code here
#=====================================================================
Command Line (cmd) to Select Browser at run time
'''Google for "command line options pytest"'''

py.test --browser_name chrome/firefox/IE

browser_name -> is Key
chrome -> is Value

----------------------
Paste code from google documentation site that will effect command line input
If code below is not given, PyTest commands will not be RECOGNIZED

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"

    )

# config.getoption must be added to code to retrieve Browser_name from command line
@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")    # retrieves key:value to run browser
    if browser_name == "chrome":
        driver.webdriver.Chrome(executable_path="C://chromedriver.exe")
    elif browser_name == "firefox":
        driver.webdriver.Firefox(executable_path="C://chromedriver.exe")
    elif browser_name == "IE":
        driver.webdriver.IE(executable_path="C://chromedriver.exe")
    driver.get("www.yahoo.com")     # Once it choses which browser to run, it will execute driver.get
    driver.maximize.window()
    
    request.cls.driver = driver     # invokes driver from Conftest file
    Yield
    driver.close()

#=====================================================================
POM - Page Object Model Mechanism 
Create Object class for ALL web elements. Reduces code duplication, clustering, improves Maintenance
Each Class is a Separate File indicates TestCase naming <class Name> -> "HomePage.py"

-----TestCase_1:
from selenium.webdriver.common.by import By 
class HomePage:

    # Constructor = Needed to establish connection class 'HomePage' with TestCase 'test_e2e.py' 
    def __init__(self, driver):
        self.driver = driver

    shops = (By.CSS_SELECTOR, "a[href*='shop']")        # this is Tuple
    
    def shopItems(self):        # 'shopItems' is a Method
        # driver.find_element_by_css_selector("//a[href*='shop']")
        'return' self.driver.find_element(*HomePage.shop)     # * reads 'shops' as Tuple/Ends Function Method
        self.driver.find_element(*HomePage.shop).click()      # Performs a Click
        
------TestCase_2:
from selenium.webdriver.common.by import By 
class CheckOutPage:     # Add to TestCase to establish connection with 'driver'
    
    # Constructor = Needed to establish connection class 'HomePage' with TestCase 'test_e2e.py' 
    def __init__(self, driver):
        self.driver = driver

    # driver.find_element_by_css_selector(".card_title a")
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

def getCardTitles(self):     # Add to TestCase to execute the Function Method
    return self.driver.find_elements(*CheckOutPage.cardTitle)       # Finds Element(s) for all Titles

def getCheckOutItems(self):     # Add to TestCase to execute the Function Method
    'return' self.driver.find_element(*CheckOutPage.checkOut)   # Ends Function Method
    self.driver.find_element(*CheckOutPage.checkOut).click()    # Performs a Click

#==================================================================
Optimmization of Page Objects
When you have 10 or more pages to Test (Each page is a class, Each Page contains an Object)

Object is considered an Object present on web page (Not web element)
    ex: Link, button, Text 


shopItem is first page
getCheckOutItems is second page 

def getCheckOutItems(self):     # Add to TestCase to execute the Function Method
    self.driver.find_element(*CheckOutPage.checkOut).click()    # Performs a Click

def shopItems(self):        # 'shopItems' is a Method
    # driver.find_element_by_css_selector("//a[href*='shop']")
    self.driver.find_element(*HomePage.shop).click()      # Performs a Click
    checkOutPage = CheckOutPage(self.driver)
    return checkOutPage

#============================================================================
Custom Utilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BaseClass:
    def verifyLinkPresence(self, text): 
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(By.LINK_TEXT, text)) # Or HardCode replacing text with "India"

IN TestCase (test_e2e.py)

self.verifyLinkPresence("India")

#================================================================================
Data Driven Set -> Eliminate HardCoded values

IN Conftest -> This method used when applied to Multiple TestCases 

# Write Tuple = 3
@pytest.fixture(params=[("kyle", "Sam", "Nick"), ("Luke", "Lacy", "Summit"), ("King", "Kong", "Bond")])
def crossBrowser(request):
    return request.param
---------------------------
IN TestCase

'''Data Driven using Tuple'''

class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage= HomePage(self.driver)
        homepage.getName().send_keys(getData[0])
        homepage.getEmail().send_keys(getData[1])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData[2])

        homepage.submitForm().click()
        alertText = homepage.getSuccessMessage().text
        assert "success" in alertText 
        self.driver.refresh()       # Will Refresh browser and clear off fields 

# By having multiple values in a Tuple, Pytest will execute this twice
@pytest.fixture(params=[("kyle", "Sam", "Nick"), ("King", "Kong", "Bond")])
def getData(self, request):
    return request.param

-----------------------------------
'''Data Driven using Dictionary'''

def test_formSubmission(self,getData):
homepage= HomePage(self.driver)
homepage.getName().send_keys(getData["firstName"])
homepage.getEmail().send_keys(getData["lastName"])
homepage.getCheckBox().click()
self.selectOptionByText(homepage.getGender(), getData["middleName"])

@pytest.fixture(params=[{"firstName": "kyle", "lastName": "Sam", "middleName": "Nick"}, 
    {"firstName": "King", "lastName": "Kong", "middleName": "Bond"}])

def getData(self, request):
    return request.param
------------------------------------
'''Data Driven in Separate file'''

@pytest.fixture(params=HomePageData.test_homePage_data) # pulls data set from different file (class.Variable)

def getData(self, request):
    return request.param

IN Different File:

class HomePageData:

    test_homePage_data = [{"firstName": "kyle", "lastName": "Sam", "middleName": "Nick"}, 
        {"firstName": "King", "lastName": "Kong", "middleName": "Bond"}]

#======================================================================
Logging

import inspect
import logging

IN Test_e2e.py

log = self.getLogger()
'''Code for Logging found in Utilities.BaseClass.py'''

IN Different File: This is also TestCase 

class TestHomePage(BaseClass): # 'BaseClass' is connection to File with class of 'BaseClass'

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage= HomePage(self.driver)
        log.info("first name is " + getData["firstName"])
        
        homepage.getName().send_keys(getData[0])
        homepage.getEmail().send_keys(getData[1])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData[2])

        homepage.submitForm().click()
        alertText = homepage.getSuccessMessage().text
        assert "success" in alertText 
        self.driver.refresh()       # Will Refresh browser and clear off fields 

        @pytest.fixture(params=[("kyle", "Sam", "Nick"), ("King", "Kong", "Bond")])
def getData(self, request):
    return request.param