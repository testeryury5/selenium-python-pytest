from selenium.webdriver.common.by import By
from pages.tesla_home_page import TeslaHomePage

class TeslaShopPage(TeslaHomePage):

    # Initializer
    def __init__(self, browser):
        self.browser = browser
        TeslaHomePage.__init__(self, browser)

    URL = 'https://shop.tesla.com'
    TITLE = 'The Official Tesla Shop | Tesla'

    # Element Locators
    SHOP_NOW = (By.CSS_SELECTOR, "[aria-describedby='hero-0']")
    SHOP_CYBERTRUCK = (By.CSS_SELECTOR, "[aria-describedby='Cybertruck']")
    SHOP_MODEL_S = (By.CSS_SELECTOR, "[aria-describedby='Model-S']")
    SHOP_MODEL_3 = (By.CSS_SELECTOR, "[aria-describedby='Model-3']")
    SHOP_MODEL_X = (By.CSS_SELECTOR, "[aria-describedby='Model-X']")
    SHOP_MODEL_Y = (By.CSS_SELECTOR, "[aria-describedby='Model-Y']")
    SHOP_CHARING = (By.CSS_SELECTOR, "[aria-describedby='Charing']")


    # Methods
    def click_on_vehicles(self):
        cybertruck = self.browser.find_element(*self.SHOP_NOW)
        cybertruck.click()

