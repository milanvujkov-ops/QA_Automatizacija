import sqlite3
import pytest


# --- 1. DEO: FIXTURE (Priprema i čišćenje baze) ---
@pytest.fixture
def setup_proizvodi():
  # Povezujemo se na bazu i kreiramo kursor
  connection = sqlite3.connect("shop.db")
  cursor = connection.cursor()

  # Kreiramo tabelu ako ne postoji
  cursor.execute(
      "CREATE TABLE IF NOT EXISTS proizvodi (id INTEGER PRIMARY KEY, naziv"
      " TEXT, cena INTEGER);"
  )

  # Ubacujemo testni proizvod
  cursor.execute(
      "INSERT INTO proizvodi (naziv, cena) VALUES ('Laptop', 80000);"
  )
  connection.commit()

  # Šaljemo kursor testu
  yield cursor

  # Čišćenje nakon testa (brišemo proizvod i zatvaramo konekciju)
  cursor.execute("DELETE FROM proizvodi WHERE naziv = 'Laptop';")
  connection.commit()
  connection.close()


# --- 2. DEO: TEST (Automatska provera) ---
def test_provera_cene_laptopa(setup_proizvodi):
  # Preuzimamo kursor koji nam je fixture poslao
  cursor = setup_proizvodi

  # Izvršavamo upit
  cursor.execute("SELECT cena FROM proizvodi WHERE naziv = 'Laptop';")
  rezultat = cursor.fetchone()

  # Provere (assert)
  assert rezultat is not None, "Greška: Laptop nije pronađen u bazi!"
  assert (
      rezultat[0] == 80000
  ), f"Očekivana cena je 80000, a dobijena je {rezultat[0]}"

  print("Test uspešno položen! Cena laptopa je tačno 80000.")