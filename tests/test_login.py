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
    
    # I ovde prvo registrujemo unikatnog korisnika da bi login bio 100% uspešan
    email = fake.email()
    registracija.otvori()
    try:
        accept_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Consent')] | //button[contains(text(), 'Consent')] | //button[@aria-label='Consent']"))
        )
        accept_btn.click()
    except:
        pass # Ako se prozor ne pojavi, idemo dalje bez problema
    registracija.unesi_ime("TestUserLogout")
    registracija.unesi_email(email)
    registracija.klikni_signup()
    
    # Radimo login sa tim novim nalogom
    login.otvori()
    login.unesi_email(email)
    login.unesi_lozinku("TvojaPravaLozinka123")
    login.klikni_login()
    
    wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(text(), "Logged in as")]')))
    login.klikni_logout()
    
    login_dugme = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-qa="login-button"]')))
    assert login_dugme.is_displayed()