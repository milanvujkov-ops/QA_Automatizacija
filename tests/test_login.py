from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def prihvati_gdpr_akoiskoci(driver):
    try:
        wait = WebDriverWait(driver, 4)
        btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@aria-label, "Consent") or contains(text(), "Consent")]')))
        btn.click()
    except:
        pass

def test_uspesan_login(driver):
    wait = WebDriverWait(driver, 30)
    login = LoginPage(driver)
    
    login.otvori()
    prihvati_gdpr_akoiskoci(driver)
    
    login.unesi_email("milan_test_2026_99@gmail.com")
    login.unesi_lozinku("TvojaPravaLozinka123")
    login.klikni_login()
    
    logged_in_user = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Logged in as")]')))
    assert logged_in_user.is_displayed()

def test_neuspesan_login(driver):
    login = LoginPage(driver)
    login.otvori()
    prihvati_gdpr_akoiskoci(driver)
    
    login.unesi_email("nepoznat_korisnik_999@gmail.com")
    login.unesi_lozinku("PogresnaLozinka123")
    login.klikni_login()

    poruka = login.uzmi_poruku_greske()
    assert poruka == "Your email or password is incorrect!"

def test_logout(driver):
    wait = WebDriverWait(driver, 30)
    login = LoginPage(driver)
    
    login.otvori()
    prihvati_gdpr_akoiskoci(driver)
    
    login.unesi_email("milan_test_2026_99@gmail.com")
    login.unesi_lozinku("TvojaPravaLozinka123")
    login.klikni_login()
    
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Logged in as")]')))
    login.klikni_logout()
    
    login_dugme = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-qa="login-button"]')))
    assert login_dugme.is_displayed()