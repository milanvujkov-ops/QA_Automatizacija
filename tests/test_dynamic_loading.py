from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dynamic_loading(driver):
    # 1. Otvaramo stranicu
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    wait = WebDriverWait(driver, 15)

    # 2. Pronalazimo dugme koje je unutar #start div-a i klikćemo ga
    start_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button")))
    start_button.click()

    # 3. Čekamo da se u elementu sa id="finish" pojavi tačan tekst "Hello World!"
    wait.until(EC.text_to_be_present_in_element((By.ID, "finish"), "Hello World!"))

    # 4. Kada se tekst pojavio, hvatamo element i radimo assert
    message_element = driver.find_element(By.ID, "finish")
    assert message_element.text == "Hello World!"