from selenium.webdriver.firefox.options import Options
import pytest
import os
from datetime import datetime
import pytest_html
from selenium import webdriver

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    
    # Inicijalizacija drajvera
    driver_instance = webdriver.Firefox(options=options)
    driver_instance.set_window_size(1920, 1080)
    
    yield driver_instance
    
    driver_instance.quit()

# Automatski skrinšotovi pri padu testa i HTML izveštaji
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