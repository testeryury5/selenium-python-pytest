import time

from pages.tesla_home_page import TeslaHomePage
import pytest
import time


@pytest.mark.smoketestpom
def test_tesla_home_page(browser):
    tesla = TeslaHomePage(browser)
    tesla.navigate_to_home_page()
    tesla.click_on_vehicles()
    time.sleep(3)