from selenium.webdriver.firefox.options import Options
import pytest
import os
from datetime import datetime
import pytest_html
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    
    # Provera da li sistemski geckodriver postoji (Docker/Linux), inače koristi GeckoDriverManager
    if os.path.exists("/usr/local/bin/geckodriver"):
        service = Service(executable_path="/usr/local/bin/geckodriver")
    else:
        service = Service(GeckoDriverManager().install())
        
    driver_instance = webdriver.Firefox(
        service=service, 
        options=options
    )
    driver_instance.set_window_size(1920, 1080)
    
    yield driver_instance
    driver_instance.quit()

# Automatski skrinšotovi pri padu testa i HTML izveštaji
import pytest
import pytest_html

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    # Proveravamo da li je test pao tokom izvršavanja ("call") ili pripreme ("setup")
    if report.when in ("call", "setup") and report.failed:
        # Tražimo drajver bilo kroz fixture ili kroz instancu klase
        driver = item.funcargs.get("driver") or getattr(item.instance, "driver", None)
        
        if driver is not None:
            # Hvatamo skrinšot kao base64 string direktno u HTML izveštaj
            screenshot_base64 = driver.get_screenshot_as_base64()
            extras.append(pytest_html.extras.image(screenshot_base64))
            report.extras = extras