# Video course from: https://www.youtube.com/watch?v=rfscVS0vtbw
# Video course from: Udemy - Python for Absolute Beginners

# Python is case Sensitive AND Indentation also MATTERS
# To Comment out any line (python does NOT support comment out Blocks)
'''Can use Tripple Quiotes to sort of Comment out Blocks'''
''' If code seems correct but not running, CHECK INDENTATION '''
########## Shortcuts
# https://code.visualstudio.com/docs/editor/codebasics  - Basic programming Editing tips
# Ctrl+Alt+Arrow keys - adds several curser which can comment out blocks by #
# Ctrl+F3 - Put cursor on word first, press, will search for that word
# Alt + Click - create multiple cursors anywhere you want
# Ctrl + Shift + L = highlights multiple matched words you clicked on
# Ctrl + / = Comments out line, entirly
# Ctrl + Z = Undo the Comment line

# Data Types: 
Strings
Integers
Boolean
Dictionaries - Stores Data Value, Ordered, NO Duplicates, Altered. Key:Value-> dic1 = {"Car": "Toyota"} curly brackets
Tuples - CANNOT be altered (Immutable, Ordered=order don't change)(tuples1 = ()

Lists - CAN be altered (Mutable)(have Duplicates)(list1 = []
Sets - Altered list BUT with NO duplicates, Unordered=order can be changed. (set1 = {} curly brackets
FrozenSets - Sets BUT Immutable (no change allowed) frozenset(Object)
Ranges - generates numbers within certain bounds. (Range(start, stop, step) -> Range(10)->0 thru 10

# PEP8 (Python Enhancement Proposal) - a document that provides guidelines and best practices on how to write Python code. 
#    Focuses on improving readability and consistency on Python code. 
# Expression = ex: print("i have used \"" + mixed[-1] + "\" too many times")
# Argument = same as paremeters being accepted into a function. ex: range(2, 10) -> argument is what inside ()
'''-- Check INDENTATION to work ----'''
'''------------------------------------- Google for Escape Characters --------------- '''
'''------------------------------------- Google for String Functions --------------- '''
'''------------------------------------- Google for Import Python Modules --------------- '''
'''------------------------------------- Google for Other Functions like "range","copy" --------------- '''
# Lists = Mutable, meaning it can be changed, removed, added
     # Mutable stored as References (can be changed)
# Strings = Immutable, meaning it cannot be changed (When they are in a form of a List)
     # Strings can only be reassigned entire new Value, but cannot be append to it, changed via Index
     # Immutable stored as themselves (hard coded values) (int, float, strings, Boolean values)
# Iterate - going thru the list and print in display (for loop/while loop)
     # Repetitively execute the same block of code over and over again.
'''-------------------------------------'''
# print vs return 
# print = does not affect calculations and DISPLAYS result to Programmer
# Return = Does NOT DISPLAY output to programmer, JUST specifies what certain function is supposed to give back  
'''------------------------ Troubleshoot ---------------------------'''
# name = "vladimir"
# number = "12345"
# num = 123
# sen = float(123)

# print(type(name)) -> will show its a String
# print(type(number)) -> will show its a String
# print(type(num)) -> will show its a Integer
# print(type(sen)) -> will show its a Float

# Trick: Always use "Float" to convert into a Number (NOT Int)
# Int - Cuz if User types for input: 1.2, it will give an error for "int"
# Float - but if user types for input: 1.2, you will NOT get error
# Float = 1.2 (decimal numbers)
# Int = 1 (single numbers)
     # Int = also converts decimal into Whole Number

'''------------------------ All about String ----------------- '''

# name = "kyle"
# age = '24'
 
# print("change my " + name)
# print("change my last " + name)
# newage = 22
# print("check my " + str(newage))
 
# print("giraffe academy".replace("giraffe", "vlads"))
# If User wants to move CURSOR to next line rather than on same line
     # ex: input("What is your name? ")
          # result: What is your name? Vlad
     # fix solution: input("What is your name?\n")
          # \n this puts CURSOR on next line
'''---------- upper/lower/isupper/islower -------------------'''
# name = "There are no capitalization here"
# print(name.upper())
# print(name.lower())

'''--------- Boolean String ------'''
# print("mixCases".isupper()) # False
# print("MIXCaSES".isupper()) # False
# print("MIXCASES".isupper()) # True
# print("SHOUT!".lower().isupper()) # False, cuz "shout" converted to lower
# print("shout".isalpha()) # Only Letters
# print("12345Shout".isalnum()) # Only Numbers and Letters (no spaces)(if spaces, would be False)
# print("12345".isdecimal()) # Only Numbers
# print("  ".isspace()) # Only Spaces
# print("not just spaces"[3].isspace()) # True, cuz 3rd char is a space 
# print("Shout Out%".istitle()) # Only Titlecase (First Letter of the word must be capitalized)
# print("the great gatsby".title()) # Capitalizes each letter of the Word, makes it look like Title
'''--------------------- startswith/endswith -------------------'''
# print("the great gatsby".startswith("the")) # gives boolean of "startswith"
# print("the great gatsby".startswith("T"))   # False, cuz its Case Sensitive, must have "t"
# print("the great gatsby!".endswith("gatsby!")) # must have "!" with it"
'''---------------------- join ---------------------'''
# print("".join(["one", "two", "three"])) #onetwothree (no separator)
# print(",".join(["one", "two", "three"])) #one,two,three (separator by ,)
# print(": ".join(["one", "two", "three"])) #one: two: three (separator by : and space)
# print(", ".join(["one", "two", "three"])) #one, two, three (separator by , and space)

'''------------------------------- Split ----------------------------'''
# print("one, two, three".split()) # ['one,', 'two,', 'three,']
# print("one, two, three".split(", ")) 
'''---------------------------------- rjust/ljust --------------------------'''
# right/left justified

# print("hello world".rjust(15)) # adds 4 spaces from left. 15 cuz "hello world" has 11 char + 4"
# print("hi".rjust(3)) # Will add 1 space from left

# print("hello world".ljust(15) + "four spaces later") # adds 4 spaces after "hello world". 15 cuz accounting for 11+4
# print("hello world".rjust(15, "-")) # -----hello world
# print("hello world".ljust(15, "*")) # hello world*****

# print("hello world".center(15)) # Centers it
# print("hello world".center(15, ":")) # ::hello world::

'''-------------------------- strip/rstrip/lstrip/replace/len ----------------------'''
# removes characters, such white spaces. ONLY works on Strings
# only accepts one argument

# print("I had an exciting trip!!!11111".strip("1")) # removes only "1111"
# print("I had an exciting trip!!!11111".rstrip("1")) # removes "1111" from Right Side
# print("I had an exciting trip!!!11111".lstrip("1")) # removes "1111" from Left side (WHich is NONE)

# print("juice, bread, cheese, beef, bread".lstrip("juice, ")) # removes "juice, " 
# print("blueblueyellowblue".strip("blue")) # Deletes all "blue", leaving "yellow"

# print("Good morning".replace("morning", "arternoon")) # Replacing "morning" with "afternoon"

# print(len("three")) # 5
# print("antidisestablishmentarianism"[7:20]) # prints characters from 7 to 20, "establishment"
# print(len("antidisestablishmentarianism"[7:20])) # prints character length from 7 to 20, "13"
''' ------------------------------ format - Concatination with format OR (F-String)-----------'''
# instead of concatinating all of those variables together, which makes a mess when its a long string. 
# Use .format() instead
 
# name = input("your name: ")
# degree = input("Your degree: ")
# job = input("your job: ")
# experience = input("your experience: ")

# print("{} majored in {}, works as a {}, and has {}, years of experience".format(name, degree, job, experience))
          # this prints "Vlad majored in IT, works as a QA tester, and has 3 years of experience"


'''----- F-String ---'''
# score = 0
# height = 3.0
# isWinning = True
# 
# Use f before "
# print(f"Hey, your score is {score}. and your height is {height}, and You about to Win big {isWinning} price")
# reads "Hey, your score is 0, and your height is 3.0, and You about to Win big True price"

''' % percent string formating'''
# %s = string
# %d = decimal
# %f = float
# ('Vlad', 30, 120.5))  Input
from typing import Tuple


print("Hello, my name is %s, I am %d, and i weight %f" % ('Vlad', 30, 120.5))

'''------------------------------------- Google for Escape Characters --------------- '''
# .,? - punctuation marks
# (\n) means break line and it will move to next line down
#               print("Webster\nSilent")
# Put Quotation mark inside the string
#        print("Webster\"Silent") -> Webster"Silent
# (\t) Tabs
#   print("This\tis\ta\tlot\t\tspace.")
# (\' or \") put quotes inside string
#   print("\"Please Don\'t do this.\"")
# (\\) backlash
#   print("put backlash here \\.")

# (\) Can be used for "Line Continuaton" (note: indentation must be complyent, must line up)
#    ex_12 = 2 + \
#            3 + \
#            1 +
# print(ex_12) # equals 6
##### Example with String
# ex_10 = "this how\ 
# line indentation\ 
# used for Strings"
# print(ex_10) # This how line indentation used for Strings
#####
# Concatinating (adding) with Continuation line must be perfectly alligned 
# ex_8 = "hello " + \
#        "world"
# print(ex_8)

'''---------------------------------------------------------'''
# abs = absolute / pow = power (3, 2) / max(2, 4)/min / round(3.7) 
# floor = grabs lowest number / ceil = rounds number up / sqrt = square root / float() = converts to a integer if input is String
# "float" vs "int" = Float used where number has a decimal, where number needs to be more precise. "Int" is number without decimal. 
# Float = decimal (3.14)

#          from math import *   -> to get more math functions

#- Gives access to more math functions
#        FROM MATH IMPORT *      (all in lower case)
'''-------------------------------------'''
### 2 decimal number with 0 ending
### If you want number 0 to appear at end of number WHEN 'round' not working (sometimes it may not add 0 at end)
# final_num = "{:.2f}".format(<variable> or <number> here)
# print("%.2f" % round(a, 2)) -> 2 decimal places
# print("{:.2f}".format(a) -> 2 decimal places
# print("{:.2f}".format(round(a, 2))) -> 2 decimal places
# print("{:.15f}".format(round(a, 2))) -> 15 decimal places

'''---------------------- Variables and Data Types ------------'''
# name = "George"
# age = "30"

# print("There once was a man named " + name)
# print("He was " + age + " years old.")

'''----------------------- Variable Scopes ---------------'''

# There are Global and Local Variables
# Global Variable is outside of a function
# Local Variable is inside a function and cannot be used for Outside of function

# var = "hello world"   -> Global Variable
# 
# def loc_ex():
#      var = "this is a string" -> ONLY THIS WILL PRINT  -> Local Variable
#      return var 
# 
# loc_ex() -> Since the function has been executed, the local variables ONLY run ONCE. 
#           That means, print(var) will not WORK after function is executed. print(var) becomes Global Var. 
#           Variable in Function is being forgotten, after function is executed. 
#
# print (var) -> WILL NOT PRINT

####### OR

# def local1():
#      example = "banana"
#      print(example)
# def local2():
#      example = "apple"
#      print(example)
# 
# example = "sweet"
# local1()
# local2()
# print(example)

####### OR

# example = "hello world"
# 
# def local():
#      return example
# 
# print(local())  -> this will still print "hello world"

####### OR

# example = 100
# 
# def local():
#      example = 50
#      return example
# 
# print(example) -> THIS WILL PRINT 100 since local() function isnt being called

'''---------------------- Global Variable --------------------------------------'''
# def local():
#      global example    #-> this makes example as GLOBAL variable and WONT change to "apple"
#      example = "banana"
#      print(example)
# 
# example = "apple"
# local()

'''-------------------------------------------------------'''
# phrase = "webster Silent"

# print(phrase.upper())
# print(phrase.upper().isupper()) -> inserting functions into print 
# print(len(phrase)) -> how many characters inside the string
# print(phrase[0]) -> displays the first letter from phrase Variable (w)
# print(phrase.index("e")) # displays where letter is indexed/located (1) 
# print(phrase.replace("<word>", "<ReplaceWith>"))
#    Google for More String Functions

# print(Hello[0]) -> prints "H"

'''------------------------ Working with Numbers --------------------'''
# print(2+4) -> you can do math 
# print(10 % 3) -> 10/3 = 1 (3*3+1)

# myNum = 5 
# print(str(myNum)) -> convert myNum(5) into a string
# print(str(myNum) + " my favorite number") -> if (str) is removed, python will not add myNumb + string
# print(pow(3, 2)) -> 3 raised to power of 2 = 9
# print(max(4, 6)) -> displays biggest number (6)

# 123_456_789 -> In Python, it removes the underscores and makes it as 123456789
# We key like this, for us HUMANS easy to read numbers

#   FROM MATH IMPORT *  ->  (all lower case) -> this gives access to more math functions

'''------------------------ Get Input from User ---------------------'''
# name = input("Enter your Name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "! You are " + age)

'''----------------------- Create Calculator------------------------'''
# num1 = input("Add - Enter First Number: ")
# num2 = input("Add - Enter Second Number: ")
# result = int(num1) + int(num2)
# print(result)
# 
# num11 = input("Subtraction - Enter First Number: ")
# num22 = input("Subtraction - Enter Second Number: ")
# result2 = int(num11) - int(num22)
# print(result2)

'''---------------------- Mad Libs ----------------------------'''
# color = input("Enter Color: ")
# oun = input("Enter Nount: ")
# celebrity = input("Enter Celebrity name: ")

# print("Roses are " + color)
# print(noun + " are blue")
# print("I love " + celebrity)

'''----------------------- Print List ------------------'''
# List may contain diversity of items such int, string, boolean, floats.
# they are called "Items" as well
# Each Item in the List has its own "Index" number
# List made of [] 

#lucky_numbers = [4, 5, 8, 15, 22, 345]
#friends = ["kevin", "Karen", "Viktor", "Kyle", "Smith"]
#example_list1 = [True, False, False, True]
#example_list2 = [[10, 3, 4], True, False, "three", "two", 1, 2, 3] # list can have diversity of data
#^^
#friends.insert(1, "creed") # (location(index), what its adding)
#friends.append("Kell")
#friends.extend(lucky_numbers)
#friends.remove("Smith")
#friends.pop()              # Removes Last item from the List. Can also pass in Argument
#print(friends.pop())  # shows last item from the list and if do "print" again, it shows as removed
#friends.clear()
#lucky_numbers.reverse()
#friends.sort()
#friends.sort(reverse=true) # list in Reverse order
#print(friends.index("Smith")) # Returns an Integer, the location of that word
#print(friends.count("Smith")) # Returns Word count of that Word

#friends2 = friends.copy()
#friends[2] = "Vlad"
#print(friends2)
#print(lucky_numbers)
#print(list("Vladimir")) # prints [V, l, a, d, i, m, i, r]

## List must be in Order to be equivalent (to equal)
# print([2, 4, 6] == [2, 4, 6]) # true
# print([2, 4, 6] == [4, 6, 2]) # false

### Return a List made out of following elements [9, 10, 11]
#r = range(3, 21)
#my_slice = list(r)[6:9]
#print(my_slice) -> [9, 10, 11]

'''-------------- Sort ------------------'''
# friends.sort(reverse=true) # list in Reverse order. 
# Sort cannot be used on Mixed list Data type(str, int, boolean)
# but it DOES reads True as 1 and False as 0
# so, when sorting mixed = [False, 5.67, -2]
# reads [-2, False, 5.67]

'''--------------- Alphabetical Order vs ASCIIbetical order -----------'''
## In ASCIIbetical order = Uppercase comes First, then Lowercase comes Second
## This is done by default

# mixed = ["Andy", "kiwi", "apple", "Karen", "Brian"]
# mixed.sort()
# print(mixed)

## To Sort by ALPHABETICAL Order
# mixed = ["Andy", "kiwi", "apple", "Karen", "Brian"]
# mixed.sort(key=str.lower)
# print(mixed)

'''----------- more examples ----- '''
'''------------------------------ List Slice (slicing) ----------------------------'''
### Slice function contains 3 argument but first 2 must be used, 3rd is optional
## Slice[start:end:step] -> step-> prints out every value mention as "step"
##  default for step is 1

# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(my_list[2:-1:2]) # [2, 4, 6, 8]= starts at 2, goes to -1 which is 9, then print out every 2nd value
# print(my_list[-2:2:-3]) # [8, 5]
# print(my_list[::2]) # [0, 2, 4, 6, 8]
'''------------------------- Slicing a string----------------'''
# url = 'http://corey.com'
# print(url[::-1]) # reverses entire url (moc.yeroc//:ptth)
# print(url[7:]) # corey.com

##### When slicing, it starts from 0, then goes on
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(number[:4]) # [1, 2, 3, 4]
# print(number[3:4]) # [4]
# print(number[3:8]) # [4, 5, 6, 7, 8]
# print(number[6:])  # [7, 8, 9]

'''--- Slicing tuple ---'''
# ints = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#      Starting from Index of a Number
# print(ints[::3]) -> Display Length of every 3rd (1, 4, 7, 10)
# print(ints[1::3]) -> Display Evens only (2, 4, 6, 8, 10)
# print(ints[7::-1]) -> Displays Backwards from 8 (8, 7, 6, 5, 4, 3, 2, 1)
# print(ints[8::-2]) -> Displays Odds only in Backwards (9, 7, 5, 3, 1)

'''----- Nested Tuple  / count/index ---'''
# nested = (1, 2, 3, (4, 5, 6), (7, 8, 9), (10, 11, 12))
# print(nested[4]) -> (7, 8, 9)
# print(nested[5][1]) -> 11

# repeat = (7, 3, 3, 3, 0, 0, 7, 0, 0)
# print(repeat.count(7)) -> "2" display number of times number appears in variable
# print(repeat.count(3)) -> "3"
# print(repeat.count(0)) -> "4"

# ints = (1, 1, 7, 8)
# print(ints.index(7)) -> "2" If you don't know the index of item being located, use ".index" to search. Number 7 is indexed under 2
# print(ints.index(1)) -> "0" Number 1, even tho its represented twice, will show only the first indexed number
# print(ints.index(8)) -> "3"

#####Reassigning Value to the List
# number[3] = 10
# print(number) # [1, 2, 3, 10, 5, 6, 7, 8, 9]
# number[1:4] = [3, 2, 1]
# print(number) # [1, 3, 2, 1, 5, 6, 7, 8, 9]

#### You can also append to the List even tho the list is short.

### Reassigning OLD VARIABLE to NEW VARIABLE
# The fact that "ex_1" and "ex_4" is now SAME list, python treats them as SAME list also
# Behind the Scenes: [1, 2, 3, 4, 5] becomes a reference to "ex_1", then copies and assigns to "ex_4"

'''------ Slicing(slice) certain characters from ex_1 and adding them to "Yes"----'''
# ex_1 = "No, you can't"
# ex_2 = "Yes" + ex_1[3:11] + "!"
# print(ex_2) # Yes you can!

'''========================== Tuple ==============================================='''
# Tuples - CANNOT be altered (Immutable, Ordered=order don't change)(tuples1 = ()

tuple1 = ("Cisco", 24, "12", "Condo")
# Number of elements must match in tuple1 variable
(Vendor, Model, IOS, Name) = tuple1
print(Vendor)  -> prints Cisco
print(Model)  -> prints 24
print(IOS)   -> prints 12
print(Name) -> prints Condo 

(a, b, c) = (10, 20, 30)
print(a) -> 10
print(b) -> 20
print(c) -> 30

a = ()
b = []
dir(a) -> will list all Methods and Attributes used in Tuple (add, format, len, str...)
dir(b) -> will list all Methods and Attributes used in List (add, len, eq, ge, sort, remove...)

''' Iterate thru tuple using "for loop" ---'''

# major_cities = ("Canada", "London", "New York", "Lava Land")
# for city in major_cities:
#      print(city)

''' Iterate thru tuple using "while loop" '''
# count = 0
# while count < len(major_cities):
#      # major_cities is being iterated by [count] starting from 0
#      print(major_cities[count])
#      count += 1

''' Iterate thru tuple going Backwards '''
# count = 0
# backwards = len(major_cities) - 1  # backwards becomes 3 (major_cities = 4-1=3), "len" becomes 3. Setting the Backwards variable
# while backwards >= count:          # The count of major_cities begins from 3, 2, 1, 0. While 3 >= 0
#      print(major_cities[backwards]) # major_cities prints from 3, then 2 and so...
#      backwards-=1                       # the Count goes backwards

'''---------------------- Storing value (Tuple, List)------------------------'''
### Tuple is a Data type, like a list, except its mutable and can be used in curly brackets. Much similar to Dictionary
### Why Use a tuple?
# When you want to have collection of data that you know you will NOT change later on in the program
# This will prevent unwanted data/list changes within the list of Tuples
# exemple of data won't change : Days of the week, Name of Seasons, Order of the alphabet

### Reason to Use Tuples over List or another mutable data type
# It takes less space in memory and faster running in results

#coordinates = [(4, 5), (6, 7), (8, 9)]
#print(coordinates[1])

#tuple_1 = tuple("such")
#print(tuple_1) # ('s', 'u', 'c', 'h')

##### Tuple can contain different set of data types
# tuple_1 = ("a", "b", "c") -> these are Items inside ()
# tuple_2 = (2.483, False, [1, 2, 3])
# tuple_3 = (1, 1, 0, 0, 0)
# tuple_4 = tuple("vlad") 
# tuple_5 = tuple([3.14, 2.30, 10])
# tuple_6 = tuple({"a": 1, "b": 2}) -> Dictionary Style
# tuple_7 = (1, 2, 3, 4,5)

# print(tuple_4) -> ('v', 'l', 'a', 'd')
# print(tuple_5) -> (3.14, 2.30, 10) turns into a List
# print(tuple_6) -> ("a", "b") -> turns From Dictionary into List. No point of doing it cuz ONLY KEYS be made into tuple
# print(tuple_7[2:]) -> this called "Slicing a string", "slice" which can also be done with tuple

### Tuple memory size check
# tuple_12 = (1, 2, 4)
# list_1 = [1, 2, 3]

# print(tuple_12.__sizeof__()) -> 48kb
# print(list_1.__sizeof__()) -> 64kb (list takes up more size in memory)

'''--------------------- Into to Sets -------------------------------------------'''
# A Data type that consists collection of items, much like a list. 
# "Set" is triggered by having Curly {} brackets
# Sets differ from List in two ways:
# First; cannot have duplicates Values in them
# Second; items that contain are unordered like the key value pairs of a dictionary
# Items in a "Set" are "Unordered"
# Sets can hold Items of different Data Types
# Sets Items cannot be accesed by Index

# Sets are useful in situations where you want to use Collection of Items BUT you don't want duplicate Items in a Collection. 
     # and you also Don't care about the Order of the Items that make up collection. 

# Two ways of creating Sets:
# set_1 = {9, 8, 7, 6}  #-> this known as "Set Literal"
     # set_1 = {9, 8, 8, 8, 7, 6} -> the Duplicates will be ignored (8)
     # This way ^(with just curly brackets), Empty Set, will create just Dictionary

# set_2 = set({"a", "b", "c", "d", "e"}) #-> this is "Set Function". It takes on Set as an argument and returns it. 
     # This way ^(with SET function), user can create an Empty Set and make changes later
# print(set_1)
# print(set_2)

### An Empty "Set"
# set_3 = set() -> empty set
# set_4 = set(start, stop, step)
# set_5 = set(range(1, 12, 2)) -> (1, 3, 5, 7, 9, 11))
# print(set_5)

### Sets may hold different Data types
# set_6 = {"a", 2.12, 18, True}
# print(set_6)

### Access Sets Items with For Loop (can't via Index)
# set_7 = {3, 6, 9, 12, 15}

# for num in set_7:
#     print(num)

### Find if Value is in Set_7
# print(12 in set_7) -> result to True

#### THis is where "Sets" would be Userful
# If you are given a big list of clients that have recently purchased product from you. That list also contains
# same clients multiple times because they have purchased your product multiple times. And you want to list them
# don't matter in what order but Must be DISTINCT clients.

# client_list = ["list of clients, didn't type here to save time"]
# print(set(client_list))  -> by adding "set" to Variable, it is gonna filter Distinct Clients.
# print(len(client_list))  -> gives you number of how many Clients are on that list. Including Clients written twice
# print(list(len(set(client_list)))

'''------------ Set Methods -----------------'''
# method = {"heaven", "moon", "Sun"}
# method.add("star") #-> adds "star" to the list
# method.remove("star")
# method.discard("star") #-> same as Remove but without giving Error messages if Item does NOT exist
# method.clear() #-> everything in a set will be removed
# set_2 = method.copy() #-> copies the "Method" variable
# print(set_2 is method) #-> will Return True or False

# print(method)
#==========================
# "union" combines Sets together
# set_1 = {1, 2, 3, 4}
# set_2 = {5, 6, 7}
# set_3 = {8, 9, 10}

# set_4 = set_1.union(set_2, set_3)
# print(set_4)
#OR
# set_4 = set_1 | set_2 | set_3
# print(set_4)
#===========================
# Intersection() - allows to find what "items" two "Sets" have in common
# set_1 = {1, 2, 3, 4}
# set_2 = {4, 6, 7}
# set_3 = {7, 9, 10}

# set_4 = set_1.intersection(set_2, set_3)
# print(set_4)
#OR
# set_4 = set_1 & set_2 & set_3
# print(set_4)
#===============================
# subtraction and difference()
# set_4 = set_1 - set_2 
# print(set_4)

# set_4 = set_1.difference(set_2)
# print(set_4)
#================================
'''-------------- Set Comprehensions -------------------'''
# Sets are usually Unordered

# comp_1 = {even+2 for even in range(2, 11, 2)} #-> (even+2) is a Method(action). (range(2, 11, 2) - start, stop, step)
# print(comp_1) #-> {4, 6, 8, 10, 12}

### Sets are usually Unordered, that is why "ALLCAPS" resulting in diff order
# comp_2 = {char.lower() for char in "ALLCAPS"} #-> (char.lower()) is a Method. "ALLCAPS" makes it to iterate in unorganized manner
# print(comp_2) #-> {'c', 'l', 'p', 's', 'a'} -> its unordered and all Lower. 

'''-------- Mutable - Stored as references (can be changed) ----------'''
# ex_1 = [1, 2, 3, 4, 5] # this stored as reference
# ex_4 = ex_1
# ex_4[2] = 10  # reassigning the value for index 2, also affects the prev variable "ex_1"
# print(ex_1) # [1, 2, 10, 4, 5]
# print(ex_4) # [1, 2, 10, 4, 5]

# Immutable = Cannot be changed
# ex_1 = "Vandeta"
# ex_2 = ex_1
# ex_2[2] = "s"  # THis will NOT work. Cannot be changed
# print(ex_1)
# print(ex_2)
'''--------------------'''
# Lists = Mutable, meaning it can be changed, removed, added
     # Mutable stored as References (can be changed)
# Strings = Immutable, meaning it cannot be changed (When they are in a form of a List)
     # Strings can only be reassigned entire new Value, but cannot be append to it, changed via Index
     # Immutable stored as themselves (hard coded values) (int, float, strings, Boolean values)
'''---------------------- DeepCopy() ----------------------'''
# deepcopy function allows to *create a copy* of a list with its own reference instead of reference to the same list.
# deepcopy makes copy of "ex_12" list and allows it to make changes on reassigned variable without effecting ORIGINAL (ex_12) variable
# import copy
# ex_12 = [1, 2, 3, 4, 5]  # original variable (reference)
# ex_13 = copy.deepcopy(ex_12) # this makes copy of "ex_12"
# ex_13[4] = 10 # reassigning values, but will NOT effect original variable (without "deepcopy", it WILL effect original variable "ex_12")
# print(ex_12) # [1, 2, 3, 4, 5]
# print(ex_13) # [1, 2, 3, 4, 10]
# ex_14 = ex_13 # this becomes Mutable (changeable) AND now WILL effect NEW ORIGINAL value (ex_13)
# ex_14[1] = 5 
# print(ex_12) # [1, 2, 3, 4, 5] old original value
# print(ex_13) # [1, 5, 3, 4, 10] New original value
'''-------------------- del from list--------------------'''
### Deletes from the list. Must specify [number]
### Deletes based on the Index number of the item

# planets = ["pluto", "mars", "earth", "venus"]
# del planets[0]
# print(planets) # mars, earth, venus
'''----------------- remove method -------------'''
### Removes from the List. Must specify actual name, string from the List
### Removes based on the Argument passed in. Removes when finds it regardless location within the List

# planets = ["pluto", "mars", "earth", "venus"]
# planets.remove("pluto")
# print(planets)
### OR
# planets = ["pluto", "mars", "pluto", "earth", "venus", "pluto"]
# planets.remove("pluto")
# print(planets) # this will Remove ONLY the FIRST Instance (item) from the List, other "pluto" will remain

'''---------------------- in/not in = boolean (Within the List) --------------------- '''
# checked_list = [1, 2, 3, 4, 5]
# print(1 in checked_list) # True, checks if '1' exist in "checked_list" list
'''------------'''
# checked_list2 = [2, 4, 6, 8]
# print(3 not in checked_list2) # True
# or
# not_in_example = 3 not in checked_list2
# print(not_in_example) # True
'''------------------------ index --------------------------'''
# index_example = ["kalmykov", "smith", "nobody"]
# print(index_example[1]) # smith
# print(index_example[2][0]) # n
# print(index_example[-2][-1]) # h # When in reverse, it starts from 1 not 0 (from the back)
 
# index_example = [[1, 2, 4], [4, 5, 6], [7, 8, 9]]
# print(index_example[2] [0]) # 7
# print(index_example[-1]) # goes in reverse, starting from back [7, 8, 0]

'''----------------- Items in expression, Index Concatinate ---------------'''
# mixed = [False, 345, 2.1, "this is a string"]
# print(mixed[2] + 1.0) # this is an "Expression"
# print("i have used \"" + mixed[-1] + "\" too many times")
# output: I have used "this is a string" too many times

'''------------------------- Functions-------------------------'''
# def sayhi(name, age):
     #print("Hello " + name)
     #print("I am " + str(age))
# print("top") - executes first
# sayhi("vlad", 35)  - executes second
# sayhi("vlad", "35") --
# print("button") - executes last

'''------------ Return Statement - gets you back information------------'''
# def cube(num):
#    return num*num*num
            # no code will work after RETURN 
# result = cube(3)    
# print(result)

####### OR

# def name_printer(parm):
#     print(name)
# name=input("enter full name: ")
#  
# name_printer(name)
#OR
# def five(x):
#    y = x + 5
#    return y
#print(five(3)) -> 8
#OR
# def plus(x):             -> x is parameter
#     return x + 10         -> 'return' plays as invisible "y" (y = x + 10)
# print(plus(10)) -> 20      -> must ALWAYS call FUNCTION NAME first "plus" then <value>
#OR

# def simple(a):
#    lucky = a + 5
#    print("result")
#    return lucky
#
# simple(10) -> prints "result" and "15" cuz 'print' and 'return' is within a function of 'simple'

'''------------------ Default Parameters / PRINT vs RETURN--------------'''
# if no parameters are given at the CAlling of Functions, then defaulted parameters will be called. Otherwise, they can be overwritten.
# def example(num1=7, num2=10):
#    return num1 * num2                 Return

# print(example() + 20)
'''-------------------------------------------'''
# def example(num1=7, num2=10):
#     print(num1 * num2)                Print

# example(2, 10)
# or 
# example(10) -> second parm will be defaulted
#   with "print", you cannot add number to a function (like in example above)
'''------------------------------------------'''
# Print vs Return = Print is a function that you call.
#    When "return" statement is reached, python will STOP execution of current function, 
#        and will send value out to where the function is being called. Use "return" when you want to send
#        value from one point in your code to another.
'''------------------------------------------- '''
# length=int(input("What is Length: ")) -> input numbers is going into variable
# width=int(input("What is width: "))
# height=int(input("What is height: "))
# 
# def prism(L, W, H): -> Parameters, because 3 values are needed, so 3 parameters
#      return L*W*H   -> what are these parameters suppose to do? Multiply together
#                     -> "Return" function must be on same line with (L*W*H), representing the RESULT
# print("The volume of the rectangular prism is " + str(prism(length, width, height)) + " cubic feet")
#                                                            ^^^numbers from used Variables above are INPUTED already in this Argument
#                                                                and these Arguments REPRESENT (L, W, H) parms      
'''----------------------------------------------- '''
# celsius=int(input("Enter celsius: "))
# 
# def temp(C):
#      return round((1.8*C+32), 1) -> round to nearest 1 decimal (2.1), nearest 2 decimal (2.12)
# 
# print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(temp(celsius)))
#
# print(8/3, 2) --> round to 2 decimal places
# print(8 // 3) --> short version of rounding (round) = equals 2 (8/3) = 2.66666666666


'''----------------------- If Statements (Flow Control)--------------------'''
#### DRAW a FLOW DIAGRAM for True/False, for VISUALIZATION and easy Code ######
# == equal (used for comparison)
# = used to assign variables
'''---------------- True/False -----------------'''
# True and True = True
# True and False = False
# False and False = False
# False and True = False
# TRUE OR FALSE = TRUE (only one statement needs to be TRUE to be executeable)
'''------------------------- Examples --------------------------'''
# veg = input ("Type name of vegatables: ")
# 
# if veg == 'corn':
#      print("The vegatagle is corn")
# else:
#      print("Wront Vegie entered.")
'''---------- if/if/else/else--------------'''
# gpa = float(input("What is your GPA: "))
# ins = input("Are you Qualified? ")
# 
# if gpa >= 3.7:
#      if ins == "yes":
#           print("You are Qualifies for low APR loan")
#      else:
#           print("You need higher GPA to qualify. BUT you are Qualified")
# else:
#      print("You are not qulified, sorry")
'''--------- elif ----------------'''
# grade = int(input("What is your score? "))
# 
# if grade >= 90:
#     print("Your grade is A")
# elif grade >= 80:
#      print("Your grade is B")
# elif grade <= 70:
#      print("Your grade is F")
# else:
#      print("Please enter correct scale")
'''---------------------------'''
# from random import randint
# one_to_three = randint(1, 3)
# 
# if one_to_three == 1:
#      print("The roman numeral is " + str(one_to_three) + " is I")
# elif one_to_three == 2:
#      print("The roman numeral is " + str(one_to_three) + " is II")
# elif one_to_three == 3:
#      print("The roman numeral is " + str(one_to_three) + " is III")
# else:
#      print("Please enter correct number")
'''--------------------------'''
# is_male = True
# is_tall = False
 
# if is_male and is_tall:
#     print("he is male")
# else:
#     print("He is NOT a Male")
# 
# if is_male and is_tall:
#     print("YOu are TALL")
# elif is_male and not(is_tall):
#     print("YOu are MALE")
# elif not(is_male) and is_tall:
#     print("YOu are SOMETHING")
# else:
#    print("YOu are NEITHER")
'''--------------- Truthy/Falsey--------------'''
# string_example = input("Enter any string BUT not empty. ")
# 
# if string_example:  #-> If Something is Entered, its TRUE statement
#      print("Thank you for entering something.")
# else:
#      print("You did not enter anything.")  #-> If NOTHING (blank) is entered, its FALSE statement
'''----Note---'''
# For Integers, 0 is FALSEY value, 
#     If Integer Value is > 0, its TRUTHY
# For Floats, 0.0 is FALSEY value,
#     If Floats value is > 0.0, its TRUTHY
# If value is 'None', its FALSEY
# If all variables are STRINGS, its TRUTHY

'''-------- Example -----'''
# print(bool(0)) -> falsey
# print(bool(2)) -> truthy

# print(bool("")) -> falsey cuz its blank

'''--------------------------If Statements with Comparison-------------'''
# def max_num(num1, num2, num3):
#    if num1>=num2 and num1>=num3:
#        return num1
#    elif num2>=num1 and num2>=num3:
#        return num2
#    else:
#        return num3
# print(max_num(3, 4, 5))

'''------------------------ Create Advanced Calculator -------------------'''
# num1 = float(input("Enter first Number:"))
# operator = input("Enter Operator:")
# num2 = float(input("Enter Second Number:"))
# 
# if operator == "+":
#     print(num1 + num2)
# elif operator == "-":
#     print(num1 - num2)
# elif operator == "/":
#     print(num1 / num2)
# elif operator == "*":
#     print(num1 * num2)
# else:
#     print("Invalid operator")

'''-------------------- Dictionary-----------------------------'''
'''------Google for more Dictionary Methods ------'''
## made out of ("key": "Value") pairs
## Keys can be Int, Boolean, floats or anything
## Dicrionaries can be unordered
## identifies by Curley {} brackets
###### ONLY WORKS if search by the KEY NOT VALUE

# integers = {9: "corum", 10: "diamond"}
# floats = {1.23: 1000, 3.14: 3.134455, 2.33: 877788}
# mixed = {"string": 1, 2330: 4442, 3.44: 22.2, False: 4}
#################
# first = {2334536465: 2343534534, 344: 344} # this is just example
# second = {234534534: 2234343242, 543: 434} # this is just example
# print(first == second) # True ## Keys and Values don't have to be in same order to be "True". As long they matching in key and value

# dic[2] = "apple" -> add key(2), value("apple") to 'dic' dictionary
# del dic[2] -> deleting key:value(2)
# print(3 in dic) -> verify if element 3 exist in dic
# dic['RAM'] = '256' -> update value to RAM key element

'''---------------- dict() function -> an alternative to Dictionary----------'''
### An alternative way to creat Dictionary in Python
### dic(a=1) - no spaces
### Numbers cannot be used as Keys
### dict(a1=1, b_=2, c_3=3) - this is acceptable
### dict(11=1, False=2, 12=3) - this is NOT acceptable
### Some other restrictions applies to Dict() function as to what can go inside ()
### Although Numbers and Boolean are ALLOWED as Keys in normal Dictionary list with {}

# empty = dict() 
# print(empty) -> {} an empty dictionary
# new_value = dict(a=1, b=2, c=3)
# print(new_value) -> {'a': 1, 'b': 2, 'c': 3}

'''------------ function within function ---------------------'''
#### first function, determines how much get paid per day
# def wage(with_hours):
#     return with_hours * 25  
#### using "wage" function, determines how much paid per day + bonus(using calculations from previous function)
# def bonus(with_hours):
#     return wage(with_hours) + 50

#print(wage(8), bonus(8))

'''--------------------------------'''
### Each tuple (key: value) contains two Items (key and value)

# monthConversion = {
#    "jan": "January",
#    "feb": "February",
#    "mar": "March",
# }

# print(monthConversion["mar"]) # March
### or
# val = monthConversion["feb"]
# print(val) # February
### or
# print("Todays is " + monthConversion["February"] + "the 23rd")
### or
# print(monthConversion.get("luv")) # by default = None, since there is no Key "luv"
# print(monthConversion.get("feb")) # February
### or
# print(monthConversion.get("luv", "not valid key")) # gives a defaulted error the one you choose "not valid key"
'''------------ get just Keys from dictionary-----'''
# print(monthConversion.keys()) # this will display all keys within a dictionary
### A <place holder> name in a For Loop <key> can be anything. But it should have a name which describes what the loop is iterating thru. 
# for key in monthConversion.keys():
#      print(key)
'''------------ get just Values from dictionary-----'''
# print(monthConversion.values())
# for value in monthConversion.values():
#      print(value)
'''------------- get only Items from dictionary-----'''
# print(monthConversion.items())
# for items in monthConversion.items():
#      print(items)
'''------------ get only Key and Value from dictionary-----'''
# print(monthConversion.items())
# for key, value in monthConversion.items():
#      print(key, value)
'''------------'''
# print(type(monthConversion.keys())) # <class 'dict_keys'>
# print(type(monthConversion.values())) # <class 'dict_values'>
# print(type(monthConversion.items())) # <class 'dict_items'>
# print(list(monthConversion.keys())) # ['jan', 'feb', 'mar']
'''-------in/not in within Dictionary -----------'''
# first = {0: 2.1, 1: 2.2, 2: 3.4, 4: 3.4}
# print(0 in first) # True
# print(1 not in first) # False, meaning it does exist
# print("February" in monthConversion.values()) # True
# print(len(monthConversion)) # 3, gives amount of items/tuple in dictionary

# computers = {"google": "chromebook", "apple": "Macbook", "microsoft": "surface pro"}
# if "Lenovo" not in computers:
#      computers["Lenovo"] = "thinkpad"
# print(computers) # adds new key 'Lenovo' with value 'thinkpad' to Dictionary if it does not exist already

'''------- fromkeys() from dictionary--------'''
### this method takes one or two arguments
### it takes any data type

# ex_1 = {}.fromkeys(["address"], "1600 Pennsylvania Avenue NW")
# print(ex_1) # {'address': '1600 Pennsylvania Avenue NW'}

# ex_2 = {}.fromkeys("addr", "1600 Pennsylvania Avenue NW")
# print(ex_2) # each letter of "addr" becomes a Key but second 'd' will be removed. Only 'a' 'd' 'r' will stay
#            # each character from Keys can be used only once
# ex_3 = {}.fromkeys(["address"])
# print(ex_3) # {'address': None} value: "none" will be used
'''------- pop() / popitem() from dictionary -----'''
### Pop = Since dictionaries can be unordered, in order to use 'pop', user must specify Key to remove
### popitem = Removes last Key from Dictionary. Does not take arguments
### If used Python earlier 3.7 = popitem will remove random item from Dictionary

# ex_1 = {"make": "Honda", "model": "civic", "year": 2016}
# ex_2 = ex_1.pop("model")
# print(ex_1)

# ex_2 = ex_1.popitem()
# print(ex_2)
# print(ex_1) # ex_1 can be printed because 'ex_1.pop.item()' don't need variable to be assigned to
'''------ clear() / copy() / update() / setdefault() --------'''
### Clear = removes everything from dictionary. Resulting in Empty dictionary
### Update = Adds key and value to Dictionary. Takes one argument

# ex_1.clear()
# print(ex_1) 

# ex_12 = {"made": 1, "suck": 2, "color": 3, "mood": 4, "panic": 5}  # original variable (reference)
# print(ex_12)
# ex_10 = ex_12.copy() # now 'ex_12' has its own copied reference
# ex_10["suck"] = 9
# print(ex_12)
# print(ex_10) 
# do more research on .copy() its confusing

# ex_9 = {"super": 111}
# ex_12.update(ex_9)
# print(ex_12) # adds "super": 111 to dictionary
# ex_9["super"] = 222
# ex_12.update(ex_9)
# print(ex_12)

### If Key 'Lenovo' is not in Dictionary, it will assign Value 'thinkpad'
### If Key 'Lenovo' existed in Dictionary, it will NOT assign new Value to it
# computers = {"google": "chromebook", "apple": "Macbook", "microsoft": "surface pro"}
# computers.setdefault("Lenovo", "thinkpad")
# print(computers)
# computers.setdefault("Lenovo", "ProMac")
# print(computers) # this will NOT change the Value 'ProMac' to 'thinkpad'

'''-------------------- While Loop -----------------------'''
### While Loop runs until Condition meet FALSE

# counter = 0           # Set Variable to BEGIN FROM
# while counter < 3:    # Condition
#     print("Something")  # Action while True
#     counter += 1        # Condition When to END, If no END Condition, Loop runs Infinite
# ---------------------------------------------
     # is 5 not equal 0? True
     # is 0 not equal 0? False, therefore Loop is over
# user = int(input("Users number entered: "))  # Convert to INT so numbers can be Summed
# initial = user  # Storing "user" value into "initial" (OPTIONAL)
# summed = 0      # This Variable will HOLD the SUM of all integers starting from 0
# while user > 0:
#       summed = summed + user  # NEW value of "summed" = OLD value of "summed" + NEW value of "user" (summed += user)
#       user = user - 1         # Condition to END (user -= 1)
# 
# print("This is initial value " + str(initial)) # Converting to String so it can Concatinate
# print("Sum of all numbers: " + str(summed))
'''------------------------------------------------'''
# i=1
# while i <= 10:
#     print(i)
#     i = i + 1
#    i += 1
# print("Done with loop")
'''-----------------------------------------------'''
# secret_name = 'vlad'
# name = ''
# guess_count = 0
# guess_limit = 3
# numberOfGuesses = False

### while name != secret_name and not (numberOfGuesses):
#    if guess_count < guess_limit:
#        name = input("Guess my name: ")
#        guess_count = guess_count + 1
#    else:
#        numberOfGuesses = True
#
# if numberOfGuesses:
#    print("Out of guesses, You Loose")
# else:
#    print ("You got it!!!")

'''------------------------- For Loop-----------------------'''
# "letter" is a VARIABLE and "kalmykov" is a value
# For each value in a variable, print and repeat
# for letter in "Kalmykov":
#   print(letter, end=":") -> K:a:l:m:y:k:o:v

# friends = ["vlad", "Jim", "Karen", "Smith"]
# for each_friend in friends:
#   print(each_friend)

# for index in range(3, 10):  # "range" makes it go from 0 to infinity (used mostly with numbers)
#   print(index)

# friends = ["vlad", "Jim", "Karen", "Smith"]
# for each_friend in range(len(friends)):
#    print(each_friend)
'''---- another way of For Loop----'''
# A <place holder> name in a For Loop <key> can be anything. But it should have a name which describes what the loop is iterating thru. 
# for key in monthConversion.keys():
#     print(key)
# example for monthConversion is in "Dictionary"
'''---------------------------------------------'''
# Assignment: Calculate number of Characters for Each word user enters
# word=input("Enter any word: ")
# number_of_characters = word  # Storing "Word" in different Variable
# for letter in word:
#      print(word)
#      break                 # break loop, does not allow it to list repeatedly 
# print(len(number_of_characters))  # "len" counts number of characters
'''------------ Different version code -----------'''
# word=input("Enter any word: ")
# count = 0
# for letter in word:
#      count = count + 1
# print(word)
# print(count)

'''-------------------- Exponent Function-------------------'''
# number = 5
# number **=3 (this means 5 raised to 3rd power = 5*5*5) = 125

# 2 raised to the 3 power (2 * 2 * 2)
# print(2**3)

# def save_to_power(base_num, pow_num):
#    result = 1
#    for index in range(pow_num):
#        result = result * base_num
#    return(result) #'return' must be part of (aligned with) For loop otherwise it won't work
# print(save_to_power(2, 3))

'''-------------------- 2D Lists & Nested Loops ------------------------'''
# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]

# print(number_grid[1][1])

# for row in number_grid:  # This uses above number_grid to do Nested loops
#   for col in row:
#       print(col)

'''------------------------ Build a Translator / Replace---------------'''
# def translate(phrase):
#     translation = ''
#     for letter in phrase:
#         if letter in 'AEIOUaeiou':
#             translation = translation + 'g'
#         else:
#             translation = translation + letter
#     return translation
# 
# print(translate(input("Enter Phrase: ")))

'''-----------------------Reading Files --------------------------------'''
# file = open('test.txt') # Open text file
# file.close()          # Close file. Make sure you close file. 
# Before closing file, write code in Between.
######### Alternative way of OPENING file
# with open('employee_file', 'w') as file:      # this way, file will OPEN and CLOSE automatically
#     content = file.readlines()
#     reversed(content)           # this will reverse entire file content (not backwards letters). Now, you must Write 'reversed' content back to file
#     with open('employee_file', 'w') as file2:       # Writing 'reversed' content back to File 'employee_file' not file2-> that is just object.
#          for line in reversed(content):   # FOR LOOP is storing 'reversed' content back to file
#               file2.write(line)
########
# open("<fileName>", "<mode>") 'r' is Read, 'w' is Write, 'a' is Append to file, 'r+' is Read and Write

# storing file content in 'employee_file' variable
# employee_file = open("employees.txt", "r")    # if file location in same folder
# print(employee_file.readable())  # gives boolean If file is actually readable. If 'w', file would not be readable (False)
# print(employee_file.read())      # actually reads the file, spits out the content of file
# print(employee_file.read(5))     # number of characters is will print 
# print(employee_file.readline())  # reads first line
# print(employee_file.readline())  # reads second line, and so on...(no parm required)
# print(employee_file.readlines())  # reads each line and putting inside array, making a list
# print(employee_file.readlines()[1]) # returns position of 1 inside the array

# for employee in employee_file.readlines():    # 3 for loop can be used as well
#    print(employee)

'''------------- Read file using While Loop------------'''
# While Loop will continue UNTIL condition returns FALSE

# line = employee_file.readline()
# While line != "":                       # Determines if Condition is TRUE to run
#     print(line)                         # Prints next line in file
#     line = employee_file.readline()     # After it prints, it looks for another line to read. (Next step after execution)

# employee_file.close() # good practice to CLOSE file

'''------------------------------ Writing/Append to Files---------------------'''
# employee_file = open("employees.txt", "a")   # this will add content to the file
# employee_file.write("Adding content to this file with parameter of A")
# employee_file.write("\n Adding another Content with line break")
# 
# employee_file.close()
# --------------------------------------------------
# employee_file = open("employees.txt", "w")   # this will override entire file by replacing everything with new line
# employee_file.write("Adding content to this file with parameter of A")
# 
# employee_file.close()
# ----------------------------------------------------
# By adding different fileName with parm 'w', this will create new file with content
# employee_file = open("employees12.txt", "w")   # this will override entire file by replacing everything with new line
# employee_file.write("Adding content to this file with parameter of A")
# 
# employee_file.close()
'''--------------------------- Exception - throwing specific error messages (Assert)(automation testing) -------------------'''
#### This is how you would Assert or Pass or Validate/Varify Automation test
#### 'raise' allows user to raise manually an exception

# There should be 2 items added in the Cart
# ItemsInCart = 0

# if ItemsInCart != 2:
#      raise Exception("Product count is Not Matching!") # this throws actual error message with your error

# if ItemsInCart != 2:
#     pass                # if its not 2, this will Pass
# assert(ItemsInCart == 0) # this will Pass cuz "ItemsInCart" is not 2 but 0
# assert(ItemsInCart == 2) # this will thro Error cuz "ItemsInCart" not suppose to be 2

'''--------------------- Try, Except block --> Error Blocks (automation testing)----------------'''
# Put code into block and see if it works before throwing an official error
# Except function will print error if code is not valid, have errors, or invalid INPUT from user

# try:
#     number = int(input("Enter a number: "))
#     print(number)
#     value = 10/0           # problem here is 10 cannot be divided by 0
# except ZeroDivisionError as err:        # text after 'except' is not necessary to have, can leave it blank
                                          # 'ZeroDivisionError' made up message cuz it makes it more clear as why there is an error
#     print(err)  # will print 'ZeroDivisionError' cuz 10 cannot be divided by 0
# except ValueError: 
#     print("invalid input") # will print if user input will be Invalid
'''----------'''
# user can have 2 except errors at a time
#     except FileNotFoundError:
#          print("File not found")
#     except Exception as e:
#          print(e)
###################
'''---- try, except, finally --- '''
# try:
#     with open('test.txt', 'r') as reader:  # this "test.txt" file does not exist
#          reader.read()
# except:
#     print("Some how there is a failure in this block")  # I'm checking if the file exist, if NOT, throw this error message
# OR 
# except Exception:
#    print("Sorry, there has been an error")
# Or
# except Exception as e:   # 'e' is referencing an actual 'Exception' code, a python error message
#     print(e)
# else: 
#    print("It runs")
#    reader.close()
# finally:
#     print("Command has executed successfully")
'''-------finally--^^--'''
# this keyword 'finally' will print this message, after 'try' block will Pass or Fail
# function within "finally" function will execute no matter if "Try except" block fails

'''---------------------------- Modules and Pip ----------------------------'''
# allows to access functions, written code, variables from different python file
# Google for 'list of python Modules'
'''---------------- Import Modules ---------------'''
# Type of Import:      Generic Import:
#     import<moduleName>  -> syntax is <moduleName>.<Function>(Arguments)
# import random
# print(random.randint(1, 10)) -> generates random number

# Type of Import;       Function Import:
#    When specific function is imported from a module (Randint imported from Random module)
# from random import randint
# print(randint(10, 20))

# Type of Import:        Universal Import:
#    Import every function from a module. and no need to type <moduleName>.<function>
# from random import *
# print(random())

'''----------------- Pip ------------------'''
# Pip allows to install python modules - use Terminal to install modules 
#           (check pip version "pip --version")
#       ex: pip install <nameOfPythonModule>
#           pip install python-docx
# Once installed, location is usually in -> Lib -> site-packages
# To use it in VScode key -> 'import docx' -> and now its usable
#  import useful_tools # this will import code from another fileName 'useful_tools' 


# print(useful_tools.<provide function from code><also may include parm with function>)

'''------------------------------ Classes & Objects --------------------'''
# Class is another Data type that can be used in Python. You can define own Data Type besides 'string', 'int', 'boolean', 'range'
# Class = Student
# Object is name, major, gpa and so on. Pretty much what is being represented inside the Class.
# Object is an Instance of a Class - an 'individual object of a certain class'
# Refer to "Student.py" file for more notes/info

# From 'student' file, import 'Student' Class
#       from student import Student

# Creating Student object
#       student1 = Student("Vlad", "Business", 3.1, False)

#       print(student1.name) # prints name - Vlad

'''------------------------- Building Multiple Choice Quiz --------------------'''
# from question import Question 
# question_prompts= [
#     "What color are apples? \n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
#     "What color are bananas? \n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
#     "What color are Strawberries? \n(a) Yellow\n(b) Red\n(c) Blue\n\n"
# ]
# 
# questions = [
#     Question(question_prompts[0], "a"),
#     Question(question_prompts[1], "c"),
#     Question(question_prompts[2], "b"),
# 
# ]
# 
# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer == question.answer:
#             score += 1
#     print("you got " + str(score) + "/" + str(len(questions)) + " correct")
# 
# run_test(questions)

'''------------------ Object Functions/Class Functions ------------------------'''
# from student import Student
# 
# student1 = Student("Oscar", "Accounting", 3.1)
# student2 = Student("Phyllis", "Business", 3.8)
# 
# print(student1.on_honor_roll())

'''--------------------------Inheritance -------------------------------'''
# define bunch of attributes and functions and things inside of a Class and then 
#   create Another Class and Inherit all of those Attributes.

# from Chef import Chef
# from ChineseChef import ChineseChef
# 
# myChef = Chef()
# myChef.make_special_dish()
# 
# myChineseChef = ChineseChef()
# myChineseChef.make_special_dish()

'''------------------------- Python Interpreter  -------------------> Python CMD line ---------------'''
# An environment where user can execute python commands/python functions (safe env)
# kind of quick and dirty way to write python

# In Terminal or in here (terminal) -> type: Python3
# >>> this three signs will appear meaning you can proceed with typing Code
#    anything can go here, functions, text, print, variables...
#    To exit, type: exit() OR Ctrl+Z (enter)

'''===================================================='''
# exponent = 4 ** 4 = 256 (4 * 4 * 4 * 4)
# floor_division = 16 // 5 = 3
# modulo = 7 % 3 = 1 (7 divided by 3, remainder 1)
# Flow of Operation = () / ** / %, /, //, *, +, -

# Slicing a String
#    var="apricots"
#        print(var[:3]) = apr
#        print(var[2:5]) = ric
#        print(var[4:]) = cots

'''-------------------- Type of file (Data Types)---------------------------'''
# Data type that can be used in Python. You can define own Data Type besides 'string', 'int', 'boolean', 'range', 'class'
'''-- Check INDENTATION to work ----'''
#var1=False
#var2=29
#var3=4.123
#var4="Word"
#var5=range(5)
 #print(type(var1)) <class 'bool'>
 #print(type(var2)) <class 'int'>
 #print(type(var3)) <class 'float'>
 #print(type(var4)) <class 'str'>
 #print(type(var5)) <class 'range'>

 #Float = 1.2 (decimal numbers)
 #Int = 1 (single numbers)
     # Int - also converts number into WHOLE Number (1.22 = 1)
 # ** means exponents
 # 2 ** 3 means 2 * 2 * 2 = 8
 # PEMDAS = order of operation () , **, */, +-

'''--------------------------- Range or between (data type) ------------------------'''
# "range" makes it go from 0 to infinity (used mostly with numbers) - google other functions for more
# if num in range(2, 9)
#     print("your number will start between 2 and 8")

# weight = int(input("What is your weight? "))
# if 25 <= weight <= 30:
#    print("Your weight is between 25 and 30 or >25 <30")

'''--------- One argument ------'''
# one_input = range(5) # this means Starts 0-5 (until 5 is reached but WONT print 5)
# for num in one_input:
#     print(num)
'''----------Two arguments ------'''
# two_input = range(5,10) # Starts at 5 ends 9
# for num in two_input:
#      print(num)
'''----------Three arguments -----'''
# three_input = range(1, 20, 3) # Starts at 1 ends 19, 3 is called "Step size", used to "increment"
# for num in three_input:
#      print(num)

# three_input = range(20, 1, -3) # this will do in REVERSE
# three_input = range(10, 25, 5) # Prints 10, 15, and 20
# three_input = range(6, -1, -2) # Prints 6, 4, 2, and 0 (in Reverse) 
'''============================================================================'''
####### replit.com/@vladimir18

####### Story Coding with Numbers
# BMI Calculator
# BMI = weight(kg)
#      -----------
#       height**
# 
# weight = float(input("your weight? "))
# height = float(input("your height? "))
# 
# BMI = weight / (height ** 2)
# print(int(BMI))  --> int converts into whole number
'''================='''
# result = 4/2 equals 2
# result /= 2  since result is 2 (2/2 = 1)
# print(result) -> 1.0
# 
# score = 0
# score += 1 same as score + 1 
# print(score)

# the weight challenge
# < 18 kg = underweight
# > 18.5 < 25 = normal weight
# > 25 < 30 = overweight
# > 30 < 35 = obese
# > 35 = clinical obese

weight = int(input("What is your age? "))

if weight <= 18:
     print("You are underweight.")
elif 18.5 <= weight <= 25:
     print("You are at normal weight.")
elif 25 <= weight <= 30:
     print("You are overweight.")
elif 30 <= weight <= 35:
     print("You are Obese.")
elif weight > 35:
     print("You are clinical obese")
else:
     print("You are in perfect shape.")
