from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://automationexercise.com/login"
        self.driver.implicitly_wait(5)

        self.polje_email = (By.CSS_SELECTOR, 'input[data-qa="login-email"]')
        self.polje_lozinka = (By.CSS_SELECTOR, 'input[data-qa="login-password"]')
        self.dugme_login = (By.CSS_SELECTOR, 'button[data-qa="login-button"]')
        self.tekst_ulogovan = (By.XPATH, '//a[contains(text(), "Logged in as")]')
        self.poruka_greska = (By.CSS_SELECTOR, 'form[action="/login"] p')
        self.dugme_logout = (By.XPATH, '//a[contains(text(), "Logout")]')

    def otvori(self):
        self.driver.get(self.url)

    def unesi_email(self, email):
        self.driver.find_element(*self.polje_email).send_keys(email)

    def unesi_lozinku(self, lozinka):
        self.driver.find_element(*self.polje_lozinka).send_keys(lozinka)

    def klikni_login(self):
        element = self.driver.find_element(*self.dugme_login)
        self.driver.execute_script("arguments[0].click();", element)

    def uzmi_tekst_ulogovan(self):
        return self.driver.find_element(*self.tekst_ulogovan).text

    def uzmi_poruku_greske(self):
        return self.driver.find_element(*self.poruka_greska).text

    def klikni_logout(self):
        element = self.driver.find_element(*self.dugme_logout)
        self.driver.execute_script("arguments[0].click();", element)
    
