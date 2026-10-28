from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_checkboxes(driver):
  # 1. Otvaramo stranicu sa checkbox-ovima
  driver.get("https://the-internet.herokuapp.com/checkboxes")

  wait = WebDriverWait(driver, 10)

  # 2. Pronalazimo prvi checkbox (ili sve preko zajedničkog selektora)
  checkboxi = wait.until(
      EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='checkbox']"))
  )

  # Prvi checkbox po default-u obično nije čekiran
  prvi_checkbox = checkboxi[0]

  # Proveravamo da li je čekiran
  if not prvi_checkbox.is_selected():
    print(
        "\n[INFO] Prvi checkbox nije čekiran. Kliknuto da se čekira!"
    )
    prvi_checkbox.click()

  # Provera preko assert-a
  assert (
      prvi_checkbox.is_selected()
  ), "Greška! Checkbox bi trebalo da bude čekiran."

  print("[USPEH] Checkbox test uspešno završen.")