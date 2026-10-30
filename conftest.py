import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    
    browser = webdriver.Firefox(options=options)
    # Ne koristimo maximize_window u headless modu, već oslanjamo se na width/height iznad
    yield browser
    browser.quit()