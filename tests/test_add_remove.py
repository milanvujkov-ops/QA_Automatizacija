from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_remove(driver):
    # 1. Otvorimo stranicu
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

    wait = WebDriverWait(driver, 10)

    # 2. Pronalazimo i klikćemo na dugme preko tag-a "button" (pošto je jedinstveno)
    add_button = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
    add_button.click()

    # 3. Čekamo da se pojavi dugme "Delete" preko klase ".added-manually"
    delete_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".added-manually")))

    # 4. Proveravamo preko assert-a da li se na dugmetu nalazi tekst "Delete"
    assert delete_button.text == "Delete"
    