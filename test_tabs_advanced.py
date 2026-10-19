import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_tabs_advanceed(driver):
    # 1. Otravamo stranicu
    driver.get("https://the-internet.herokuapp.com/windows")

    wait = WebDriverWait(driver, 10)

    # 2. Sačuvaj handle glavnog prozora
    glavni_prozor = driver.current_window_handle

    # 3. Pronalazimo link "Click Here" (pazi na velika/mala slova) i klikćemo ga
    link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Click Here")))
    link.click()

    # 4. Uzimamo sve otvorene prozore
    svi_prozori = driver.window_handles
    
    # 5. Prebacujemo se na novi prozor (onaj čiji ID nije glavni_prozor)
    for prozor in svi_prozori:
        if prozor != glavni_prozor:
            driver.switch_to.window(prozor)
            break
    
    # 6. Na novom prozoru čekamo da se pojavi h3 čiji je tekst tačno "New Window" (bez 's' na kraju)
    heading = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3")))
    assert heading.text == "New Window"

    # 7. Zatvaramo novi prozor
    driver.close()

     # 8. Vraćamo se nazad na glavni prozor
    driver.switch_to.window(glavni_prozor)
    
    # 9. Provera da li smo se uspešno vratili na staru stranicu
    assert "Opening a new window" in driver.page_source