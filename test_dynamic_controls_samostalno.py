from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dynamic_controls(driver):
    # 1. Otvaram stranicu
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    wait = WebDriverWait(driver, 10)

    # 2. Pronalazimo i klikćemo na dugme "Remove" preko XPath-a
    remove_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Remove']")))
    remove_button.click()

    # 3. Čekamo da checkbox postane nevidljiv
    wait.until(EC.invisibility_of_element_located((By.ID, "checkbox")))

    # 4. Proveravamo preko assert-a da se pojavila poruka "It's gone!"
    message_element = wait.until(EC.presence_of_element_located((By.ID, "message")))
    assert message_element.text == "It's gone!"