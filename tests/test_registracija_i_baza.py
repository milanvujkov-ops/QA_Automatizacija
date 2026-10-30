import sqlite3
import pytest
from pages.registracija_page import RegistracijaPage
from faker import Faker

fake = Faker()

@pytest.mark.smoke
def test_registracija_i_baza_provera(driver):
    registracija = RegistracijaPage(driver)
    
    # Generišemo nasumične podatke
    nasumicno_ime = fake.first_name()
    nasumicno_prezime = fake.last_name()
    nasumicni_email = fake.email()
    nasumicna_lozinka = "Lozinka123!"
    
    # Korak 1: UI Registracija preko POM-a
    registracija.otvori()
    registracija.unesi_ime(nasumicno_ime)
    registracija.unesi_email(nasumicni_email)
    registracija.klikni_signup()

    registracija.unesi_lozinku(nasumicna_lozinka)
    registracija.popuni_adresu(
        nasumicno_ime, 
        nasumicno_prezime, 
        fake.street_address(), 
        "Srbija", 
        fake.city(), 
        fake.postcode(),
        fake.phone_number()
    )
    registracija.klikni_create_account()

    # Provera na UI-ju
    poruka = registracija.uzmi_tekst_potvrde()
    assert poruka == "ACCOUNT CREATED"

    # Korak 2: SQL Provera u bazi (Primer sa tvojom lokalnom / test bazom)
    # Ovde se povezujemo na bazu gde čuvaš podatke (npr. shop.db ili test_baza.db)
    connection = sqlite3.connect("shop.db")  # Ili naziv baze koju koristiš u projektu
    cursor = connection.cursor()

    # Primer upita (prilagodi naziv tabele i kolona tvojoj bazi)
    # cursor.execute("SELECT * FROM korisnici WHERE email = ?", (nasumicni_email,))
    # rezultat = cursor.fetchone()
    # connection.close()

    # assert rezultat is not None, "Greška: Korisnik je kreiran na UI-ju, ali nije nađen u bazi!"
    print("UI registracija uspešno završena!")