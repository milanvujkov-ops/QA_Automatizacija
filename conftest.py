import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")

    browser = webdriver.Firefox(options=options)
    browser.set_window_size(1920, 1080)
    browser.set_page_load_timeout(30)
    
    yield browser
    browser.quit()