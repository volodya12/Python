# This Code will be in JAVA
# https://www.youtube.com/watch?v=UlOREVRHpYs > Action Class in WebDriver (Java)

# Actions Class: (must be imported)
#   Mouseover =  MoveToElement()
#   Mouse Right-Click = contextClick()
#   Drag and Drop = ClickAndHold(), MoveToElement(), Release() or dragAndDrop(source, target)
#   Slider = moveToElement(), dragAndDrop(source, xOffset, yOffset)
#   Resizable
#   doubleClick()   

from ast import Or
from cmath import atan
from operator import methodcaller
from pydoc import visiblename
from tkinter import Scrollbar
import org.openqa.selenium.By
import org.openqa.selenium.WebDriver
import org.openqa.selenium.chrome.ChromeDriver
import org.openqa.selenium.interactions.Actions

public class MouseOver{

    public static void main(String[] args){

        System.setProperty("webdriver.chrome.driver", "location of chromedriver")
        WebDriver driver=new ChromeDriver();

        driver.get("http://opensource-demo.orangehrmlive.com")

        # Login (http://opensource-demo.orangehrmlive.com)
        driver.findElement(By.id("txtUsername")).sendKeys("Admin")
        driver.findElement(By.id("txtPassword")).sendKeys("Admin123")
        driver.findElement(by.id("btnClick")).click()

        #========================================= Mouse Over
        # Action 'act' is a variable 
        # driver = is 'WebDriver driver'
        Actions act=new Actions(driver);

        # driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);

        # Admin->User management-> users
        WebElement admin = driver.findElement(By.xpath("//*[@id='menu_admin_viewAdminModule']/b"));
        WebElement usermng = driver.findElement(By.xpath("//*[@id='menu_admin_UserManagement']");
        WebElement sysUser = driver.findElement(By.xpath("//*[@id='menu_admin_viewSystemUsers']"));

        # MouseOver action
        act.moveToElement(admin).build().perform(); #move
        act.moveToElement(usermng).build().perform();   #move   
        act.moveToElement(sysUser).click().build().perform();   #click
        
        # Combine 3 Actions to one LIne
        act.moveToElement(admin).moveToElement(usermng).moveToElement(sysUser).click().build().perform();
        
        #========================================= Mouse Right-Click
        # Mouse Right-Click (https://swisnl.github.io/jQuery-contextMenu/demo.html)
        Actions act=new Actions(driver);

        WebElement buttonClick = driver.findElement(By.xpath("//*[@class='context-menu-one']"))

        act.contextClick(button).build().perform()  #Mouse Right-Click
        
        # Select "Copy"
        WebElement copy = driver.findElement(By.xpath("/html/body/ul/li[3]"));

        # Switch to Alert Box once Copy is Selected
        System.out.println(driver.switchTo().alert().getText()); # Prints content inside Alert box

        # Close Alert Box
        driver.switchTo().alert().accept();

        #========================================= Drag and Drop
        driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

        WebElement source1 = driver.findElement(By.id("Box7"))
        WebElement target1 = driver.findElement(By.id("Box103"))

        Actions act=new Actions(driver);
        
        # 3 actions Requires: Click, Move/Drag, Release mouse
        act.clickAndHold(source1).moveToElement(target1).release().build().perform();
        or
        act.dragAndDrop(source, target).build().perform()

        #=============================================== Slider
        driver.get("https://jqueryui.com/slider/")
        # Contains iframe tag. Need to use switchTo()
        # I believe 'frame(0)' is index 
        driver.switchTo().frame(0);

        # This is Slider, not a Slide bar
        WebElement slider = driver.findElement(By.xpath("//*[@id='slider']/span"))

        Actions act=new Actions(driver);

        # Move Mouse to Slider and Drag to specific Location (horizontally)
        # act.moveToElement(slider).dragAndDrop(slider, xOffset, yOffset)
        act.moveToElement(slider).dragAndDrop(slider, 300, 0).build().perform();

        #=================================================== Scroll
        # https://stackoverflow.com/questions/12293158/page-scroll-up-or-down-in-selenium-webdriver-selenium-2-using-java
        # JavaScript

        # Scroll Down
        WebDriver driver = new ChromeDriver();
        JavascriptExecutor js = (JavascriptExecutor)driver;
        js.executeScript("window.scrollBy(0,250)");
        Or
        jse.executeScript("scroll(0, 250);");
        
        # Scroll UP
        js.executeScript("window.scrollBy(0,-250)");
        OR,
        js.executeScript("scroll(0, -250);");

        #================================================= Scroll until visible
        # https://stackoverflow.com/questions/3401343/scroll-element-into-view-with-selenium
        # Scroll page until Specific Element is visible on page

        scrollIntoView(True) - method

        #================================================== Resize/Resizable
        # Use moveToElement(), dragAndDropBy()
        driver.get("https://jqueryui.com/resizable/")

        driver.switchTo().frame(0);

        # Points to arrow that resizes the box
        WebElement resize = driver.findElement(By.xpath("//*[@id='resizable']/div[3]"));
        
        Actions act=new Actions(driver);
        #act.moveToElement(resize).dragAndDropBY(resize, xOffset, yOffset)
        act.moveToElement(resize).dragAndDropBy(resize, 50, 50).build().perform()
        
        # Sleeps for 3 seconds
        Thread.sleep(3000);

        #============================================== DoubleClick
        Actions act=new Actions(driver);
        
        # Press Ctl+space to expand options in Eclipse IDE
        #   many actions will show to select from
        act.doubleClick() -> will click where pointer is at
        or -> moves mouse and clicks
        act.moveToElement(variable of element).doubleClick()

        # Will Click on Specific Element of Choice
        act.doubleClick(WebElement onElement()).build().perform()
        act.doubleClick(variable of element here)
        #======================================================= Screenshot
        # Take Screenshot 
        TakesScreenshot scrShot =((TakesScreenshot)webdriver);
        File SrcFile=scrShot.getScreenshotAs(OutputType.FILE);

        #=======================================================

        
    }


}



















