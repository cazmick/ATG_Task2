import time

from Main.Base import Base
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(filename='../Resources/logURL.txt', level=logging.INFO,
                    format='%(levelname)s:%(name)s:%(message)s')

import os


class ArticleLocators(Base):
    def sendTitle(self):
        element = Base.waitForElement(self, "//textarea[@id='title']", "xpath", 10)
        element = Base.getElement(self, "//textarea[@id='title']", "xpath")
        Base.action_sendkey(element, "Automation Practice")

    def sendDescription(self):
        # element = Base.waitForElement(self, "description", "classname", 10)
        # element = Base.getElement(self, "description", "classname")
        # Base.action_click(element)
        element = Base.waitForElement(self,
                                      "//*/form[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]",
                                      "xpath", 10)
        element = Base.getElement(self,
                                  "//*/form[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]",
                                  "xpath")
        element.clear()
        Base.action_sendkey(element, "It is a Part of Automation Practice")

    def uploadCover(self):
        element = Base.waitForElement(self, "//input[@id='cover_image']", "xpath", 10)
        element = Base.getElement(self, "//input[@id='cover_image']", "xpath")
        os.chdir("../Resources")
        new_path = os.getcwd()
        Base.action_sendkey(element, new_path + "\\darkPencil.jpg")

    def submitPost(self):
        element = Base.waitForElement(self, "//button[@id='hpost_btn']", "xpath")
        element = Base.getElement(self, "//button[@id='hpost_btn']", "xpath")
        Base.action_click(element)
        print(self.get_log("browser"))
        logger.info("Current URL")
