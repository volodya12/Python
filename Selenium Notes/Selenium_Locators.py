# Locators in Selenium -> way to draw out links from Web sites
# https://www.youtube.com/watch?v=HBOdscUwUnc&t=1197s -> ID, Name, Link, Tags, Class & CSS Selector

'''Determine When to use specific Locators'''
# Sometimes, easy locators such as ID, Name, class, tags, CANNOT be utilized simply because 
#   naming for these locators already used/occupied by other Nodes as well. And when running Selenium,
#   it will NOT execute because that Name also being used in other tags within same page. 
# A Unique name must be chosen for each Node. 
# To Avoid, use XPath for Child-> Parent... or CSS Selector for Parent-> Child traversing 'back'
#       Tip: in "inspect" window, Ctr+F (find), key tagName want to use, see if it find multiples
# 
# Common XPath ways: xpath("/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a")
#   //*[@id="OkTab"]/button     (parent->child)

# Best to Capture Full Xpath/Traversing
#   Inspect - Right-Click on Node, Copy->Select "Copy Xpath" or "Copy Full Path"
'''-----------------------------------------------------------------------------------------'''
With Java:
driver.findElement(By.id("search_query")).sendKeys("shorts")

TIPS:
* <a href=<link>... </a> -> this is 'anchor tag' for link 
* driver.find_elements_by_tagName("a").size()   -> finds ALL Links and return #
* Attribute = name, class, id, and any other attributes mentioned in a Node 

# Tag is 'Title' = Short legged animal<
# Usually located withing <a... </a> anchor tag
# 'Link_text' would be "Short legged animal"
# 'Partial_link_text' would be "legged animal"
driver.find_element_by_link_text(<grab text from 'title tag'>).click()
driver.find_element_by_partial_link_text(<grab partial text from 'title tag'>)

============================================
If need to pull group of whatever, find Parents, and find common Tag being Shared

Use 'driver.find_elements' when looking for more than one element/to Pull more than One element 
ex: slideshow on web: Multiple images are sliding automatically
        
driver.find_elements_by_class_name("homeslider-container").size() -> will say how many slides in a slideshow

================================================= CSS Selector 
# CSS Only Traverse/Moves Forward in Tags (Parent-> child)

# Tag 'input' is optional ("input#email")
# With CSS, you can do ID, Class, Attribute, and/or class & attribute combined

driver.find_element_by_css_selector("#email")  -> ID
driver.find_element_by_css_selector(".email")  -> Class
driver.find_element_by_css_selector("[name=email]")  -> attribute=value in []
driver.find_element_by_css_selector(".inputtext[data-testid=royal_email]")  -> class and attribute used together
                                        ^class  &  ^attribute
# used whenever trying to pull element BUT some attributes are SAME. 
# To differentiate fields, use class and attribute together. 

================================================= XPath Selector
# https://www.youtube.com/watch?v=jD37dxX3ZNo -> XPath Locator

# Provides flexibility with Traverse forward and back using tags (parent->child / child-> parent-> grandparent)
# Ability to find Web Elements using HTML tags and DOM structure
# Can be used to navigate through elements and attributes in DOM

# //tagname[@attribute='value']
# //*[@attribute='value'] *represents all Tags. Whatever tag, attribute match, it selects it.

''' XPath Shortcut'''
# Find specific Node/Tag you looking while "inspect" to identify your field,
#       Right-Click-> copy-> Select "Copy XPath" and Paste into "driver.find_element_by_xpath()"
#       This will give correct Path to your Inspected field. 

# "Copy Xpath" -> Relative Xpath -> Partial Xpath -> //*[@id="divLogo"]/img
# "Copy Full Xpath" -> Absolute Xpath -> Full Xpath -> /html/body/div[1]/div/div[3]/div[1]/img

# Absolute Path = Starts from the Root node /html/body/ => Good For Traversing
# Relative Path = Jumps directly to Element in DOM //[@name="logo"] 

# Absolute Path = Uses ONLY tags/nodes /div/li/a/name  => Useful for Traversing
# Relative Path = Uses Attributes     name="username"

'''XPath Options''' 
# There are many more other options, these are Commonly used:

# And
driver.find_element_by_xpath("//input[@name='username' and @class='uName']")
# Or 
driver.find_element_by_xpath("//input[@id='searchbutton' or @class='btn btn-default button-search']")

# Contains()
//tagname[contains(@attribute, 'value')]   == //input[contains(@id, 'firstName')]
It checks if the attribute is present, If value matches the attributek. Portion of Value may work 'first'
Ex: //input[@id, 'start'] and //input[@id, 'stop'] ===> //input(contains[@id, 'st']) --> Dynamic xpath

# Starts-with()
Ex: //input[@id, 'start'] and //input[@id, 'stop'] ===> //input(starts-with[@id, 'st']) --> Dynamic xpath

# Text()  -> useful if none attributes are present in Node. Mostly within 'a' anchor tags
<a href="http://automationpractice.org" Woman</a>
//a[text()='women']

# Chained Xpath --> write multiple attributes if they located inside Container. Xpath followed by another Xpath
//form[@id='searchbox']//input[4]
or can write this way:
//form[@id='searchbox']//input[@id='search_query_top']

======================================================= XPath Axes
# https://www.youtube.com/watch?v=BRzlyGXx13Q&t=850s -> Advanced XPath Axes Methods

# Method used when web elements is NOT identified with ID, Name, class, link text, css selector
#https://1.bp.blogspot.com/-qf5RVHBUaEQ/X2LyZ0ylTKI/AAAAAAAAQ-4/S29JPBhxqKgHEdYT1iiHKHKREM--xhjDwCLcBGAsYHQ/s640/Picture1.jpg
#https://training-course-material.com/images/3/3d/XPathAxis.png  -> image diagram-Relationship of Nodes
#https://www.scientecheasy.com/wp-content/uploads/2019/08/html-page.png ->image diagram-Relationship of Nodes
# They are:
    Self
    Parent
    Child
    Ancestor 
    Descendant
    Following
    Following-sibling
    Preceding 
    Preceding-sibling 

================================================== Elements in Shadow DOM
# https://www.youtube.com/watch?v=bpzyjNZ0jaw  -> Shadow DOM

# DOM - Document Object Model -> HTML consists of DOM or build in DOM structure 
# Some Elements cannot be access using HTML Tags, MUST use DOM JavaScript
#   DOM identification within 'Inspect' -> they will have '#shadow-root' over the node.

root=driver.find_element_by_tagname("book-app")  # Shadow DOM starts="Shadow Host"->"Shadow Root"
JavascriptExecutor js=(JavascriptExecutor)driver
shadowDom1=(WebElement) js.executeScript("return arguments[0].shadowRoot", root)  # "Shadow Root"

appheader=shadowDom1.find_element_by_tagname("app-header")
apptoolbar=appheader.find_element_by_css_selector("app-toolbar.toolbar-buttom")
bookinputdecorator = apptoolbar.find_element_by_tagname("book-input-decorator")

bookinputdecorator.find_element_by_css_selector("inut#input").sendKeys("Testing")
























