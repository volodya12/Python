from selenium import webdriver
import time
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome(executable_path = "C:\\Users\\volod\\Downloads\\chromedriver.exe", options=options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("a[href*='shop']").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")
for i in products:
    productName = print(i.find_element_by_xpath("div/h4/a").text)
    if productName == "Blackberry":
        i.find_element_by_xpath("div[2]/button").click()  #> also works "div/button"
    

#time.sleep(5)










# driver.get("https://rahulshettyacademy.com/angularpractice/")
# Shows all 4 products. Need to select specific one
# CSS (parent to child) -> h4.card-title a
# 
# Shows all 4 products. Need to select specific one 
# XPath (parent to child) -> //div[@class='card h-100']
# "//div[@class='card h-100']/div/h4/a"  -> Selecting Blackberry as Link 