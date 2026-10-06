from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_checkboxes_vezba(driver):
    # 1. Otvaramo stranicu sa checkbox-ovima
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    # 2. Pronalazimo sve checkbox-ove preko CSS selektora (koristimo find_elements u množini)
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

    # 3. Prvi checkbox (indeks 0) po difoltu nije čekiran, klikćemo na njega
    checkboxes[0].click()

    # 4. Proveravamo preko assert-a da li je checkbox čekiran (is_selected() vraća True)
    assert checkboxes[0].is_selected()
