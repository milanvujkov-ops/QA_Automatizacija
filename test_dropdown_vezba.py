from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select  # <--- Ova klasa nam služi za dropdown!

def test_dropdown(driver):
    # 1. Otvaramo stranicu
    driver.get("https://the-internet.herokuapp.com/dropdown")

    wait = WebDriverWait(driver, 10)

    # 2 i 3 Pronalazimo element dropdown menija po id-ju
    dropdown = Select(driver.find_element(By.ID, "dropdown"))

    # 4. Biramo opciju po njenom vidljivom tekstu
    dropdown.select_by_visible_text("Option 1")

    # 5. Biramo opciju preko vidljivog teksta (npr. "Option 1")
    selected_option = dropdown.first_selected_option

    # 6. ZADATAK ZA TEBE: Dodaj assert da proveris da je izabrana opcija zaista "Option 1"
    assert selected_option.text == "Option 1"