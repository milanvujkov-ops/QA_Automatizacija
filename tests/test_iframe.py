from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def test_iframe(driver):
    # 1. Otvaramo stranicu
    driver.get("https://the-internet.herokuapp.com/iframe")

    wait = WebDriverWait(driver, 10)

    # 2. PRVO se prebacujemo u iFrame preko njegovog ID-ja ("mce_0_ifr")
    driver.switch_to.frame("mce_0_ifr")

    # 3. Pronalazimo telo editora unutar iFrame-a
    editor = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # 4. Postavljamo tekst direktno preko JavaScript-a (zaobilazi problem sa rich-text editorom)
    driver.execute_script("arguments[0].innerHTML = 'Automatsko testiranje sa Seleniumom je super!';", editor)

    # 5. Proveravamo da li je tekst uspešno unet
    assert editor.text == "Automatsko testiranje sa Seleniumom je super!"