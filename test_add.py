from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add(driver):
    # 1. Otvaram stranicu
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    wait = WebDriverWait(driver, 10)

    # 2. Prvo moramo da kliknemo "Remove" da bi se dugme uopšte pretvorilo u "Add"
    remove_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Remove']")))
    remove_button.click()

    # 3. Čekamo poruku da je sklonjeno
    gone_message = wait.until(EC.presence_of_element_located((By.ID, "message")))
    assert gone_message.text == "It's gone!"

    # 4. Sada se pojavilo dugme "Add" – nalazimo ga i klikćemo
    add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add']")))
    add_button.click()

    # 5. Čekamo da se checkbox ponovo pojavi
    wait.until(EC.visibility_of_element_located((By.ID, "checkbox")))

    # 6. Proveravamo poruku "It's back!"
    message_element = wait.until(EC.presence_of_element_located((By.ID, "message")))
    assert message_element.text == "It's back!"