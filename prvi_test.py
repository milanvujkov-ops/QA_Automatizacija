from selenium.webdriver.common.by import By
import time
from utils.logger import setup_logger

# Inicijalizujemo loger
logger = setup_logger()

def test_osnovni_login(driver):
    logger.info("--- POČETAK TESTA: test_osnovni_login ---")
    
    # 1. Otvaramo test stranicu (koristimo stabilnu stranicu za vežbu)
    driver.get("https://the-internet.herokuapp.com/login")
    logger.info(f"Otvorena stranica za login: {driver.current_url}")
    
    # 2. Pronalazimo polje za korisničko ime preko ID-ja i upisujemo tekst
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")
    logger.debug("Uneto korisničko ime: tomsmith")
    
    # 3. Pronalazimo polje za lozinku preko ID-ja i upisujemo lozinku
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    logger.debug("Uneta lozinka.")
    
    # 4. Pronalazimo dugme za login preko CSS selektora (klase) i klikćemo
    login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
    login_button.click()
    logger.info("Kliknuto na dugme za prijavu.")
    
    # Pauza od 3 sekunde da vidiš rezultat
    time.sleep(3)
    
    logger.info("--- KRAJ TESTA: Uspešno završen ---")