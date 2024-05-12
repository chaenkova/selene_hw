import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope="function",autouse=True)
def browser_settings():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.timeout = 2
    browser.config.base_url = 'https://demoqa.com'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser.config.driver_options = options

    yield
    browser.quit()