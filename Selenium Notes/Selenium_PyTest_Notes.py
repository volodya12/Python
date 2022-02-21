# SELENIUM PYTHON FRAMEWORK DESIGN

#1. PyTest Framework

from msilib.schema import File
from multiprocessing.sharedctypes import Value
from re import S

from h11 import Data


* pip install pytest
* PyTest Projects Names always starts with "test_<Name>.py" -> test_demo1.py 
* Two SPACES required between Methods/functions
***** MUST HAVE Indentation present when writing Methods **************

* It is RECOMMENDED to build related Test Cases Per "test_pytest.py" file 

* PyTest code must be written in Functions and start with "test_" OR end with "_test"
        * Give MEANINGFUL NAME to a Method 
        
ex: def test_firstProgram():
        print("Hello World")

* Every Function/PyTest Method is treated as One Test Case  
* An interpreter must be set as PyTest

# Test Case:
        def test_firstProgram():
                print("This is my first Test Case in PyTest")
        assert msg == "This message will not match"        (Test will fail)

#=============================================================
# Use CMD Line to execute ALL PyTests

* cd to PyTestDemo folder project-> key: py.test -v -s
        v-verbose-gives more info after execution
        s-prints console logs such "Hello World"
        m- mark/run testcases with marked with a Tag 

# Execute only Specific File of PyTest
* cd to PyTestDemo folder project
key: py.test <fileName>.py -v -s

# Execute ONLY SPECIFIC Test Case/Methods within a File
* cd to PyTestDemo folder project-> key: py.test -k <TestCaseName or partial Name> -v -s
* cd to PyTestDemo folder project-> key: py.test -m <tagName> -v -s

def test_firstCreditCard()
def test_secondCreditCard()

EX: TestCase Name = py.test -k first_CreditCard -v -s
EX: Partial Name = py.test -k CreditCard -v -s

        - if there are several methods/test cases in a pytest file, and only specific once needs to run.
        - runs ONLY methods mentioned as keyword within ALL PyTest files. 
        k- keyword

=================== Mark/Tags =================================
# Execute ONLY Test Case/Methods that have TAG/MARK
#       Mark -> Marking Test Case/Methods with specific Tag for execution purposes
# There are Pre-defined marks in Pytest -> google it:
#       https://docs.pytest.org/en/6.2.x/example/markers.html

import pytest

@pytest.mark.<Any_tag_name>
def test_secondProgram():
        print("hello people")

* cd to PyTestDemo folder project-> key: py.test -m <tagName> -v -s

@pytest.mark.skip               # 'skip', 'xfail', pre-defined marks - Also Known as "Annotation"
@pytest.mark.smoke
# Several marks can be applied to a TestCase
# will actually skip that TEST/Method Even tho, all Tests are meant to run
# cd to PyTestDemo folder project-> key: py.test -v -s

@pytest.mark.xfail
# Operation that allows to Run Method even tho it would give an Error message (Bug) 
#       but it still needs to run as Pre-requisites. Error will NOT be Reported.

# May recieve Warning while running pytest = "PytestUnknownMarkWarning"
# https://stackoverflow.com/questions/60806473/pytestunknownmarkwarning-unknown-pytest-mark-xxx-is-this-a-typo
# https://docs.pytest.org/en/latest/how-to/mark.html#raising-errors-on-unknown-marks

======================== Fixtures -> pre-requisites =========================================
# Fixtures -> goes into Function as a Parameter. 
# Fixture is mainly part of a Setup process. It runs first as a Setup process. 
# Ex: Launch the browser with specific website, OR clear Cache, Cookies, History before Tests run

# When executed, it senses the fixture first before executing Method/TestCase and navigates to THAT fixture.
# Must have "fixture" tag 
Fixtures is usually added to TestCases / Methods 

Conftest.py = file inside folder = Contain fixtures that runs for ALL TestCases/Files within same folder.
    Declare all your "Fixtures" in Conftest.py and call them into Actual TestCases = separate file 
    Each TestCase is Separate File.py
TIP: Fixture in Conftest used only when used in Multiple TestCases 
TIP: Fixture: This method used when applied to Multiple TestCases 

@pytest.fixture()
def setup():
        print("I will be executed First")
        yield
        driver.close()          # 'yield' normally used for closing browser, deleting cookies...
        print("I will be executed LAST")

def test_fixtureDemo(setup):
        print("I will execute steps in 'setup' method first because its a fixture")

Yield -> Post-Execution = First, 'Setup' method will be executed because of FIXTURE, then, 'test_fixtureDemo', 
then anything after "yield"
       Usually used for closing browser, delete oookies, or something to end test case with.

======================= Conftest.py file =========================================
# Conftest file -> this file would include test cases that are repeatedly used in other files
# Put TestCases with Fixtures into Conftest files ONLY if you think particular Fixture is SHARED by 
# multiple files/Test Cases/Class
Must have "import pytest"

        * Whenever function with a fixture is being executed, it will look for that specific fixture name in 
        other files, if none found, it will look into "conftest.py" file. 

TIP:  Fixtures in conftest file Identifies files named starts with "test_"
--------------------------

IN Conftest.py
@pytest.fixture()
def setup():            # 'setup' method is created to be executed
        print("This will be executed first")

IN test_demo.py
def test_fixtureDemo(setup)     # 'setup' method is called to run in Conftest.py file FIRST
        print("I will execute steps in fixtureDemo method")
# When executed, python will check TestCase/Method in 'test_demo.py' file first, sees 'setup' fixture, checks
# within a file if any 'setup' fixture present, if aint, goes to diff files where 'setup' method is present, 
# executes it. 

========================= Class/Scope ======================================================
# Class -> put all test cases into a Class. Segregate methods into Groups
Lesson 80
# Optimization: Having several methods as TestCases, passing fixture('setup') for every test case, 
#       use Class to wrap all TestCases and add Global "usefixtures('setup')"

TIP: When Creating "class TestExample", Method ALWAYS have argument of "self"

import pytest

@pytest.mark.usefixtures("setup")           #- assuming there is method with fixture 'setup'
class TestExample:
        def test_fixtureDemo(self):
        print("hello world")

        def test_fixtureDemo2(self):
        print("hello world")

        def test_fixtureDemo3(self):
        print("hello world")

# this allows to execute fixture "setup" first, before any of these methods
        # Setup then fixtureDemo, Setup then fixtureDemo1, Setup then fixtureDemo2
# "Scope" goes as argument in Fixture / "Scope" takes class name only

* google: scope, class, hooks in pytest 

======================== Data Driven - Fixtures ============================================
Lesson 81
Fixtures help Load Data
Load Data using Fixture and then pass Data into TestCase or pass Fixture with Data into TestCase 

IN Conftest

@pytest.fixture()       # must specifiy this is fixture or pytest won't execute it
def dataLoad():
        print("user profile data is being created")
        return ["Kyle", "Mike", "Kyle@yahoo.com"]       # Tuple

IN Diff File

@pytest.mark.usefixtures("dataLoad")    # implementing 'dataLoad' Method into 'usefixture' to Read Data From
class TestEample:
        def editProfile(self, dataLoad):
                print(dataLoad)         # prints ALL Data Set within Tuple
                print(dataLoad[0])      # Prints specific set
                print(dataLoad[1])

# 'dataLoad' as argument, if want to return Data to Specific Test
#       use that 'dataLoad' inside TestCase/Method.
# May not need to add 'dataLoad' as argument if 'usefixtures("dataLoad")' is declared Globaly
# In our case, If we NEED to RETURN Data Set Tuple, we need second argument as "dataLoad" 

======================== Parametizing data - Data Set - Data Driven ====================
# Parametizing data with multiple data sets using Fixtures
#Lesson 82

TIP: 'self' not required sometimes if Test Method are not Wrapped in Class
        'self' applies when Test Cases/Methods are Wrapped in Class 

IN Conftest

# Once passed into TC, TC will run data set of: Chrome, firefox, and IE
# Will Run 3 Times because of 3 values in Fixture

@pytest.fixture(params=["chrome", "firefox", "IE"])
def crossBrowser(request):              # 'request' Instance, allows to SEND data to TestCase
        return request.param

# Once TC executed, it will read from Fixture 'params' then go into 'request' instance, and Returns
#        Parameters Data Set
# "Request" only used when Fixture has Values in it

IN DEMO file

# This test will run 3 times because of Fixture in Conftest file
def test_crossBrowser(crossBrowser):    # Connection TC Method to Fixture in Conftest
        print(crossBrowser)     
        print(crossBrowser)[0]          # 1st run: Prints "Browser", 2nd run: "firefox" and so on  
-----------------
@pytest.fixture(params=[("Browser","chrome"), "firefox", "IE"])
("browser", "chrome") is First Value
"firefox" is Second Value
"IE" is Third Value

========================= Reports in HTML ===============================================
pip install pytest-html

py.test --html=report.html -v  #-> will create report as .html file in pytest file folder

* Navigate to pytest folder, look for report.html, right-click-> copy path-> paste into browser

========================= Logs/Logging ==============================================
Log Levels:
        Debug
        Info
        Warning
        error
        critical
--------------------------
import logging

# Indentation must be present when writing Methods

def test_loggingDemo():
# by including __name__, it will log file name this line mentioned in
#       by default, it will print as 'root'
#        This line responsible for printing Logs
        logger = logging.getLogger(__name__)

# 'fileHandler=' is an object
        fileHandler = logging.FileHandler('logfile.log')
# Format your log message line ('formatter='     it is an Object)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")

        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)      # prints starting from INFO level

        logger.debug("A debug statement is executed")
        logger.info("Information Statement")
        logger.warning("Something is in WARNING mode")
        logger.error("This is an error")
        logger.critical("Critical issue")

# When ^ script is executed. It will create 'logfile.log' file with formatted Logging message
#        and print logs there Instead of the Console.
#        AND will print log messages starting from INFO, Warning, Error, Critical 
#                No "debug" message
Prints: date time :INFO : <Project_Folder>.<file_Name> :Information Statement
                  :ERROR : pytestsDemo.test_logging :This is an error
==================
Include all these logging into HTML report
Section 19, lesson 87
====================================================================================










