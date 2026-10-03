from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Pokrećemo Chrome brauzer
driver = webdriver.Chrome()

try:
    # 2. Otvaramo test stranicu (koristićemo stabilnu stranicu za vežbu)
    driver.get("https://the-internet.herokuapp.com/login")

    # 3. Pronalazimo polje za korisničko ime preko ID-ja i upisujemo tekst
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    # 4. Pronalazimo polje za lozinku preko ID-ja i upisujemo lozinku
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")

    # 5. Pronalazimo dugme za login preko CSS selektora (klase) i klikćemo
    login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
    login_button.click()

    # Pauza od 3 sekunde da vidiš rezultat pre nego što se zatvori
    time.sleep(3)

finally:
    # 6. Obavezno gasimo brauzer na kraju da ne ostanu procesi u pozadini
    driver.quit()