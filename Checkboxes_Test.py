from selenium import webdriver
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
import pytest

class Checkboxes(pytest):      
    
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=CHROME_PATH)
        cls.driver = implicity_wait(10)
        cls.driver.maximize_window()

    def button_click_to_correct_url(self):
        self.driver.get(CHECKBOXES_URL)
        self.driver.find_element_by_xpath("link=Checkboxes").send_keys()
        self.driver.find_element_by_xpath().click("xpath=//input[@type='checkbox']")