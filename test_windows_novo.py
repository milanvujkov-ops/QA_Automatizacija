from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_multiple_windows(driver):
  # 1. Otvaramo stranicu
  driver.get("https://the-internet.herokuapp.com/windows")

  wait = WebDriverWait(driver, 10)

  # 2. Pamtim ID originalnog (prvog) prozora
  originalni_prozor = driver.current_window_handle

  # 3. Klikćemo na link koji otvara novi tab/prozor
  link_novi_prozor = wait.until(
      EC.element_to_be_clickable((By.LINK_TEXT, "Click Here"))
  )
  link_novi_prozor.click()

  # 4. Čekamo da se pojavi novi prozor (da ukupan broj prozora bude 2)
  wait.until(lambda d: len(d.window_handles) > 1)

  # 5. Nalazimo ID novog prozora i prebacujemo fokus na njega
  for prozor in driver.window_handles:
    if prozor != originalni_prozor:
      driver.switch_to.window(prozor)
      break

  tekst_novog_prozora = wait.until(
      EC.presence_of_element_located((By.TAG_NAME, "h3"))
  ).text
  assert (
      tekst_novog_prozora == "New Window"
  ), f"Greška! Tekst je: {tekst_novog_prozora}"
  print(f"\n[USPEH] Uspešno prebačen fokus na novi prozor! Tekst: {tekst_novog_prozora}")

  # 6. (Opciono) Možemo da zatvorimo novi prozor i vratimo se na stari
  driver.close()
  driver.switch_to.window(originalni_prozor)