from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(filename='../Resources/logURL.txt', level=logging.DEBUG,
                    format='%(levelname)s:%(name)s:%(message)s')


class Driver:

    @staticmethod
    def openBrowser():  # Method to execute the Browser
        options = Options()
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(executable_path="../Resources/chromedriver.exe", options=options)
        driver.get("https://atg.party/")
        driver.implicitly_wait(20)
        driver.maximize_window()
        print(driver.get_log("browser"))
        logger.debug("Get URL")

        return driver

    @staticmethod  # method to close the Browser
    def driverClose(driver):
        driver.close()
        driver.quit()

    @staticmethod
    def updateURL(self):
        self.get("https://atg.party/article")
        self.implicitly_wait(20)
        return self
