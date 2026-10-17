import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_upload(driver):
    # 1. Otvaramo stranicu
    driver.get("https://the-internet.herokuapp.com/upload")

    wait = WebDriverWait(driver, 10)

    # 2. Pravimo putanju do bilo kog fajla koji imamo pri ruci, npr. trenutnog foldera
    fajl_putanja = os.path.abspath("test_dynamic.py")

    # 3. Pronalazimo input za upload i šaljemo mu putanju
    # Šaljemo putanju fajla direktno u input element
    upload_input = driver.find_element(By.ID, "file-upload")
    upload_input.send_keys(fajl_putanja)

    # 4. Klikćemo na dugme za upload/submit
    submit_button = driver.find_element(By.ID, "file-submit")
    submit_button.click()

    # 5. Čekamo da se pojavi naslov i proveravamo tekst
    success_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[text()='File Uploaded!']")))
    assert success_message.text == "File Uploaded!"