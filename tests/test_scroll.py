from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_scroll(driver):
    driver.get("https://the-internet.herokuapp.com/large")
    
    wait = WebDriverWait(driver, 10)
    footer = wait.until(EC.presence_of_element_located((By.ID, "page-footer")))
    
    # Obavezno inicijalizujemo actions pre korišćenja!
    actions = ActionChains(driver)
    actions.move_to_element(footer).perform()
    
    assert "Elemental Selenium" in footer.text