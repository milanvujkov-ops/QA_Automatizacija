from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_inputs(driver):
    # 1. Otvaramo stranicu
    driver.get("https://the-internet.herokuapp.com/inputs")

    wait = WebDriverWait(driver, 10)

    # 2. Pronalazimo input polje preko pametnog čekanja i CSS selektora
    input_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='number']")))

    # 3. Upisujemo broj u polje
    input_field.send_keys("12345")
    
    # 4. Proveravamo preko assert-a da li je uneta vrednost "12345"
    assert input_field.get_attribute("value") == "12345"