# Full Stack Web Development Bootcamp - Bogdan Stashchuk - Udemy
# https://www.udemy.com/course/full-stack-web-development-bootcamp/learn/lecture/29429174#overview

#NOTE: Ctr+, settings
#NOTE: Ctr+Alt+N (start code), Ctr+Alt+M(Stop code, if takes too long)

#TIP:
#Global Variables = lives outside of 'Function'
#Local Variables = Lives inside the 'Function'
#print(type(variable))    -> use it alot
#Its good practice to add Description to Functions using 3 """. It goes Inside the Function. 
#Comparison/Expression Operators use == not =
'''Notes'''

#def function(parameter):
#    return parameter #which is <variable>
#    return 10        #will print 10

#def my_name(parameter="What is your name"): #> defaulted name, if none given at calling
#    print("My Name is", parameter.upper())  #> applying 'Method' to Parameter
#    print("My Name is" + parameter)
#    return parameter.upper()
    # If No 'return' called, so prints 'None'

#print(my_name("vlad"))          #Argument or Positional Argument

#def person_info(name, age):
#    print(name, age)

### Function can be called in different ways
#person_info("vlad", 20)   #> called 'Positional Arguments'
#person_info(name="Bob", age=25)
#person_info("Vlad", age=25)

#============================== *args
#def sum(*args):         # allows to run many arguments 
#    return args         # 'return' breaksout of function. Nothing runs after
#    print(type(args))
#print(sum(2,2,3,3,3))

#def plus(*args):        #*parm allows to apply multiple 'positional arguments' into parameter 
                                # Each # in argument will be executed one at a time 
                                 # Normally if one PARM specified, then ONE Argument allowed
#    print(args)
#print(plus(2, 3, 4))    # 2, 3, 4

#def sum(*args):             # function will iterate each argument one at a time
#    total=0
#    for arg in args:
#        total = total + arg
#        print(total)
#print(sum(2, 3, 4))    # prints: 2, 5, 9

#================================== **ArgSpec

#def person(**args):     # prints as Dictionary type
#    print(args)
#    print(type(args))   # indicates that 'args' type is dictionary

#print(person(name="bob", lastName="vlad", nickname="tim", age=20, favNum=35))

#def people(**args):
#    print(args.get("lastName"))
#    print(args["lastName"])
#print(people(name="bob", lastName="vlad", nickname="tim", age=20, favNum=35))

#============================ Function Description 
### Its good practice to add Description to Functions or Name Functions more meaningful.
### Description is added after Function name or inside the Function. Using 3 """
### Navigate mouse to Function <name> and see the message

#def sum(a, b):
#    """Sums of two numbers
#    Numbers must be Integers"""
#    return(a + b)
#print(sum(5, 2)) 

#=================================== Logical Operators AND / Truthy/Falsey
### Evaluates based on LAST Variable

### AND, OR = related to VALUE
### NOT = based on True, False
### If a = 'None', its FALSEY
### If all variables are STRINGS, its TRUTHY

#a = 5
#b = 0
#print(a == b) #False, String is NOT equals to Integer
#print(a and b) # 0
#print(bool(a and b)) #Falsey, 0 is always False

#c=5
#d=10
#print(c and d) # 10
#print(bool(c and d)) #Truthy, 10 is greater than 0

#=============================================== Short-Circuit Evaluation
### in this scenario, evaluates to Falsey because it short-circuited
### Means, it executed variables a, b and stopped because b is 0

#a='abc'
#b=0
#c=4
#print(a and b and c) # 0, 0 is where it breaks and becomes Falsey
#print(a and b and print("not called")) # Falsey, and 'not called' wont be executed
#print(bool(a and b and c)) #Falsey
#If b=2
#print(a and b and print("not called")) # 'not called' , would be executed
#print(bool(a and b and c)) #Truthy

#=================================== Logical Operators OR / Truthy/Falsey
### Evaluates based on First Variable
### this is Opposite of AND operator

#c=5
#d=10
#print(c or d) # 5, 5 is first variable
#print(bool(c or d)) #Truthy, because 5 is greater than 0

#a='abc'
#b=10
#print(a or b) # 'abc' 
#print(bool(a or b)) # True

#a = ""
#b = None
#print(a or b) # None
#print(bool(a or b)) # Falsey, None is always False

#a=""
#=None
#c=10
#print(bool(a or b or c)) # True, 10 is greater than 0
#print(a or b or c) # 10
#IF c = 0
#print(bool(a or b or c)) # False

#=================================== Logical Operators NOT / Truthy/Falsey

#a = 'a'
#print(not a) # False

#print(5 or "abc" and not 3) # mixing AND OR NOT 

#===================================== Try/Except
Try: lets you test a block of code for errors
Except: lets you handle the error
Else: lets you execute code when there is NO error 
Finally: lets you execute code, regardless of the result of 'try' and 'except' blocks

10/0  # will bring ZeroDivisionError

try: 
    10/0
except ZeroDivisionError as e:
    print(e)
#============================================== Modules - Create your OWN module
File_1
def sum(a, b):
    """sums of two numbers"""
    return a + b

File_2
this way: from File_1 import sum  # importing Function 'sum' from module
or this way: import File_1  # Calling Module 'File_1'

this way: print(file_1.sum(5, 6))  # Calling Module named "File_1" and calling function name 'sum'
or this way: print(sum(5, 6)) 

#================================================








