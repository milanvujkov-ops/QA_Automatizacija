from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/login")

    wait = WebDriverWait(driver, 10)

    # 1. Namerno unosimo pogrešno korisničko ime i lozinku
    username_field = wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username_field.send_keys("nepoznati_korisnik")

    password_field = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password_field.send_keys("PogresnaLozinka123")

    # 2. Klikćemo na login
    login_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.radius"))
    )
    login_button.click()

    # 3. Čekamo poruku o grešci koja se pojavljuje na vrhu stranice
    error_message = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )
    print("Test uspešan! Poruka o grešci sa sajta je:", error_message.text)

finally:
    driver.quit()