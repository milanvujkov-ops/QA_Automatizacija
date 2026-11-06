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
    wait = WebDriverWait(driver, 40)

    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    registracija = RegistracijaPage(driver)
    checkout_page = CheckoutPage(driver)

    # 1. Registracija novog korisnika do kraja
    registracija.otvori()
    nasumicno_ime = fake.first_name()
    nasumicno_email = fake.email()

    registracija.unesi_ime(nasumicno_ime)
    registracija.unesi_email(nasumicno_email)
    registracija.klikni_signup()

    # Završetak registracije
    registracija.unesi_lozinku("TvojaPravaLozinka123")
    registracija.popuni_adresu("Milan", "Vujkov", "Glavna 1", "United States", "Beograd", "21220", "060123456")
    registracija.klikni_create_account()

    # 2. Dodavanje u korpu
    products_page.otvori()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".features_items")))
    products_page.dodaj_prvi_proizvod_u_korpu()

    # 3. Prelazak u korpu i checkout
    cart_page.otvori_korpu()
    checkout_dugme = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".check_out")))
    checkout_dugme.click()
    
    # Možeš dodati i poziv checkout_page metoda ukoliko ih koristiš za dalji nastavak
    # npr. checkout_page.potvrdi_porudzbinu()