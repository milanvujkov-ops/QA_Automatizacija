import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dynamic(driver):
    # 1. Otvaramo strnicu 
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    wait = WebDriverWait(driver, 20)

    # 2. Pronalazimo dugme koje je unutar #start div-a i klikćemo ga
    start_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button")))
    start_button.click()
    
    # Čekamo da se element sa porukom pojavi i postane vidljiv
    hello_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4")))
    
    # 4. Kada se tekst pojavio, hvatamo element i radimo assert
    message_element = driver.find_element(By.ID, "finish")
    assert message_element.text == "Hello World!"