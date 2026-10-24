import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_tables(driver):
    # 1. Otvaramo stranicu
    driver.get("https://the-internet.herokuapp.com/tables")

    wait = WebDriverWait(driver, 20)

    # 2. Pronalazimo iznos duga (Due) za korisnika čiji je email jsmith@gmail.com
    # XPath traži polje sa emailom i uzima prvu sledeću kolonu u tom redu (Due)
    due_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "//table[@id='table1']//td[text()='jsmith@gmail.com']/following-sibling::td[1]"))
    )

    # 3. Proveravamo pomoću assert-a da li je taj iznos tačno "$50.00"
    assert due_element.text == "$50.00"
