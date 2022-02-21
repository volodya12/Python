# https://stackoverflow.com/questions/30503518/waiting-for-an-element-to-load-using-selenium
from cgitb import text
from importlib.metadata import files


-- Verify if Specific Element is "Present" on screen
(Java) Boolean isPresent = driver.findElements(By.<locatorName>()).size() > 0

-- (Java) Verify Specific Element is "Loaded" on screen (Use WAIT)
WebDriverWait wait = new WebDriverWait(getDriver(), timeOut);
WebElement element = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("MainContent_lblLandmarkUPRN")));

String actualValue = element.getText();
Or
WebElement element = wait.until(ExpectedConditions.textToBePresentInElement(By.id("MainContent_lblLandmarkUPRN"), s));
Or 
Explicit wait or Fluent Wait

#=======================================================================
Running Selenium in Command line (CLI)(cmd)
# https://stackoverflow.com/questions/1231975/i-want-to-run-selenium-test-case-file-from-command-line
====================================================================
# Common WebDriverException
# https://www.softwaretestinghelp.com/exception-handling-framework-selenium-tutorial-19/#5_orgopenqaseleniumInvalidSelectorException

noSuchElement - occurs when WebDriver is unable to find or locate elements
noSuchWindow - when webdriver tries to switch to Invalid window
invalidSelector - wrong selector used/incorrect/wrong syntax/common in XPath 
noElementPresent/ElementNotVisible - WebDriver performs action on invisible/non-existing element 
TimeOutException - wait time exceeds for component to load 
StaleElement - means, Element is no longer Present in the web page but visible in DOM
    - differ ElementNotVisible

================================================================
# Page Object Model (POM) (Java based)
#       https://www.youtube.com/watch?v=-0F-YBAQdGE > 1
#       https://www.youtube.com/watch?v=tnWig6KfQ9w > 2

- Stores Object Repository and Locators for web UI elements Separately
    - Each Page would have separate Class/Object Locators
    - AND Corresponding page with Action Methods 

- Advantage is it reduces code duplication and improves test maintenance
- Benefits of POM:
    Test Objects and Functions are separated for easy Maintenance and keeping code clean.
    Test Cases and Class/Objects are kept on separate files, for ease of change code if needed. 
    Easy Maintenance and Less Rework
    Every unique object locator is created only once 

You create Locators and Methods/Actions on separete files
    Locators/Objects/Class = xpath, name, className, id, link, text
    Method/Action = return, sendKeys, click, doubleClick, getText...


==================================================================
# Listeners in Selenium

Often used between testing multiple pages which requires passing data from one page to another.
Its ability to listen to certain events. Often used for customizing reports and logs.
It serves as an interface that can modify system behavior.

Types of Listeners:
    WebDriver Listeners
    TestNG Listeners

(Java) driver.manage().Navigate()/Forward()/Back()

===================================================================
# Type of TEsting supported by Selenium

Smoke, Sanity, Functional, Regration, Cross-browsing, integration, Responsive Testing
===========================================
# Build faces in Maven

Validate, combine, test, package, install, diploy
=============================================
# Build in Framework in Selenium Python
PyTest, Robot Framework, UnitTest etc.
#========================================
Handling Mouse Actions Methods 
- provide methods 



