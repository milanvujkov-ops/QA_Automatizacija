import pytest

from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_uspesan_login(driver):
    wait = WebDriverWait(driver, 30)
    login = LoginPage(driver)
    
    login.otvori()
    login.unesi_email("milan_test_2026_99@gmail.com")
    login.unesi_lozinku("TvojaPravaLozinka123")
    
    # Siguran klik preko JavaScript-a ako slučajno neka reklama/iframe blokira element
    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-qa="login-button"]')))
    driver.execute_script("arguments[0].click();", login_btn)
    
    # Čekamo da se URL promeni sa login stranice na početnu/profilnu
    wait.until(EC.url_changes(driver.current_url))
    
    # Proveravamo da se pojavio tekst "Logged in as"
    logged_in_user = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//a[contains(text(), "Logged in as")]'))
    )
    assert logged_in_user.is_displayed()

def test_neuspesan_login(driver):
    login = LoginPage(driver)
    login.otvori()
    login.unesi_email("nepoznat_korisnik_999@gmail.com")
    login.unesi_lozinku("PogresnaLozinka123")
    login.klikni_login()

    poruka = login.uzmi_poruku_greske()
    assert poruka == "Your email or password is incorrect!"
    
def test_logout(driver):
    wait = WebDriverWait(driver, 30)
    login = LoginPage(driver)
    
    login.otvori()
    login.unesi_email("milan_test_2026_99@gmail.com")
    login.unesi_lozinku("TvojaPravaLozinka123")
    login.klikni_login()
    
    wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(text(), "Logged in as")]')))
    login.klikni_logout()
    
    login_dugme = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-qa="login-button"]')))
    assert login_dugme.is_displayed()