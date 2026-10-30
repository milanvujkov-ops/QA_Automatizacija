from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_popunjavanje_forme_pom(driver):
    forma_stranica = KontaktFormaPage(driver) if 'KontaktFormaPage' in globals() else None
    
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    driver.find_element(By.NAME, "my-text").send_keys("Petar")
    
    element = driver.find_element(By.NAME, "my-select")
    select = Select(element)
    select.select_by_visible_text("Two")
    
    driver.find_element(By.CSS_SELECTOR, "button").click()
    
    wait = WebDriverWait(driver, 10)
    poruka = wait.until(EC.presence_of_element_located((By.ID, "message"))).text
    assert poruka == "Received!"