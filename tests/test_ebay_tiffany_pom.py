import time

import pytest
from pages.home_page import EbayHomePage
from pages.search_page import SearchPage

@pytest.mark.smoketestpom
def test_search_tiffany(browser):
    home_page = EbayHomePage(browser)
    search_page = SearchPage(browser)
    home_page.navigate_to_page()
    home_page.verify_page_title()
    home_page.search_for_item("Tiffany")
    search_page.verify_title()
    time.sleep(3)
