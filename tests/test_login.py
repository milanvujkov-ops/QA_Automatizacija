from pages.login_page import LoginPage
from pages.registracija_page import RegistracijaPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

fake = Faker()

def test_uspesan_login(driver):
    wait = WebDriverWait(driver, 20)
    registracija = RegistracijaPage(driver)
    login = LoginPage(driver)
    
    # Prvo napravimo unikatnog korisnika
    email = fake.email()
    registracija.otvori()
    # Sačekaj da se stranica učita i da URL bude tačan
    wait.until(EC.url_contains("/login"))
    
    # Zatim kratko sačekaj da polje za ime bude prisutno u DOM-u
    wait.until(EC.presence_of_element_located((By.NAME, "name")))
    registracija.unesi_ime("TestUser")
    registracija.unesi_email(email)
    registracija.klikni_signup()
    
    # Sada radimo login sa tim email-om
    login.otvori()
    login.unesi_email(email)
    login.unesi_lozinku("TvojaPravaLozinka123")
    login.klikni_login()
    
    logged_in_user = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(text(), "Logged in as")]')))
    assert logged_in_user.is_displayed()

def test_neuspesan_login(driver):
    login = LoginPage(driver)
    login.otvori()
    login.unesi_email("milan_test_2026_99@gmail.com")
    login.unesi_lozinku("PogresnaLozinka123")
    login.klikni_login()

    poruka = login.uzmi_poruku_greske()
    assert poruka == "Your email or password is incorrect!"

def test_logout(driver):
    wait = WebDriverWait(driver, 40)
    registracija = RegistracijaPage(driver)
    login = LoginPage(driver)
    
    # Registracija novog korisnika do kraja
    email = fake.email()
    registracija.otvori()
    registracija.unesi_ime("TestUser")
    registracija.unesi_email(email)
    registracija.klikni_signup()
    
    # OVO JE NEDOSTAJALO: Popunjavanje obaveznih polja da bi nalog stvarno bio kreiran
    registracija.unesi_lozinku("TvojaPravaLozinka123")
    registracija.popuni_adresu("Milan", "Vujkov", "Glavna 1", "United States", "Beograd", "21220", "060123456")
    registracija.klikni_create_account()

    # Sada radimo login sa tim email-om
    login.otvori()
    login.unesi_email(email)
    login.unesi_lozinku("TvojaPravaLozinka123")
    login.klikni_login()
    
    logged_in_user = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(text(), "Logged in as")]')))
    assert logged_in_user.is_displayed()