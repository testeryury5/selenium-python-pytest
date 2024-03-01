import time

import pytest
from pages.tesla_shop_page import TeslaShopPage


@pytest.mark.heritage
def test_tesla_shop(browser):
    shop_page = TeslaShopPage(browser)
    shop_page.navigate_to_home_page()
    shop_page.verify_page_title()
    time.sleep(3)
    shop_page.click_on_vehicles()
    time.sleep(3)
