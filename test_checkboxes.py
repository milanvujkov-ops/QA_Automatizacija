from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_checkboxes(driver):
    # 1. Otvaramo stranicu sa checkbox-ovima
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    
    # 2. Pronalazimo checkbox-ove preko CSS selektora ili XPath-a
    # Na toj stranici checkbox-ovi se nalaze unutar form elementa
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    
    # Prvi checkbox (indeks 0) po defaultu obično nije čekiran
    # Hajde da kliknemo na njega da ga čekiramo
    checkboxes[0].click()
    
    # 3. Proveravamo preko assert-a da li je sada čekiran (is_selected() vraća True ako jeste)
    assert checkboxes[0].is_selected()