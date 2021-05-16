import time

from Main.Base import Base
from Main.Driver import Driver
from Main.LocatorsArticle import ArticleLocators


class LoginLocators(Base):
    def loginButton(self):
        element = Base.waitForElement(self, "//a[contains(text(),'Login')]", "xpath", 10)
        element = Base.getElement(self, "//a[contains(text(),'Login')]", "xpath")
        Base.action_click(element)

    def sendEmail(self):
        element = Base.waitForElement(self, "//*/div[2]/div[1]/form[1]/div[1]/div[1]/input[1]", "xpath", 10)
        element = Base.getElement(self, "//*/div[2]/div[1]/form[1]/div[1]/div[1]/input[1]", "xpath")
        Base.action_sendkey(element, "wiz_saurabh@rediffmail.com")

    def sendPassword(self):
        element = Base.waitForElement(self, "//*/div[2]/div[1]/form[1]/div[1]/div[2]/input[1]", "xpath", 10)
        element = Base.getElement(self, "//*/div[2]/div[1]/form[1]/div[1]/div[2]/input[1]", "xpath")
        Base.action_sendkey(element, "Pass@123")

    def SignInButton(self):
        element = Base.waitForElement(self, "//button[@class='form-button landing-signin-btn arrow-animate']", "xpath", 10)
        element = Base.getElement(self, "//button[@class='form-button landing-signin-btn arrow-animate']", "xpath")
        Base.action_click(element)



