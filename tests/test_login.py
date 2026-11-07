import uuid
import time
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
    random_email = f"milan_test_{uuid.uuid4().hex[:6]}@gmail.com"
    
    login.otvori()
    prihvati_gdpr_akoiskoci(driver)
    
    # 1. Korak: Signup inicijalizacija
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-qa="signup-name"]'))).send_keys("Milan Test")
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="signup-email"]').send_keys(random_email)
    driver.find_element(By.CSS_SELECTOR, 'button[data-qa="signup-button"]').click()
    
    # 2. Korak: Detalji naloga sa stabilnim čekanjem
    wait.until(EC.element_to_be_clickable((By.ID, "id_gender1"))).click()
    driver.find_element(By.ID, "password").send_keys("TvojaPravaLozinka123")
    
    # Kratka pauza da DOM pohvata unose
    time.sleep(1)
    
    driver.find_element(By.ID, "first_name").send_keys("Milan")
    driver.find_element(By.ID, "last_name").send_keys("Vujkov")
    driver.find_element(By.ID, "address1").send_keys("Test Adresa 123")
    driver.find_element(By.ID, "state").send_keys("Vojvodina")
    driver.find_element(By.ID, "city").send_keys("Novi Sad")
    driver.find_element(By.ID, "zipcode").send_keys("21000")
    driver.find_element(By.ID, "mobile_number").send_keys("0611234567")
    
    # Siguran klik na dugme za kreiranje preko JavaScript-a
    create_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-qa="create-account"]')))
    driver.execute_script("arguments[0].click();", create_btn)
    
    logged_in = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Logged in as")]')))
    assert logged_in.is_displayed()

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