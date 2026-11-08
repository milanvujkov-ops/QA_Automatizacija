from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from conftest import driver

class RegistracijaPage:
    def __init__(self, driver):
        self.driver = driver
        # Povećano vreme čekanja na 30 sekundi zbog CI servera
        self.wait = WebDriverWait(driver, 30)
        self.url = "https://automationexercise.com/login"

        # Lokatori - Prvi korak (stabilniji XPATH za CI)
        self.ime_input = (By.XPATH, '//input[@data-qa="signup-name"]')
        self.email_input = (By.XPATH, '//input[@data-qa="signup-email"]')
        self.signup_button = (By.XPATH, '//button[@data-qa="signup-button"]')
        
        # Lokatori - Drugi korak
        self.gender_mr_radio = (By.ID, 'id_gender1')
        self.password_input = (By.ID, 'password')
        self.first_name_input = (By.ID, 'first_name')
        self.last_name_input = (By.ID, 'last_name')
        self.address_input = (By.ID, 'address1')
        self.country_select = (By.ID, 'country')
        self.state_input = (By.ID, 'state')
        self.city_input = (By.ID, 'city')
        self.zipcode_input = (By.ID, 'zipcode')
        self.mobile_number_input = (By.ID, 'mobile_number')
        self.create_account_button = (By.CSS_SELECTOR, 'button[data-qa="create-account"]')
        
        self.success_title = (By.CSS_SELECTOR, 'h2[data-qa="account-created"]')

    def ukloni_reklame(self):
        try:
            self.driver.execute_script("""
                var ads = document.querySelectorAll('iframe, .adsbygoogle, #aswift_0_wrap');
                for (var i = 0; i < ads.length; i++) {
                    ads[i].remove();
                }
            """)
        except:
            pass

    def otvori(self):
        self.driver.get(self.url)
        # Automatsko prihvatanje kolačića na CI serveru ako se pojavi GDPR prozor
        try:
            cookie_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Consent')] | //button[contains(text(), 'Consent')] | //div[contains(@class, 'fc-dialog')]//button[contains(@class, 'fc-primary-button')]"))
            )
            cookie_button.click()
        except:
            pass # Ako nema kolačića, idemo dalje normalno

    def unesi_ime(self, ime):
        element = self.wait.until(EC.visibility_of_element_located(self.ime_input))
        element.send_keys(ime)

    def unesi_email(self, email):
        element = self.wait.until(EC.visibility_of_element_located(self.email_input))
        element.send_keys(email)

    def klikni_signup(self):
        # Uklonjeno obavezno brisanje reklame pre klika da ne bi blokiralo CI
        btn = self.wait.until(EC.element_to_be_clickable(self.signup_button))
        self.driver.execute_script("arguments[0].click();", btn)

    def unesi_lozinku(self, lozinka):
        # Izbor pola (Mr)
        mr_radio = self.wait.until(EC.element_to_be_clickable(self.gender_mr_radio))
        self.driver.execute_script("arguments[0].click();", mr_radio)
        
        element = self.wait.until(EC.visibility_of_element_located(self.password_input))
        element.send_keys(lozinka)

    def popuni_adresu(self, ime, prezime, adresa, drzava, grad, postanski_broj, telefon):
        self.wait.until(EC.visibility_of_element_located(self.first_name_input)).send_keys(ime)
        self.driver.find_element(*self.last_name_input).send_keys(prezime)
        self.driver.find_element(*self.address_input).send_keys(adresa)
        
        drzava_dropdown = Select(self.driver.find_element(*self.country_select))
        try:
            drzava_dropdown.select_by_visible_text(drzava)
        except:
            drzava_dropdown.select_by_visible_text("India")

        # Popunjavanje state, city, zipcode i telefona
        self.driver.find_element(*self.state_input).send_keys("Vojvodina")
        self.driver.find_element(*self.city_input).send_keys(grad)
        self.driver.find_element(*self.zipcode_input).send_keys(postanski_broj)
        self.driver.find_element(*self.mobile_number_input).send_keys(telefon)

    def klikni_create_account(self):
        self.ukloni_reklame()
        btn = self.wait.until(EC.element_to_be_clickable(self.create_account_button))
        self.driver.execute_script("arguments[0].click();", btn)

    def uzmi_tekst_potvrde(self):
        element = self.wait.until(EC.visibility_of_element_located(self.success_title))
        return element.text

    # Za klik na dugme:
    element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "tvoj_id"))
    )
    element.click()

    # Za unos teksta:
    input_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "tvoj_id"))
    )
    input_field.send_keys("tekst")