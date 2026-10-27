from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_javascript_alert(driver):
  # 1. Otvaramo stranicu sa alert prozorima
  driver.get("https://the-internet.herokuapp.com/javascript_alerts")

  wait = WebDriverWait(driver, 10)

  # 2. Nalazimo dugme preko njegovog teksta i klikćemo ga
  dugme_alert = wait.until(
      EC.element_to_be_clickable(
          (By.XPATH, "//button[text()='Click for JS Alert']")
      )
  )
  dugme_alert.click()

  # 3. Čekamo da se alert pojavi i prebacujemo fokus na njega
  alert = wait.until(EC.alert_is_present())

  # 4. Pročitamo tekst sa alerta i kliknemo "OK" (accept)
  print(f"\n[INFO] Tekst sa alerta je: {alert.text}")
  alert.accept()

  # 5. Proveravamo da li se ispod pojavila poruka da smo uspešno kliknuli
  rezultat = wait.until(
      EC.presence_of_element_located((By.ID, "result"))
  ).text
  assert (
      rezultat == "You successfully clicked an alert"
  ), f"Greška! Rezultat je: {rezultat}"

  print("[USPEH] Alert je uspešno zatvoren i potvrđen!")