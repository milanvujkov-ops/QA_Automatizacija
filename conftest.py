import pytest
import os
from datetime import datetime
import pytest_html
from selenium import webdriver

# 1. Tvoja postojeća fixture za Firefox (ostaje tu gde jeste)
@pytest.fixture
def driver():
    # ... ovde je tvoje pokretanje Firefox/Chrome drajvera ...
    
    # Dodaj ove dve linije pre nego što vratiš driver:
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(10)  # Čeka do 10 sekundi za svaki element automatski
    
    yield driver
    driver.quit()

# 2. Novi dodatak za automatske skrinšotove pri padu testa i HTML izveštaje
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver") or getattr(item.instance, "driver", None)
        
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_name = f"screenshots/fail_{item.name}_{timestamp}.png"
            
            driver.save_screenshot(screenshot_name)
            print(f"\n[INFO] Skrinšot sačuvan: {screenshot_name}")
            
            if hasattr(report, "extra"):
                report.extra.append(pytest_html.extras.image(screenshot_name))
            else:
                report.extra = [pytest_html.extras.image(screenshot_name)]