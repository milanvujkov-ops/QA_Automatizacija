import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    # Ovi argumenti rešavaju problem sa DOM-om i fokusom na CI serveru
    options.add_argument("--disable-gpu")
    options.set_preference("dom.ipc.processCount", 1)
    
    browser = webdriver.Firefox(options=options)
    browser.set_window_size(1920, 1080)
    browser.set_page_load_timeout(60)
    
    yield browser
    browser.quit()