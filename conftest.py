import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")

    browser = webdriver.Firefox(options=options)
    # Pravilan način za podešavanje veličine prozora u Firefox-u
    browser.set_window_size(1920, 1080)
    browser.set_page_load_timeout(60)
    
    yield browser
    browser.quit()