#!/usr/bin/env python
import ipdb; ipdb.set_trace(context=11)
import selenium
import pytest
print("ready to rock and roll")
print(dir(selenium))


@pytest.fixture
def browser():
    #Initialize the ChromeDriver instance
    b = selenium.webdriver.Chrome()

    #Make its calls wait up to 10 seconds for elements to appear
    b.implicitly_wait(10)

    #Return the webdriverinstance for the setup
    yield b

    #Quit the WebDriver instance for the cleanup
    b.quit()

