import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    
    # Ove opcije govore Chrome-u da se pokreće u pozadini bez otvaranja prozora (obavezno za GitHub Actions / Linux)
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    browser.quit()