from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successful_login():
    driver = webdriver.Chrome()
    try:
        driver.get("https://the-internet.herokuapp.com/login")
        wait = WebDriverWait(driver, 10)

        wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("tomsmith")
        wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("SuperSecretPassword!")
        
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.radius"))).click()

        success_message = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
        
        # Proveravamo da li je poruka o uspehu tu
        assert "You logged into a secure area" in success_message.text
    finally:
        driver.quit()


def test_failed_login():
    driver = webdriver.Chrome()
    try:
        driver.get("https://the-internet.herokuapp.com/login")
        wait = WebDriverWait(driver, 10)

        # Unosimo pogrešne podatke
        wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("pogresan_user")
        wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("PogresnaLozinka")
        
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.radius"))).click()

        error_message = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
        
        # Proveravamo da li piše da je username nevažeći
        assert "Your username is invalid!" in error_message.text
    finally:
        driver.quit()