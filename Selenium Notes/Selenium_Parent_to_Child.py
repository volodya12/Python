Grandparent to Parent
Parent to Child
Child to Parent Traverse

# XPath vs CSS Selector = CSS does NOT have the ability to Traverse (going from one tag up/down to another)
#                                = XPath HAVE ability to Traverse (jump from one tag down/up to another tag)(div/label)

driver = webdriver.Chrome(executable_path="C:\\Users\\volod\\Downloads\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

## Task: Traversing UP from CHILD to GRANDPARENT
        ## MUST only use XPath, because CSS selector won't Work

:: double semicolon provides path FROM CHILD to Parent and to GrandParent (if there are two 'div' tags)
:: makes you go UP in tags

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
# going from Child to GrandParent
driver.find_element_by_xpath("//div[@class='product-action']/button/parent::div/parent::div").click()

# This is verification, in a way, check to make sure correct 'add to cart' button is click and matches whats inside the 'Cart'
# Loop go thru products, will find button from 'product-action' class tag, SEE the text and Click the 'add to cart' button.
for i in buttons:
    print(i.find_element_by_xpath("parent::div/parent::div/h4").text)   #-> this is sort of verification to print product Name the one Clicked.
    i.click()

======================================================================

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
====================================================================================

driver = webdriver.Chrome(executable_path="C:\\Users\\volod\\Downloads\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)

countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")

for country in countries:
    if country.text == "India":
        country.click()
        break

print(driver.find_element_by_id("autosuggest").text)
assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"
=====================================================================
## Task: Do the comparison between page 1 (product title) vs page 2 (product title)

#list = []
#list2 = []

#page1 = driver.find_element_by_xpath("parent::div/parent::div/h4").text
#page2 = driver.find_element_by_css_selector("p.product-name")
============================================================================
===============================================================================

driver = webdriver.Chrome(executable_path="C:\\Users\\volod\\Downloads\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_xpath("//div[@class='product-action']/button/parent::div/parent::div").click()
============================================================

driver = webdriver.Chrome(executable_path="C:\\Users\\volod\\Downloads\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
================================================================

driver = webdriver.Chrome(executable_path = "C:\\Users\\volod\\Downloads\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("a[href*='shop']").click()
driver.find_element_by_xpath("//div[@class='card h-100']/div[2]/button").click()
