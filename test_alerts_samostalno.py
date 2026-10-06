from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_alerts_samostalno(driver):
    # 1. Otvaramo zadatu stranicu
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    wait = WebDriverWait(driver, 10)

    # 2. Pronalazimo i klikćemo na prvo dugme (preko XPath-a po tekstu dugmeta)
    add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Alert']")))
    add_button.click()

    # 3. Prelazimo na alert i prihvatamo ga (klik na OK)
    alert = driver.switch_to.alert
    alert.accept()

    # 4. Proveravamo da se ispod pojavio tačan tekst poruke
    result_element = wait.until(EC.presence_of_element_located((By.ID, "result")))
    assert result_element.text == "You successfully clicked an alert"