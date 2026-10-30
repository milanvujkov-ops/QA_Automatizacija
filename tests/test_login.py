from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_uspesan_login(driver):
    wait = WebDriverWait(driver, 25)
    # ... tvoj kod za unos kredencijala i klik na login ...
    
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
    login = LoginPage(driver)
    login.otvori()
    login.unesi_email("milan_test_2026_99@gmail.com")
    login.unesi_lozinku("Lozinka123!")
    login.klikni_login()

    login.klikni_logout()
    assert "automationexercise.com" in driver.current_url