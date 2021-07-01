from selenium.webdriver.common.by import By
from selenium import webdriver, 
from seleniumpagefactory.Pagefactory import PageFactory

class SearchSeasonalJobs(PageFactory):
    def __init__(self, driver):
        self.driver = driver


    def userSearch(self):
        _user_Input = webdriver.findElement(By.ID('occupation')).get_attribute('value')
        self.userInput.get_text(_user_Input)
