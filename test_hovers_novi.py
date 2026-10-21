import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def test_hovers_novi(driver):
    # 1. Otvaramo stranicu
    driver.get("https://the-internet.herokuapp.com/hovers")

    wait = WebDriverWait(driver, 20)

    # 2.Pronalazimo prvu sliku
    avatar = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='figure'])[1]")))

    # 3.Prelazimo misem preko slike koristeci ActionChains:
    actions = ActionChains(driver)

    # 4. Prelazimo misam preko slike i obavezno pozivamo .perform()!
    actions = ActionChains(driver)
    actions.move_to_element(avatar).perform()

    # 5. Proveravamo da se pojavio tekst "name: user1" u h5 elementu
    message_element = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='figcaption']/h5)[1]")))
    assert message_element.text == "name: user1"
