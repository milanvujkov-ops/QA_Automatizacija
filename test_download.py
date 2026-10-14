import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_download(driver):
    # 1. Otvaramo stranicu za preuzimanje
    driver.get("https://the-internet.herokuapp.com/download")

    wait = WebDriverWait(driver, 10)

    # 2. Pronalazimo sve linkove sa klasom/lokacijom, uzimamo prvi koji je realan fajl (npr. preskačemo navigaciju ako je ima)
    # Na ovoj stranici fajl linkovi su direktno unutra, pa ćemo uzeti npr. prvi link koji ima tekst u sebi
    fajl_linkovi = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".example a")))
    
    # Uzimamo prvi link sa liste koji ima neki naziv fajla
    fajl_link = fajl_linkovi[0]
    ime_fajla = fajl_link.text
    
    # Klikćemo na link da pokrenemo preuzimanje
    fajl_link.click()

    # 3. Dajemo browseru par sekundi da preuzme fajl na računar
    time.sleep(3)

    # 4. Definišemo putanju do standardnog Downloads foldera na tvom računaru (OneDrive te možda vodi kroz poseban put, ali probaćemo standardni user folder)
    download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    fajl_putanja = os.path.join(download_folder, ime_fajla)

    # 5. Proveravamo pomoću assert-a da li fajl zaista postoji u Downloads folderu
    assert os.path.exists(fajl_putanja), f"Fajl {ime_fajla} nije uspešno preuzet u Downloads folder!"