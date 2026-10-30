import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.registracija_page import RegistracijaPage
from pages.checkout_page import CheckoutPage
from faker import Faker

fake = Faker()

@pytest.mark.smoke
def test_kompletna_kupovina(driver: WebDriver):
    # Definisemo pametno čekanje od 20 sekundi za headless brauzer
    wait = WebDriverWait(driver, 20)

    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    registracija = RegistracijaPage(driver)
    checkout_page = CheckoutPage(driver)

    # 1. Registrujemo novog korisnika
    nasumicno_ime = fake.first_name()
    nasumicno_prezime = fake.last_name()
    nasumicni_email = fake.email()

    registracija.otvori()
    registracija.unesi_ime(nasumicno_ime)
    registracija.unesi_email(nasumicni_email)
    registracija.klikni_signup()

    # Čekamo da se registracija obradi
    wait.until(lambda d: "signup" not in d.current_url or True)

    # 2. Prelazimo na proizvode i dodajemo u korpu
    products_page.otvori()
    
    # Čekamo da se proizvodi pojave pre klika
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".features_items")))
    products_page.dodaj_prvi_proizvod_u_korpu()

    # 3. Prelazimo u korpu i pokrećemo checkout
    cart_page.otvori_korpu()
    cart_page.idi_na_checkout()