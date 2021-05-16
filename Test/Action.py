import time

from Main.Base import Base
from Main.Driver import Driver
from Main.LocatorsArticle import ArticleLocators
from Main.LocatorsLogin import LoginLocators

a = Base.openBrowser()
LoginLocators.loginButton(a)
LoginLocators.sendEmail(a)
LoginLocators.sendPassword(a)
LoginLocators.SignInButton(a)
time.sleep(10)
Driver.updateURL(a)
ArticleLocators.sendTitle(a)
ArticleLocators.sendDescription(a)
ArticleLocators.uploadCover(a)
ArticleLocators.submitPost(a)
time.sleep(5)
Driver.driverClose(a)
