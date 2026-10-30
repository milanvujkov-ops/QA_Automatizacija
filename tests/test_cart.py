from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.products_page import ProductsPage

def test_dodavanje_proizvoda_u_korpu(driver):
    wait = WebDriverWait(driver, 20)
    products_page = ProductsPage(driver)
    
    products_page.otvori()
    
    # Čekamo da se proizvodi pojave pre nego što dodamo u korpu
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".features_items")))
    
    products_page.dodaj_prvi_proizvod_u_korpu()
    products_page.idi_u_korpu()

    naziv = products_page.uzmi_naziv_proizvoda_u_korpi()
    assert naziv == "Blue Top"

def test_uklanjanje_proizvoda_iz_korpe(driver):
    wait = WebDriverWait(driver, 20)
    products_page = ProductsPage(driver)
    
    products_page.otvori()
    
    # Čekamo da se proizvodi pojave pre nego što dodamo u korpu
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".features_items")))
    
    products_page.dodaj_prvi_proizvod_u_korpu()
    products_page.idi_u_korpu()

    # Uklanjamo proizvod i provjeravamo je li košarica prazna
    products_page.obrisi_proizvod_iz_korpe()
    assert products_page.da_li_je_korpa_prazna()