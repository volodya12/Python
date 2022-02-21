''' 62. tags: iframe, frameset, frame '''
### Selenium ONLY works with HTML tags
# https://the-internet.herokuapp.com/ -> Frames and more (https://the-internet.herokuapp.com/iframe)

# Frames accepts: id, name or index value
# Here, we are passing ID
driver.get("https://the-internet.herokuapp.com/iframe")
 
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("Hello World")

# switch back to HTML 
driver.switch_to.default_content()  
print(driver.find_element_by_tag_name("h3").text)
