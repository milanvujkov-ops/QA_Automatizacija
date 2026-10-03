from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.parametrize("username, password, expected_text", [
    ("tomsmith", "SuperSecretPassword!", "You logged into a secure area"),
    ("pogresan_user", "PogresnaLozinka", "Your username is invalid!")
])
def test_login(driver, username, password, expected_text):
    driver.get("https://the-internet.herokuapp.com/login")
    wait = WebDriverWait(driver, 10)

    # Unosimo podatke (koji stižu iz parametara iznad)
    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(username)
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)
    
    # Klik na login
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.radius"))).click()

    # Provera poruke
    message = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
    
    # Assert proverava da li očekivani tekst postoji u poruci sa sajta
    assert expected_text in message.text