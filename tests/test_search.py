from pages.products_page import ProductsPage

import pytest

@pytest.mark.regression
def test_pretraga_proizvoda(driver):
    products_page = ProductsPage(driver)
    
    # 1. Otvaramo stranicu s proizvodima
    products_page.otvori()

    # 2. Pretražujemo pojam "Dress"
    pojam_pretrage = "Dress"
    products_page.pretrazi_proizvod(pojam_pretrage)

    # 3. Provjeravamo je li se pojavio naslov "SEARCHED PRODUCTS"
    assert products_page.da_li_je_prikazan_naslov_pretrage()

    # 4. Uzimamo sve pronađene nazive i verifikujemo da postoje rezultati
    nazivi_proizvoda = products_page.uzmi_sve_nazive_pretrazenih_proizvoda()
    assert len(nazivi_proizvoda) > 0, "Lista pretraženih proizvoda ne bi smjela biti prazna!"
    