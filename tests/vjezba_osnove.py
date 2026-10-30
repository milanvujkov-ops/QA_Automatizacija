import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class KontaktFormaPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.selenium.dev/selenium/web/web-form.html"
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


def test_popunjavanje_forme_pom(driver):
    forma_stranica = KontaktFormaPage(driver)
    
    forma_stranica.otvori()
    forma_stranica.popuni_ime("Petar")
    forma_stranica.izaberi_opciju("Two")
    forma_stranica.klikni_submit()
    
    poruka = forma_stranica.dobit_poruku_uspeha()
    assert poruka == "Received!"