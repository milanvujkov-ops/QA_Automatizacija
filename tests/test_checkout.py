import pytest
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.registracija_page import RegistracijaPage
from pages.checkout_page import CheckoutPage
from faker import Faker

fake = Faker()

@pytest.mark.smoke
def test_kompletna_kupovina(driver):
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    registracija = RegistracijaPage(driver)
    checkout_page = CheckoutPage(driver)

    # 1. Registrujemo novog korisnika (potrebno radi checkout procesa)
    nasumicno_ime = fake.first_name()
    nasumicno_prezime = fake.last_name()
    nasumicni_email = fake.email()

    registracija.otvori()
    registracija.unesi_ime(nasumicno_ime)
    registracija.unesi_email(nasumicni_email)
    registracija.klikni_signup()
    registracija.unesi_lozinku("Lozinka123!")
    registracija.popuni_adresu(
        nasumicno_ime, nasumicno_prezime, fake.street_address(),
        "Srbija", fake.city(), fake.postcode(), fake.phone_number()
    )
    registracija.klikni_create_account()

    # 2. Dodajemo proizvod u korpu
    products_page.otvori()
    products_page.dodaj_prvi_proizvod_u_korpu()

    # 3. Idemo u korpu i pokrećemo checkout
    cart_page.otvori_korpu()
    checkout_page.klikni_proceed_to_checkout()
    checkout_page.klikni_place_order()

    # 4. Unosimo podatke za plaćanje i potvrđujemo
    checkout_page.popuni_podatke_kartice(
        ime=f"{nasumicno_ime} {nasumicno_prezime}",
        broj="4111111111111111",
        cvc="311",
        mesec="12",
        godina="2028"
    )
    checkout_page.klikni_pay_and_confirm()

    # 5. Verifikacija uspešne kupovine
    poruka = checkout_page.uzmi_poruku_potvrde()
    assert poruka == "ORDER PLACED!"