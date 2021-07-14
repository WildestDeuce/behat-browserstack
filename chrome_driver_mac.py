from selenium import webdriver


driver = webdriver.Chrome(CHROME_PATH)
driver.get('https://seasonaljobs.dol.gov/)

class PageSeasonalJobsSearch():

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.higlight = True

    def search(self, keywords):
        