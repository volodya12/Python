'''---------------------- WAITS function - Implicit/Explicit wait ---------------------- section 12:52-53 udemy'''
# implicit_wait() = it is Global wait, means it applies to entire code when mentioned once
#       It will wait 5 seconds until object is loaded. If object loads quickly, it will auto resume.
#       If object will NOT show at all, test resumes after 5 seconds.
#       USE Implicit_wait if entire application/web is huge and lots of data need time to load on page.
#       If each page is using about 3 seconds to load, Implicit wait is way to go.

time.sleep(4) = wait function that needs ("Import time")
time.sleep(<amountOfSeconds>) pauses test for few seconds using time class- (part of python, not selenium)

driver = webdriver.chrome(executable_path="c:\\chromedriver.ext")

#Globaly (applies to every screen on web, waits 5 seconds)
driver.implicit_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

# selects class name for input field "search_keyword"
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)

# gives count of result show for keyword "ber"
count = len(driver.find_element_by_xpath("//div[@class='products']/div"))
# varifying that it shows 3 results
assert count == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for allBut in buttons:
    allBut.click()      # Clicks all buttons (which adds product to the cart on web)

# Clicks on Cart icon (which is an image)
driver.find_element_by_css_selector("img[alt='Cart']").click()

# After items added to Cart, Clicks on "proceed to checkout"
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

# enter Promo Code
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")

# Clicks on Apply button
driver.find_element_by_css_selector(".promoBtn").click()

# Print text in Terminal that promo has been applied
print(driver.find_element_by_css_selector("span.promoInfo").text())

'''--- Explicit_wait ---'''
# Use Explicit_wait when specific page takes a while to load WHILE entire application/web is quick to load.
# Used to target only specific element
# You can put "Explicit_wait" for this specific "promoCode" element
# Package that needs to be imported for this Explicit wait function

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_condition as EC

# "WebDriverWait" object takes TWO arguments (driver, seconds)
wait = WebDriverWait(driver, 5)

#   this saying, i want to wait until "ClASS_NAME, promoCode" is present. 
wait.until(expected_conditions.presence_of_element_located(By.CLASS_NAME, "promoCode"))
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")

wait.until(expected_conditions.<varias methods to choose from>))
#                                alert_is_present
#                                presence_of_element_located(By.CSS_SELECTOR, "span.promoInfo")