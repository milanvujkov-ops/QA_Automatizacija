from selenium import webdriver
from selenium.webdriver.common.by import By
# 1. Uvozimo alate za pametno čekanje
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/login")

    # 2. Pravimo pametno čekanje (maksimalno 10 sekundi)
    wait = WebDriverWait(driver, 10)

    # 3. Čekamo da polje za username postane vidljivo i tek onda ga hvatamo
    username_field = wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username_field.send_keys("tomsmith")

    # Isto to za password
    password_field = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password_field.send_keys("SuperSecretPassword!")

    # Isto to za dugme
    login_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.radius"))
    )
    login_button.click()

    # Čekamo da se pojavi poruka o uspešnom loginu (Provera!)
    success_message = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )
    print("Uspeh! Poruka sa sajta:", success_message.text)

finally:
    driver.quit()