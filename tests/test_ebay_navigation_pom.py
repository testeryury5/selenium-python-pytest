import pytest
from pages.home_page import EbayHomePage


@pytest.mark.smoketestpom
def test_ebay_navigation(browser):
    home_page = EbayHomePage(browser)
    home_page.navigate_to_page()
    home_page.verify_page_title()
