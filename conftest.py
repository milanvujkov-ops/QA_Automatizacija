import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Pokrećemo pretraživač pre testa
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    # Gasimo pretraživač nakon što se test završi
    browser.quit()