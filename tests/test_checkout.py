import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.registracija_page import RegistracijaPage
from pages.checkout_page import CheckoutPage
from faker import Faker

fake = Faker()

@pytest.mark.smoke
def test_kompletna_kupovina(driver):
    wait = WebDriverWait(driver, 45)

    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    registracija = RegistracijaPage(driver)
    checkout_page = CheckoutPage(driver)

    # 1. Registracija novog korisnika
    registracija.otvori()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-qa='signup-name']")))

    nasumicno_ime = fake.first_name()
    nasumicno_prezime = fake.last_name()
    nasumicni_email = fake.email()

    registracija.unesi_ime(nasumicno_ime)
    registracija.unesi_email(nasumicni_email)
    registracija.klikni_signup()

    # 2. Dodavanje u korpu sa stabilnim čekanjem
    products_page.otvori()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".features_items")))
    products_page.dodaj_prvi_proizvod_u_korpu()

    # 3. Prelazak u korpu i checkout
    cart_page.otvori_korpu()
    cart_page.idi_na_checkout()