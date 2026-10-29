import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    
    # Čist Selenium drajver bez webdriver-managera koji pravi problem na Linuxu
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    browser.quit()