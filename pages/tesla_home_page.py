from selenium.webdriver.common.by import By


class TeslaHomePage():

    def __init__(self, browser):
        self.browser = browser

    URL = "https://www.tesla.com"
    TITLE = "Electric Cars, Solar & Clean Energy | Tesla"

    # Element Locators
    SHOP_AVAILABLE = (By.LINK_TEXT, "Shop Available")
    DEMO_DRIVE = (By.LINK_TEXT, "Demo Drive")
    VEHICLES = (By.ID, "dx-nav-item--vehicles")


    # Methods

    def navigate_to_home_page(self):
        self.browser.get(self.URL)

    def click_on_vehicles(self):
        vehicles = self.browser.find_element(*self.VEHICLES)
        vehicles.click()

    def verify_page_title(self):
        assert self.browser.title == self.TITLE