import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Main.Driver import Driver


class Base(Driver):

    @staticmethod
    def getByType(locatorType):  # Method to find Locator Type
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            print("LocatorType " + locatorType + " not supported")
            return False

    @staticmethod
    def getElement(driver, locator, locatorType):  # Method to get the element
        element = None
        try:
            byType = Base.getByType(locatorType)
            print(byType)
            element = driver.find_element(byType, locator)
            print(element)
            print("Element Found")
        except:
            print("Element not appeared on the webpage")
        return element

    @staticmethod
    def getElements(driver, locator, locatorType):  # Method to handle muliple elements
        element = None
        try:
            byType = Base.getByType(locatorType)
            print(byType)
            element = driver.find_elements(byType, locator)
            print("Elements Found")
        except:
            print("Elements not appeared on the webpage")
        return element

    @staticmethod
    def action_click(ele):  # Method to perform click action
        ele.click()
        print("CLICKING")

    @staticmethod
    def action_sendkey(ele, msg):  # Method to perform send Text
        # ele.clear()
        ele.send_keys(msg)
        print("SENDING KEYS")

    @staticmethod
    def get_title(driver):
        print(driver.title)

    @staticmethod
    def action_dropDown(ele, visible_text):  # Method to haandle the drop down Scenario
        sel = Select(ele)
        sel.select_by_visible_text(visible_text)

    @staticmethod
    def takeScreenshot(driver):
        fileName = time.strftime("%Y%m%d-%H%M%S") + ".png"
        screenshotDir = "../Screenshots/" + fileName
        try:
            driver.save_screenshot(screenshotDir)
            print("Screenshot saved successfully")
        except:
            print("Screenshot not saved!")

    @staticmethod
    def action_alert(driver):  # Method to handle the alert pop up
        alert1 = driver.switch_to.alert
        alert1.accept()

    @staticmethod
    def waitForElement(driver, locatorValue, locatorType="id", timeout=10):
        element = None
        try:
            byType = Base.getByType(locatorType)
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(driver, timeout)
            element = wait.until(EC.element_to_be_clickable((byType, locatorValue)))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
        return element
