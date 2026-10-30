import os
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@pytest.mark.skip(reason="HTML5 drag and drop ne radi u headless modu na CI serveru")
def test_drag_and_drop(driver):
    # 1. Otvaramo stranicu
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")

    wait = WebDriverWait(driver, 20)

    # 2. Pronalazimo elemente preko ID-ja (column-a i column-b)
    element_a = wait.until(EC.presence_of_element_located((By.ID, "column-a")))
    element_b = wait.until(EC.presence_of_element_located((By.ID, "column-b")))

    # 3. Inicijalizujemo ActionChains i prevlačimo element A na mesto elementa B
    actions = ActionChains(driver)
    actions.drag_and_drop(element_a, element_b).perform()

    # 4. Proveravamo pomoću assert-a da li u koloni A sada piše "B"
    header_a = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#column-a header")))
    assert header_a.text == "B"

