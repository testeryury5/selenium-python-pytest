import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser():
    opts = webdriver.ChromeOptions()
    # opts.add_argument('headless')
    service = ChromeService(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=opts)
    browser.maximize_window()
    yield browser
    browser.quit()
