# https://www.youtube.com/watch?v=o0XvMdpNIvo&t=3s --> commonly used Syntax/XPath
/ = indicates Select child node from parent
// = node anywhere in DOM
(=) = full match
(,) = partial match
(*) = any tag (can be applied anywhere within Locators)

//tagName[@text()='text']
//*[text()='text']
//tagName[contains(text(),'text')]
//tagName[contains(id,'text')]
//tagName[contains(.,'text')]   # (.) means string
//*[text()[contains(., 'text')]]    # Searching Entire DOM for specific text

# Collection
(//h2)[1]   # will count all 'h2' but with index of 1 will indicate 1st h2

//h2[starts-with(@data-attribute, 'text')][1]
//input[@type='text'][1]

# Attribute AND, OR
//input[@type='text' and @value='Go']
//input[@type='text' or @value='Go']

# Use of Containers, normally located in 'div' tags
# Parent-Child
//div[@class='inventory-list']/*[1]
//div[@class='inventory-list']/*[last()]    # instead of indexing, links straing to last child tag
//div[@class='inventory-list']/*[last()-1]    # first from last/bottom
//div[@class='inventory-list']/*[last()-2]    # second from last/bottom







