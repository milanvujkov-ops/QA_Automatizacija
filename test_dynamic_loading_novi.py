import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dynamic_loading_novi(driver):
    # 1. Otvaramo stranicu
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    wait = WebDriverWait(driver, 20)

    # 2. Pronalazimo dugme unutar #start div-a (ispravljeno "butten" u "button")
    start_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button")))
    start_button.click()

    # 3. Čekamo da se u elementu sa id = "finish" pojavi tačan tekst "Hello World!"
    wait.until(EC.text_to_be_present_in_element((By.ID, "finish"), "Hello World!"))

    # 4. Kada se tekst pojavi, hvatamo element i radimo assert
    message_element = driver.find_element(By.ID, "finish")
    assert message_element.text == "Hello World!"

