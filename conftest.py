import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    # Ovi argumenti sprečavaju pucanje i timeout-ove Firefox-a na CI serveru
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")

    browser = webdriver.Firefox(options=options)
    # Uklanjamo set_window_size jer koristimo argumente iznad i postavljamo page load timeout na 60 sekundi
    browser.set_page_load_timeout(60)
    
    yield browser
    browser.quit()