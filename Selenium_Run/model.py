from selenium import webdriver

class Booking







driver = webdriver.Chrome(executable_path="C:\\Users\\volod\\Downloads\\chromedriver.exe")

# closes Browser after testing finished
def __exit__(self, exc_type, exc_val, exc_tb):
    self.quit()

def land_first_page(self):
    self.get(const.BASE_URL)

# change 'currency' to 'currency=None' so that there is Hard coded value as None
#def change_currency(self, currency):
#    currency_element = self.find_element_by_css_selector("button[data-tooltip-text='Choose your currency']")
#
#    currency_element.click()