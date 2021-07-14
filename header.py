from selenium import webdriver
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory

class Header(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    #Externalize the url rather than hard coding
    def links(_url):
        _url = "https://seasonaljobs.dol.gov/jobs"


        