from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Lokatori za Korpu
        self.cart_link = (By.CSS_SELECTOR, 'a[href="/view_cart"]')
        self.cart_items = (By.CSS_SELECTOR, '#cart_info_table tbody tr')

    def ukloni_reklame(self):
        self.driver.execute_script("""
            var ads = document.querySelectorAll('iframe, .adsbygoogle, #aswift_0_wrap');
            for (var i = 0; i < ads.length; i++) {
                ads[i].remove();
            }
        """)

    def otvori_korpu(self):
        self.ukloni_reklame()
        btn = self.wait.until(EC.element_to_be_clickable(self.cart_link))
        self.driver.execute_script("arguments[0].click();", btn)

    def uzmi_broj_proizvoda_u_korpi(self):
        proizvodi = self.wait.until(EC.presence_of_all_elements_located(self.cart_items))
        return len(proizvodi)