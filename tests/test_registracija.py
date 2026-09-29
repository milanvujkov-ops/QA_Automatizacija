import pytest
from pages.registracija_page import RegistracijaPage
from faker import Faker

fake = Faker()

@pytest.mark.smoke
def test_registracija_korisnika(driver):
    registracija = RegistracijaPage(driver)
    
    nasumicno_ime = fake.first_name()
    nasumicno_prezime = fake.last_name()
    nasumicni_email = fake.email()
    nasumicna_lozinka = "Lozinka123!"
    nasumicna_adresa = fake.street_address()
    nasumicni_grad = fake.city()
    nasumicni_postanski_broj = fake.postcode()
    nasumicni_telefon = fake.phone_number()

    registracija.otvori()
    registracija.unesi_ime(nasumicno_ime)
    registracija.unesi_email(nasumicni_email)
    registracija.klikni_signup()

    registracija.unesi_lozinku(nasumicna_lozinka)
    registracija.popuni_adresu(
        nasumicno_ime, 
        nasumicno_prezime, 
        nasumicna_adresa, 
        "Srbija", 
        nasumicni_grad, 
        nasumicni_postanski_broj,
        nasumicni_telefon
    )
    registracija.klikni_create_account()

    poruka = registracija.uzmi_tekst_potvrde()
    assert poruka == "ACCOUNT CREATED!"