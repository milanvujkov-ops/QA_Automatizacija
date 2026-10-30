from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_popunjavanje_forme(driver):
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    
    # Unosimo tekst u polje za ime
    driver.find_element(By.NAME, "my-text").send_keys("Petar")
    
    # Biramo opciju iz padajuće liste
    element = driver.find_element(By.NAME, "my-select")
    select = Select(element)
    select.select_by_visible_text("Two")
    
    # Klikćemo na dugme submit
    driver.find_element(By.CSS_SELECTOR, "button").click()
    
    # Čekamo poruku uspeha i verifikujemo je
    wait = WebDriverWait(driver, 10)
    poruka = wait.until(EC.presence_of_element_located((By.ID, "message"))).text
    assert poruka == "Received!"