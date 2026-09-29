from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Lokatori
        self.proceed_to_checkout_btn = (By.CSS_SELECTOR, 'a.check_out')
        self.place_order_btn = (By.CSS_SELECTOR, 'a[href="/payment"]')
        
        # Lokatori za plaćanje
        self.name_on_card_input = (By.CSS_SELECTOR, 'input[name="name_on_card"]')
        self.card_number_input = (By.CSS_SELECTOR, 'input[name="card_number"]')
        self.cvc_input = (By.CSS_SELECTOR, 'input[name="cvc"]')
        self.expiry_month_input = (By.CSS_SELECTOR, 'input[name="expiry_month"]')
        self.expiry_year_input = (By.CSS_SELECTOR, 'input[name="expiry_year"]')
        self.pay_button = (By.CSS_SELECTOR, 'button[data-qa="pay-button"]')
        
        self.order_placed_title = (By.CSS_SELECTOR, 'h2[data-qa="order-placed"]')

    def ukloni_reklame(self):
        self.driver.execute_script("""
            var ads = document.querySelectorAll('iframe, .adsbygoogle, #aswift_0_wrap');
            for (var i = 0; i < ads.length; i++) {
                ads[i].remove();
            }
        """)

    def klikni_proceed_to_checkout(self):
        self.ukloni_reklame()
        btn = self.wait.until(EC.element_to_be_clickable(self.proceed_to_checkout_btn))
        self.driver.execute_script("arguments[0].click();", btn)

    def klikni_place_order(self):
        self.ukloni_reklame()
        btn = self.wait.until(EC.element_to_be_clickable(self.place_order_btn))
        self.driver.execute_script("arguments[0].click();", btn)

    def popuni_podatke_kartice(self, ime, broj, cvc, mesec, godina):
        self.wait.until(EC.visibility_of_element_located(self.name_on_card_input)).send_keys(ime)
        self.driver.find_element(*self.card_number_input).send_keys(broj)
        self.driver.find_element(*self.cvc_input).send_keys(cvc)
        self.driver.find_element(*self.expiry_month_input).send_keys(mesec)
        self.driver.find_element(*self.expiry_year_input).send_keys(godina)

    def klikni_pay_and_confirm(self):
        self.ukloni_reklame()
        btn = self.wait.until(EC.element_to_be_clickable(self.pay_button))
        self.driver.execute_script("arguments[0].click();", btn)

    def uzmi_poruku_potvrde(self):
        element = self.wait.until(EC.visibility_of_element_located(self.order_placed_title))
        return element.text