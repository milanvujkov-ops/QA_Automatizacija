from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Lokatori
        self.name_input = (By.CSS_SELECTOR, 'input[data-qa="name"]')
        self.email_input = (By.CSS_SELECTOR, 'input[data-qa="email"]')
        self.subject_input = (By.CSS_SELECTOR, 'input[data-qa="subject"]')
        self.message_textarea = (By.CSS_SELECTOR, 'textarea[data-qa="message"]')
        self.file_upload_input = (By.NAME, "upload_file")
        self.submit_button = (By.CSS_SELECTOR, 'input[data-qa="submit-button"]')
        self.success_message = (By.XPATH, '//*[@class="status alert alert-success"]')

    def open(self, url):
        self.driver.get(url)

    def fill_contact_form(self, name, email, subject, message, file_path=None):
        self.wait.until(EC.visibility_of_element_located(self.name_input)).send_keys(name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.subject_input).send_keys(subject)
        self.driver.find_element(*self.message_textarea).send_keys(message)

        if file_path:
            self.driver.find_element(*self.file_upload_input).send_keys(file_path)

    def submit_form(self):
        element = self.driver.find_element(*self.submit_button)
        self.driver.execute_script("arguments[0].click();", element)
        
        # Prihvatanje JavaScript potvrdnog prozora (alert)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

    def get_success_message_text(self):
        element = self.wait.until(EC.visibility_of_element_located(self.success_message))
        return element.text