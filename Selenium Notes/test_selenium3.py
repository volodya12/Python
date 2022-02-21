from selenium import webdriver;

driver = webdriver.Chrome(executable_path="C:\\Users\\volod\\Downloads\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Alerts.html")

driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a").click()
driver.find_element_by_class_name("btn-primary").click()

stopped at 63 - udemy




