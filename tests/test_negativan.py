import pytest
from selenium.webdriver.common.by import By

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
        self.driver.find_element(*self.polje_korisnicko_ime).send_keys(username)
        self.driver.find_element(*self.polje_lozinka).send_keys(password)
        self.driver.find_element(*self.dugme_za_prijavu).click()


# 2. TEST FUNKCIJA (driver dolazi automatski iz conftest.py)
def test_uspjesna_prijava(driver):
    login_stranica = LoginPage(driver)
    login_stranica.otvori()
    login_stranica.prijavi_se("student", "Password123")
    assert "logged-in-successfully" in driver.current_url

# 3. TEST POGRESNA PRIJAVA
def test_pogresna_prijava(driver):
    login_stranica = LoginPage(driver)
    login_stranica.otvori()
    login_stranica.prijavi_se("student", "PogresnaPassword123")
    assert "logged-in-successfully" not in driver.current_url