from selenium.webdriver.common.by import By


class EbayHomePage:

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    URL = "https://www.ebay.com"
    TITLE = "Electronics, Cars, Fashion, Collectibles & More | eBay"

    # Element Locators
    EBAY_LOGO = (By.ID, "gh-la")
    SEARCH_FIELD = (By.ID, "gh-ac")
    SEARCH_BUTTON = (By.ID, "gh-btn")

    # Methods

    def navigate_to_page(self):
        self.browser.get(self.URL)

    def verify_page_title(self):
        assert self.browser.title == self.TITLE

    def search_for_item(self, item):
        search_field = self.browser.find_element(*self.SEARCH_FIELD)
        search_field.clear()
        search_field.send_keys(item)
        search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        search_button.click()