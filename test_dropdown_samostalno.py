from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dropdown_samostalno(driver):
    # 1. Otvaram stranicu
    driver.get("https://the-internet.herokuapp.com/dropdown")

    # 2. i 3. Pronalazimo element i odmah pravimo Select objekat
    dropdown = Select(driver.find_element(By.ID, "dropdown"))

    # 4. Biramo opciju po njenom vidljivom tekstu
    dropdown.select_by_visible_text("Option 1")

    # 5. Uzimamo trenutno izabranu opciju preko first_selected_option
    selected_option = dropdown.first_selected_option

    # Assert proverava da li je tekst te izabrane opcije "Option 1"
    assert selected_option.text == "Option 1"