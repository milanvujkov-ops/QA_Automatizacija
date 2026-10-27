from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_iframe(driver):
  # 1. Otvaramo stranicu sa iframe-om
  driver.get("https://the-internet.herokuapp.com/windows")  # (ili /iframe, drži se svog driver.get)
  driver.get("https://the-internet.herokuapp.com/iframe")

  wait = WebDriverWait(driver, 10)

  # 2. Prebacujemo se u iframe preko ID-a
  wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "mce_0_ifr")))

  # 3. Nalazimo element za unos i brišemo postojeći tekst, pa upisujemo preko JavaScript-a
  editor = wait.until(EC.presence_of_element_located((By.ID, "tinymce")))

  # Čistimo i upisujemo tekst direktno preko JS-a da izbegnemo probleme sa fokusom editora
  driver.execute_script("arguments[0].innerHTML = 'Zdravo! QA obuku';", editor)

  # Proveravamo tekst
  unet_tekst = editor.text
  assert (
      "QA obuku" in unet_tekst
  ), f"Greška! Tekst nije unet, trenutno je: '{unet_tekst}'"
  print(f"\n[USPEH] Tekst uspešno unet: {unet_tekst}")

  # 4. Vraćamo se na glavni prozor
  driver.switch_to.default_content()

  # Proveravamo naslov na glavnoj strani
  naslov = wait.until(
      EC.presence_of_element_located((By.TAG_NAME, "h3"))
  ).text
  assert "An iFrame containing" in naslov
  print("[USPEH] Uspešno vraćen fokus na glavni prozor!")