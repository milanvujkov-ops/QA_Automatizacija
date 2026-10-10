from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_windows(driver):
    # 1. Otvaram stranicu
    driver.get("https://the-internet.herokuapp.com/windows")

    wait = WebDriverWait(driver, 10)

    # 2. Pronalazimo link "Click Here" preko teksta i klikćemo na njega
    link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Click Here")))
    link.click()

    # 3. Uzimamo listu svih otvorenih tabova i prebacujemo se na novi (drugi)
    driver.switch_to.window(driver.window_handles[1])

    # 4. Na novom prozoru čekamo i proveravamo da li je tekst naslova (h3) "New Window"
    heading = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h3")))
    assert heading.text == "New Window"