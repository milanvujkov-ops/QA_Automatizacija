from pages.products_page import ProductsPage

def test_dodavanje_proizvoda_u_korpu(driver):
    products_page = ProductsPage(driver)
    products_page.otvori()
    products_page.dodaj_prvi_proizvod_u_korpu()
    products_page.idi_u_korpu()

    naziv = products_page.uzmi_naziv_proizvoda_u_korpi()
    assert naziv == "Blue Top"

def test_uklanjanje_proizvoda_iz_korpe(driver):
    products_page = ProductsPage(driver)
    products_page.otvori()
    products_page.dodaj_prvi_proizvod_u_korpu()
    products_page.idi_u_korpu()

    # Uklanjamo proizvod i provjeravamo je li košarica prazna
    products_page.obrisi_proizvod_iz_korpe()
    assert products_page.da_li_je_korpa_prazna()