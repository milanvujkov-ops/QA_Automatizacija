from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_cookies(driver):
    # 1. Otvaramo stranicu
    driver.get("https://the-internet.herokuapp.com/")

    wait = WebDriverWait(driver, 10)

    # 2. Kreiramo i dodajemo novi kolačić u pretraživač
    moj_kolacic = {"name": "mojKolacic", "value": "12345"}
    driver.add_cookie(moj_kolacic)
    
    # 3. Uzimamo sve aktivne kolačiće sa stranice i ispisujemo ih u terminal
    svi_kolacici = driver.get_cookies()
    print("Svi kolačići:", svi_kolacici)
    
    # Proveravamo da li naš kolačić stvarno postoji u listi kolačića
    pronadjen = False
    for kolacic in svi_kolacici:
        if kolacic['name'] == 'mojKolacic':
            pronadjen = True
            break
            
    assert pronadjen, "Kolačić nije pronađen!"

    # 4. Brišemo taj specifični kolačić po imenu
    driver.delete_cookie("mojKolacic")

    # 5. Proveravamo da li je uspešno obrisan (da ga više nema)
    nakon_brisanja = driver.get_cookies()
    for kolacic in nakon_brisanja:
        assert kolacic['name'] != 'mojKolacic', "Kolačić nije obrisan!"

    # Možemo testirati i brisanje svih kolačića odjednom
    driver.delete_all_cookies()
    assert len(driver.get_cookies()) == 0, "Kolačići nisu svi obrisani!"