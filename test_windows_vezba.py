import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_windows(driver):
    # 1. Otvoriti stranicu
    driver.get("https://the-internet.herokuapp.com/windows")

    wait = WebDriverWait(driver, 10)

    # Pamti se ID glavnog prozora (dobra praksa)
    glavni_prozor = driver.current_window_handle

    # 2. Pronalazimo link "Click Here" preko teksta i klikćemo na njega
    link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Click Here")))
    link.click()
    
    # Uzimamo sve otvorene prozore/tabove
    svi_prozori = driver.window_handles

    # Prebacujemo se na onaj prozor koji nije glavni
    for prozor in svi_prozori:
        if prozor != glavni_prozor:
            driver.switch_to.window(prozor)
            break
    
    # 4. Na novom prozoru čekamo i proveravamo da li je tekst naslova (h3) "New Window"
    heading = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h3")))
    assert heading.text == "New Window"
    
    # 5. Zatvaramo novi prozor
    driver.close()

    # 6. VRAĆAMO SE NA GLAVNI PROZOR (Dobra praksa!)
    driver.switch_to.window(glavni_prozor)

    # Provera da smo se uspešno vratili na staru stranicu
    assert "Opening a new window" in driver.page_source