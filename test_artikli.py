import sqlite3
import pytest


# --- 1. FIXTURE (Priprema i čišćenje baze) ---
@pytest.fixture
def setup_baza():
  # Povezujemo se na bazu i kreiramo kursor
  connection = sqlite3.connect("shop_test.db")
  cursor = connection.cursor()

  # Kreiramo tabelu 'artikli' ako ne postoji
  cursor.execute(
      "CREATE TABLE IF NOT EXISTS artikli (id INTEGER PRIMARY KEY, naziv"
      " TEXT, cena INTEGER);"
  )
  connection.commit()

  # Prosleđujemo kursor i konekciju testu
  yield cursor, connection

  # Čišćenje tabele i zatvaranje konekcije posle testa
  cursor.execute("DELETE FROM artikli;")
  connection.commit()
  connection.close()


# --- 2. PARAMETRIZOVANI TEST ---
@pytest.mark.parametrize(
    "naziv_artikla, ocekivana_cena",
    [
        ("Mis", 2500),
        ("Tastatura", 6000),
        ("Monitor", 22000),
    ],
)
def test_unos_i_provera_artikala(
    setup_baza, naziv_artikla, ocekivana_cena
):
  cursor, connection = setup_baza

  # 1. Ubacujemo artikal u bazu
  cursor.execute(
      "INSERT INTO artikli (naziv, cena) VALUES (?, ?);",
      (naziv_artikla, ocekivana_cena),
  )
  connection.commit()

  # 2. Proveravamo da li je artikal upisan sa tačnom cenom
  cursor.execute("SELECT cena FROM artikli WHERE naziv = ?;", (naziv_artikla,))
  rezultat = cursor.fetchone()

  # 3. Assert provere
  assert rezultat is not None, f"Artikal {naziv_artikla} nije pronađen u bazi!"
  assert (
      rezultat[0] == ocekivana_cena
  ), f"Greška za {naziv_artikla}! Očekivana cena: {ocekivana_cena}, a u bazi je: {rezultat[0]}"

  print(
      f"Uspešno testiran artikal: {naziv_artikla} sa cenom {ocekivana_cena} RSD."
  )