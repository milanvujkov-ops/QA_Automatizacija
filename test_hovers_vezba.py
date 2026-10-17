import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def test_hovers(driver):
    # 1. Otvaramo stranicu
    driver.get("https://the-internet.herokuapp.com/hovers")

    wait = WebDriverWait(driver, 20)

   # 2. Pronalazimo prvu sliku
    avatar = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='figure'])[1]")))

    # 3. Prelazimo mišem preko slike koristeći ActionChains:
    actions = ActionChains(driver)
   # 3. Prelazimo mišem preko slike i obavezno pozivamo .perform()!
    actions = ActionChains(driver)
    actions.move_to_element(avatar).perform()

     # 4. Proveravamo da se pojavio "View profile" u h5 elementu
    link_element = wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='figcaption']/a)[1]")))
    assert link_element.text == "View profile"