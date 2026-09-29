import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def pytest_addoption(parser):
    parser.addoption(
        "--headless", action="store_true", default=False, help="Run tests in headless mode"
    )

@pytest.fixture
def driver(request):
    chrome_options = Options()
    if request.config.getoption("--headless"):
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == 'setup':
        xfail = getattr(report, 'wasxfail', False)
        if (report.failed and not xfail) or (report.skipped and xfail):
            driver = item.funcargs.get('driver', None)
            if driver:
                screenshots_dir = "screenshots"
                if not os.path.exists(screenshots_dir):
                    os.makedirs(screenshots_dir)
                
                file_name = f"{screenshots_dir}/{item.name}.png"
                driver.save_screenshot(file_name)
                
                if file_name:
                    html = f'<div><img src="{file_name}" alt="screenshot" style="width:600px;height:350px;" ' \
                           f'onclick="window.open(this.src)" align="right"/></div>'
                    extra.append(pytest_html.extras.html(html))
        report.extra = extra