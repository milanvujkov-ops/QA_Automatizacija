from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


def test_dropdown_meni(driver):
  # 1. Otvaramo stranicu sa dropdown primerom
  driver.get("https://the-internet.herokuapp.com/dropdown")

  wait = WebDriverWait(driver, 10)

  # 2. Pronalazimo element select preko ID-ja
  element_padajuceg_menija = wait.until(
      EC.presence_of_element_located((By.ID, "dropdown"))
  )

  # 3. Inicijalizujemo Select klasu
  dropdown = Select(element_padajuceg_menija)

  # 4. Biramo opciju prema tekstu koji vidimo na ekranu
  dropdown.select_by_visible_text("Option 1")

  # 5. Proveravamo da li je izabrana opcija tačna
  izabrana_opcija = dropdown.first_selected_option.text
  assert (
      izabrana_opcija == "Option 1"
  ), f"Greška! Izabrano je: {izabrana_opcija}"

  print(
      f"\n[USPEH] Uspešno izabrana opcija iz dropdown menija: {izabrana_opcija}"
  )