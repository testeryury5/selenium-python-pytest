import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("item",
                         [
                             "Tiffany Rings",
                             "Tiffany Necklace",
                             "Tiffany Earings",
                             "Vintage Cars",
                         ])
@pytest.mark.regressiontest
def test_ebay_search_multiple_jewelry(browser, item):
    browser.get('https://www.ebay.com')
    browser.find_element(By.ID, 'gh-ac').send_keys(item)
    browser.find_element(By.ID, 'gh-btn').click()
    assert item in browser.title
