import sqlite3
import pytest


@pytest.fixture
def setup_baza_log():
  connection = sqlite3.connect("shop_log.db")
  cursor = connection.cursor()
  cursor.execute(
      "CREATE TABLE IF NOT EXISTS korisnici (id INTEGER PRIMARY KEY, email"
      " TEXT, status TEXT);"
  )
  connection.commit()

  yield cursor, connection

  cursor.execute("DELETE FROM korisnici;")
  connection.commit()
  connection.close()


@pytest.mark.parametrize(
    "email, status",
    [
        ("test1@gmail.com", "aktivan"),
        ("test2@gmail.com", "neaktivan"),
    ],
)
def test_status_korisnika(setup_baza_log, email, status):
  cursor, connection = setup_baza_log

  print(
      f"\n[INFO] Pokrećem upis korisnika sa email-om: {email} i statusom:"
      f" {status}"
  )

  # Ubacujemo korisnika u bazu
  cursor.execute(
      "INSERT INTO korisnici (email, status) VALUES (?, ?);", (email, status)
  )
  connection.commit()

  # Proveravamo upis
  cursor.execute("SELECT status FROM korisnici WHERE email = ?;", (email,))
  rezultat = cursor.fetchone()

  # Detaljna poruka u assert-u ako nešto pukne
  assert (
      rezultat is not None
  ), f"KRITIČNO: Korisnik sa email-om {email} nije sačuvan u bazi!"
  assert (
      rezultat[0] == status
  ), f"GREŠKA: Očekivani status je '{status}', ali je u bazi pronađen '{rezultat[0]}'."

  print(f"[USPEH] Korisnik {email} je uspešno proveren i test je položen.")