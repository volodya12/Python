# https://www.youtube.com/watch?v=aAWvwGFkySI

# ancestor, parent, self, following-sibling, preceding-sibling, child, descendant
# Ancestor- Parent - Sibling - Child- Descendant
#       Following and Proceding

'''Always start with UNIQUE tag, not similar to others'''
'''Look to start with Containers=div - if no tags are unique'''
================================================================
# https://www.hyrtutorials.com/p/add-padding-to-containers.html


# following-sibling = Email
//label[text()='Email']/following-sibling::input[1]

# Parent - box of fields
//label[text()='Email']/following-sibling::input[1]/parent::div

# Child - firstName text field
//div[@class='container']/child::input[@type='text']

# Preceding-sibling = Check-box
//td[text()='Maria Anders']/preceding-sibling::td/child::input

# descendant = button 
//div[@class='container']/descendant::button 

# anserstor-or-self = many buttons
//div[@class='buttons']/ancestor-or-self::div  --> gives more specific divs
//div[@class='buttons']/ancestor::div    --> gives wide variety of divs

# Following - Password field
//label[text()='Password']/following::input[1]



















