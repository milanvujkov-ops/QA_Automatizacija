import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. PAGE OBJECT KLASA FOR LOGIN
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://practicetestautomation.com/practice-test-login/"
        
        # Lokatori elemenata
        self.polje_korisnicko_ime = (By.ID, "username")
        self.polje_lozinka = (By.ID, "password")
        self.dugme_za_prijavu = (By.ID, "submit")

    def otvori(self):
        self.driver.get(self.url)

    def prijavi_se(self, username, password):
        # Unosimo ime, lozinku i klikćemo na dugme
        self.driver.find_element(*self.polje_korisnicko_ime).send_keys(username)
        self.driver.find_element(*self.polje_lozinka).send_keys(password)
        self.driver.find_element(*self.dugme_za_prijavu).click()


# 2. FIXTURE ZA OTVALJANJE I ZATVARANJE BROWSERA
@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


# 3. TEST FUNKCIJA
def test_uspjesna_prijava(driver):
    login_stranica = LoginPage(driver)
    
    # 1. Otvaramo stranicu
    login_stranica.otvori()
    
    # 2. Prijavljujemo se sa validnim podacima
    login_stranica.prijavi_se("student", "Password123")
    
    # 3. Proveravamo da li nas je preusmerilo na stranicu uspešne prijave
    assert "logged-in-successfully" in driver.current_url

# 4. TEST POGRESNA PRIJAVA
def test_pogresna_prijava(driver):
    login_stranica = LoginPage(driver)

    # 1. Otvaramo stranicu
    login_stranica.otvori()

    # 2. Prijavljujemo se sa pogrešnim podacima
    login_stranica.prijavi_se("student", "PogresnaPassword123")

    # 3. Pogrešna prijava
    assert "logged-in-successfully" not in driver.current_url
    



