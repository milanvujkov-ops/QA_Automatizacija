from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dropdown(driver):
    # 1. Otvaramo sranicu
    driver.get("https://the-internet.herokuapp.com/dropdown")

    # 2. Pronalazimo sam element dropdown menija (koji ima id "dropdown")
    dropdown_element = driver.find_element(By.ID, "dropdown")

    # 3. Pravimo objekat tipa Select jer se radi o padajucem meniju
    dropdown = Select(dropdown_element)

    # 4. Biramo opciju po njenom vidljivom tekstu ("Option 1")
    dropdown.select_by_visible_text("Option 1")

    # 5. Proveravamo da il je opcija zaista izabrana (first_selected_option vraca selektovanu opciju)
    selected_option = dropdown.first_selected_option

    # Assert proverava da li je tekst izabrane opcije "Option 1"
    assert selected_option.text == "Option 1"