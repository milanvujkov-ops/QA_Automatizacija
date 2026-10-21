import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def test_iframe_novo(driver):
    # 1. Otvaramo stranicu
    driver.get("https://the-internet.herokuapp.com/iframe")

    wait = WebDriverWait(driver, 10)

    # 2. Prvo se prebacim na iframe preko njegovog ID-ja "mce_0_ifr".
    driver.switch_to.frame("mce_0_ifr")

    # 3. Pronalazimo telo editora unutar iframe
    editor = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # 4. Postavljamo text direkno preko JavaScript-a (zaobilazi problem sa rich-text editorom)
    driver.execute_script("arguments[0].innerHTML = 'Automatsko testiranje sa Seleniumom je super!';", editor)

    # 5. Proveravamo dali je tekst uspesno unet.
    assert editor.text == "Automatsko testiranje sa Seleniumom je super!"