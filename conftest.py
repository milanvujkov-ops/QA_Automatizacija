import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless") # Firefox headless režim za GitHub Actions
    
    browser = webdriver.Firefox(options=options)
    browser.maximize_window()
    yield browser
    browser.quit()