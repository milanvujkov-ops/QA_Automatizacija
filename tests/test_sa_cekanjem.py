from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_uspeh_sa_cekanjem(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    # 2. Pravimo pametno čekanje (maksimalno 10 sekundi)
    wait = WebDriverWait(driver, 10)

    # 3. Čekamo da polje za username postane vidljivo
    username_field = wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username_field.send_keys("tomsmith")

    password_field = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password_field.send_keys("SuperSecretPassword!")

    login_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.radius"))
    )
    login_button.click()

    # Čekamo da se pojavi poruka o uspešnom loginu
    success_message = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )
    assert success_message.is_displayed()