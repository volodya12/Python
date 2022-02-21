If assert is NOT true, Code will fail with error
If assert PASS no errors will display and Code runs Smooth
#============================================================
# Hide / Show Buttons 
# https://rahulshettyacademy.com/AutomationPractice/
# Its good practice to have "Assertions" for true/false

assert driver.find_element_by_id("displayed-text").is_displayed() # True or False
#print(driver.find_element_by_id("displayed-text").is_displayed()) # True or False

driver.find_element_by_id("hide-textbox").click()

assert not driver.find_element_by_id("displayed-text").is_displayed() # True or False
#print(driver.find_element_by_id("displayed-text").is_displayed()) # True or False

assert not => If statement returns FALSE, as expected, the "assert" will FAIL and Test will FAIL
    That is why, use "assert not" so the statement result in TRUE 
================================================================

assert "Selenium" in "This is tested in Selenium", "Selenium is NOT present"
print("Validation 1 passed")


str1="Python"
str2='python"'

assert str1==str2, "String matching Failed"
print("Validation 2 Passed")

assert "Selenium" in ["Sellenium", "Kalomani", "Java"], "Selenium is NOT present"
print("Validation 3 passed")

# assert not driver.find_element_by_id("displayed-text").is_displayed() #> will PASS cuz of 'assert not' - opposite of True
# assert (driver.find_element_by_id("autosuggest").get_attribute('value') == 'India'  

# for i in checkboxes:
#    i.click()       --> this will click all checkboxes on that page in (type=checkbox) attribute
#    assert.i.is_selected()    -> this asserts that all 3 checkboxes are selected 

'''if you want to select checkbox 'option 2'''
# for i in checkboxes:
#    print(i.get_attribute("value"))  -> this will print how "value" for checkboxes will display in terminal (good info for you)(then, "print" may be removed)
#    if i.get_attribute("value") == "option2":
#       i.click()       
#       assert i.is_selected()   

#radiobutton = driver.find_elements_by_xpath("//input[@type='radio']")
#radiobutton[2].click()
#assert radiobutton[2].is_selected()   -> verify button selected

## now, remove "print(alert.text)" and give it a variable to do assertion later in test
# alertText = alert.text
# assert textValidate in alertText    ----> if test passes, assert is correct, if fail, assert failed.

### varifying that it shows 3 results
#assert count == 3

#assert list == list2         
#> this asserts that two lists from two different pages are same.
#> if error received, 'assert' statement failed, otherwise it passes if no errors

# assert "Opening a new window" == driver.find_element_by_tag_name("h3").text     
#> If NO errors, ASSERT is Correct.

# print(driver.find_element_by_id("displayed-text").is_displayed())
## Assert sucessful only if TRUE
# assert driver.find_element_by_id("displayed-text").is_displayed()  #> True

## To Pass Assertion...
# assert not driver.find_element_by_id("displayed-text").is_displayed()
#> will PASS cuz of 'assert not' - opposite of True

