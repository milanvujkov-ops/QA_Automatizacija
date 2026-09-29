import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. PAGE OBJECT KLASA: Sadrži sve lokatore i akcije na stranici
class KontaktFormaPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.selenium.dev/selenium/web/web-form.html"
        # Lokatori elemenata
        self.polje_ime = (By.NAME, "my-text")
        self.padajuca_lista = (By.NAME, "my-select")
        self.dugme_submit = (By.CSS_SELECTOR, "button")
        self.poruka_uspeha = (By.ID, "message")

    def otvori(self):
        self.driver.get(self.url)

    def popuni_ime(self, ime):
        self.driver.find_element(*self.polje_ime).send_keys(ime)

    def izaberi_opciju(self, tekst_opcije):
        element = self.driver.find_element(*self.padajuca_lista)
        select = Select(element)
        select.select_by_visible_text(tekst_opcije)

    def klikni_submit(self):
        self.driver.find_element(*self.dugme_submit).click()

    def dobit_poruku_uspeha(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located(self.poruka_uspeha)).text


# 2. FIXTURE za otvaranje i zatvaranje preglednika
@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


# 3. TEST: Čist i izuzetno čitljiv kod
def test_popunjavanje_forme_pom(driver):
    # Inicijalizujemo stranicu
    forma_stranica = KontaktFormaPage(driver)
    
    # Izvršavamo korake
    forma_stranica.otvori()
    forma_stranica.popuni_ime("Petar")
    forma_stranica.izaberi_opciju("Two")
    forma_stranica.klikni_submit()
    
    # Verifikacija
    poruka = forma_stranica.dobit_poruku_uspeha()
    assert poruka == "Received!"