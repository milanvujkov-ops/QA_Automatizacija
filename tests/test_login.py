from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_uspesan_login(driver):
    wait = WebDriverWait(driver, 25)
    login = LoginPage(driver)
    login.otvori()
    
    # Unesi svoje kredencijale za uspešan login
    login.unesi_email("milan_test_2026_99@gmail.com")
    login.unesi_lozinku("TvojaPravaLozinka123")  # Zameni sa svojom tačnom lozinkom ako je drugačija
    login.klikni_login()
    
    # Čekamo da se pojavi "Logged in as" u headless modu
    logged_in_user = wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "Logged in as")]')))
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
    wait = WebDriverWait(driver, 25)
    login = LoginPage(driver)
    login.otvori()
    
    # Prvo se ulogujemo da bismo imali dugme za logout
    login.unesi_email("milan_test_2026_99@gmail.com")
    login.unesi_lozinku("TvojaPravaLozinka123")  # Zameni sa svojom tačnom lozinkom
    login.klikni_login()
    
    # Čekamo da se pojavi login/logout element i radimo logout
    wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "Logged in as")]')))
    
    # Pozivamo metodu za logout iz LoginPage klase
    login.klikni_logout()
    
    # Proveravamo da nas je vratilo na login stranicu ili da se pojavilo dugme za login
    login_dugme = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-qa="login-button"]')))
    assert login_dugme.is_displayed()