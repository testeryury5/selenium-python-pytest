import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.parametrize("year, make, model, submodel", [
    ("2022", "BMW", "K1600B", "Grand America"),
    ("1950", "BMW", "R24", "Single 247")
])
@pytest.mark.regressiontest
def test_find_parts_motorcycle(browser, year, make, model, submodel):
    browser.get("http://www.ebay.com")
    browser.find_element(By.LINK_TEXT, "Motors").click()
    WebDriverWait(browser, 10).until(EC.title_contains("Motors"))
    browser.find_element(By.NAME, "MOTORCYCLE").click()

    year_dropdown = Select(
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(browser.find_element(By.NAME, "Year"))))
    year_dropdown.select_by_visible_text(year)

    make_dropdown = Select(
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(browser.find_element(By.NAME, "Make"))))
    make_dropdown.select_by_visible_text(make)

    model_dropdown = Select(
        WebDriverWait(browser, 15).until(EC.element_to_be_clickable(browser.find_element(By.NAME, "Model"))))
    model_dropdown.select_by_visible_text(model)

    submodel_dropdown = Select(
        WebDriverWait(browser, 13).until(EC.element_to_be_clickable(browser.find_element(By.NAME, "Submodel"))))
    submodel_dropdown.select_by_visible_text(submodel)

    find_parts = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(browser.find_element(By.XPATH, "//button[text()='Find Parts']")))
    find_parts.click()

    WebDriverWait(browser, 10).until(EC.title_contains("My Garage"))
    assert "Garage" in browser.title
