from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_hover(driver):
    # 1. Otvara stranicu
    driver.get("https://the-internet.herokuapp.com/hovers")

    wait = WebDriverWait(driver, 5)

    # 2. Pronalazimo prvu sličicu (sa ispravljenom zagradom u XPath-u)
    avatar = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='figure'])[1]")))

    # 3. Prelazimo mišem preko nje pomoću ActionChains (prosleđujemo promenljivu avatar)
    actions = ActionChains(driver)
    actions.move_to_element(avatar).perform()

    # 4. Proveravamo da se pojavio tekst "name: user1" u h5 elementu
    message_element = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='figcaption']/h5)[1]")))
    assert message_element.text == "name: user1"