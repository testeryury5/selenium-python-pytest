import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

base_url = 'https://www.ebay.com/'
expected_title = 'Electronics, Cars, Fashion, Collectibles & More | eBay'


@pytest.mark.regressiontest
def test_ebay_search_bmw(browser):
    browser.get(base_url)
    assert expected_title in browser.title
    assert base_url in browser.current_url
    browser.find_element(By.LINK_TEXT, 'Motors').click()

    year_dropdown = Select(WebDriverWait(browser, 10).until(lambda b: b.find_element(By.NAME, 'Year')))
    year_dropdown.select_by_visible_text('2020')

    make_dropdown = Select(WebDriverWait(browser, 25).until(lambda b: b.find_element(By.NAME, 'Make')))
    make_dropdown.select_by_visible_text('BMW')

    model_dropdown = Select(WebDriverWait(browser, 6).until(EC.element_to_be_clickable(browser.find_element(By.NAME, 'Model'))))
    model_dropdown.select_by_visible_text('420i Gran Coupe')

    trim_dropdown = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable(browser.find_element(By.NAME, 'Trim'))))
    trim_dropdown.select_by_visible_text('Executive Hatchback 4-Door')

    find_button = WebDriverWait(browser, 3).until(EC.element_to_be_clickable(browser.find_element(By.XPATH, "//button[@type='submit'][text()='Find Parts']")))
    find_button.click()
    WebDriverWait(browser, 5).until(EC.title_contains('My Garage'))
    assert 'My Garage' in browser.title
    assert 'mygarage' in browser.current_url
