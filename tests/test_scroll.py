from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_scroll(driver):
    # 1. Otvaramo stranicu
    driver.get("https://the-internet.herokuapp.com/large")

    wait = WebDriverWait(driver, 10)

    # 2. Pronalazimo footer na dnu stranice preko ID-ja
    footer = wait.until(EC.presence_of_element_located((By.ID, "page-footer")))
    driver.execute_script("arguments[0].scrollIntoView(true);", footer)
    actions.move_to_element(footer).perform()
    
    # 3. Prelazimo mišem / skrolujemo do footera koristeći ActionChains
    actions = ActionChains(driver)
    actions.move_to_element(footer).perform()
    
    # 4. Proveravamo da li tekst footera sadrži "Elemental Selenium"
    assert "Elemental Selenium" in footer.text