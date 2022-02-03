from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\volod\\Downloads\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com")

print(driver.title)
print(driver.current_url)
driver.get("http://rahulshettyacademy.com/AutomationPractice")
assert "rahulshettyacademy" in driver.current_url, "rehulasshetyacademy is present"
#driver.back()
#assert driver.title == "Rahul Shetty Academy"
#driver.refresh()
