from selenium import webdriver
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory

driver = webdriver.Chrome(CHROME_PATH)


class AboutTest:
    def __init__(self, driver):
        self.driver = driver


def AboutLinkCheck():
    about = 