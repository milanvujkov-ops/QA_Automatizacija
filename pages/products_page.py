from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = "https://automationexercise.com/products"

        # Lokatori za košaricu
        self.prvi_proizvod_dodaj_dugme = (By.CSS_SELECTOR, 'a[data-product-id="1"]')
        self.dugme_view_cart = (By.XPATH, '//u[contains(text(), "View Cart")]')
        self.naziv_proizvoda_u_korpi = (By.CSS_SELECTOR, 'td.cart_description h4 a')
        self.dugme_obrisi_proizvod = (By.CSS_SELECTOR, 'a.cart_quantity_delete')
        self.poruka_prazna_korpa = (By.ID, 'empty_cart')

        # Novi lokatori za pretragu
        self.search_input = (By.ID, 'search_product')
        self.search_button = (By.ID, 'submit_search')
        self.searched_products_title = (By.XPATH, '//h2[contains(text(), "Searched Products")]')
        self.product_list_names = (By.CSS_SELECTOR, 'div.productinfo p')

    def ukloni_reklame(self):
        self.driver.execute_script("""
            var ads = document.querySelectorAll('iframe, .adsbygoogle, #aswift_0_wrap');
            for (var i = 0; i < ads.length; i++) {
                ads[i].remove();
            }
        """)

    def otvori(self):
        self.driver.get(self.url)

    def dodaj_prvi_proizvod_u_korpu(self):
        element = self.wait.until(EC.element_to_be_clickable(self.prvi_proizvod_dodaj_dugme))
        self.driver.execute_script("arguments[0].click();", element)

    def idi_u_korpu(self):
        element = self.wait.until(EC.element_to_be_clickable(self.dugme_view_cart))
        self.driver.execute_script("arguments[0].click();", element)

    def uzmi_naziv_proizvoda_u_korpi(self):
        element = self.wait.until(EC.visibility_of_element_located(self.naziv_proizvoda_u_korpi))
        return element.text

    def obrisi_proizvod_iz_korpe(self):
        self.ukloni_reklame()
        element = self.wait.until(EC.element_to_be_clickable(self.dugme_obrisi_proizvod))
        element.click()

    def da_li_je_korpa_prazna(self):
        element = self.wait.until(EC.visibility_of_element_located(self.poruka_prazna_korpa))
        return element.is_displayed()

    # Nove metode za pretragu
    def pretrazi_proizvod(self, naziv_proizvoda):
        self.ukloni_reklame()
        search_box = self.wait.until(EC.visibility_of_element_located(self.search_input))
        search_box.clear()
        search_box.send_keys(naziv_proizvoda)
        
        button = self.driver.find_element(*self.search_button)
        self.driver.execute_script("arguments[0].click();", button)

    def da_li_je_prikazan_naslov_pretrage(self):
        element = self.wait.until(EC.visibility_of_element_located(self.searched_products_title))
        return element.is_displayed()

    def uzmi_sve_nazive_pretrazenih_proizvoda(self):
        elements = self.wait.until(EC.presence_of_all_elements_located(self.product_list_names))
        return [el.text for el in elements]