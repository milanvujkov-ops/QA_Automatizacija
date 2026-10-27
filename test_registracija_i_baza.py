import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def test_registracija_i_baza():
  # --- DEO 1: Selenium UI Test ---
  driver = webdriver.Chrome()
  driver.get("http://localhost:3000")# ne radi jer ovaj link nije dobar

  # Popunjavamo formu preko Selenium-a
  driver.find_element(By.ID, "username").send_keys("pera_peric")
  driver.find_element(By.ID, "email").send_keys("pera@example.com")
  driver.find_element(By.ID, "submit_btn").click()

  # Zatvaramo pretraživač jer je UI deo završen
  driver.quit()

  # --- DEO 2: SQL Provera Bekenda ---
  # Povezujemo se na bazu da potvrdimo da je upis uspeo
  connection = sqlite3.connect("test_baza.db")
  cursor = connection.cursor()

  cursor.execute(
      "SELECT * FROM korisnici WHERE email = 'pera@example.com';"
  )
  rezultat = cursor.fetchone()

  connection.close()

  # Pytest assert proverava da li podatak postoji u bazi
  assert (
      rezultat is not None
  ), "Greška: Korisnik je uspešno viđen na ekranu, ali nije sačuvan u bazi!"
  print("Test uspešno položen! UI i baza su sinhronizovani.")